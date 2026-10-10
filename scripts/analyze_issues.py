import re

SUSPICIOUS_TERMS = (
    "pppdud", "take your money back", "follow my", "backflip",
    "gazillion", "value: 0.00", "approximately 0 usd",
    "currency: tbd", "currency not decided", "bounty is negative",
)

# These indicate a report claiming to have completed/submitted bounty work,
# not an offer inviting a new contributor to do the work.
NON_OFFER_MARKERS = (
    "bounty-submission",
    "submission id:",
    "submission package",
)

WEAK_CLAIMS = (
    "up to ", "terms and conditions apply", "expiry is",
    "pay you in btc", "pay in btc", "pay in crypto",
)

ACCEPTANCE_SIGNALS = (
    "acceptance criteria", "acceptance criterion", "definition of done",
    "expected behavior", "requirements", "reproduction steps",
    "steps to reproduce", "how to reproduce",
)

QUALITY_LABELS = ("good first issue", "help wanted", "bounty", "reward", "paid")


def detect_bounty(text):
    # Do not treat a submitter's claimed aggregate value as a new bounty offer.
    if any(marker in text.lower() for marker in NON_OFFER_MARKERS):
        return None
    patterns = (
        r"\$\s?([0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?)",
        r"(?:USD|US\$)\s?([0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?)",
        r"([0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?)\s*(?:USD\b|dollars?\b)",
    )
    values = []
    for pattern in patterns:
        for raw in re.findall(pattern, text, re.I):
            value = float(raw.replace(",", ""))
            if 0 < value <= 100000:
                values.append(value)
    return max(values) if values else None


def analyze_issue(issue, repo_meta=None, history=None):
    repo_meta = repo_meta or {}
    history = history or {}
    text = f"{issue.get('title', '')} {issue.get('body', '')}"
    lower = text.lower()
    labels = " ".join(x.get("name", "") for x in issue.get("labels", []))
    label_lower = labels.lower()

    value = detect_bounty(text)
    if value is None:
        return None
    suspicious = any(term in lower for term in SUSPICIOUS_TERMS)
    weak_claim = any(term in lower for term in WEAK_CLAIMS)

    quality = 0
    quality_reasons = []
    if any(term in lower for term in ACCEPTANCE_SIGNALS):
        quality += 20
        quality_reasons.append("clear requirements/acceptance")
    if any(label in label_lower for label in QUALITY_LABELS):
        quality += 10
        quality_reasons.append("useful issue label")
    if len(issue.get("body") or "") >= 500:
        quality += 10
        quality_reasons.append("detailed issue description")
    if any(term in lower for term in ("steps to reproduce", "reproduction steps", "how to reproduce")):
        quality += 10
        quality_reasons.append("reproduction guidance")
    quality = min(quality, 40)

    stars = repo_meta.get("stargazers_count", 0)
    forks = repo_meta.get("forks_count", 0)
    archived = repo_meta.get("archived", False)
    repo_score = min(stars / 100, 10) + min(forks / 20, 5)
    if repo_meta.get("pushed_at"):
        repo_score += 5
    if not archived:
        repo_score += 5
    repo_score = min(repo_score, 25)

    history_score = min(history.get("linked_merged", 0) * 7, 15)
    history_score += 2 if history.get("linked_closed") and not history.get("linked_merged") else 0
    history_score += min(history.get("merged", 0) * 2, 10)
    history_score += 5 if history.get("prs") else 0
    history_score = min(history_score, 15)

    maintainer = 0
    maintainer_reasons = []
    if issue.get("author"):
        maintainer += 5
        maintainer_reasons.append("identified issue author")
    if issue.get("comments", 0) >= 2:
        maintainer += 5
        maintainer_reasons.append("active discussion")
    if issue.get("updatedAt"):
        maintainer += 5
        maintainer_reasons.append("recently updated")
    maintainer = min(maintainer, 15)

    risk = 0
    risk_reasons = []
    if suspicious:
        risk += 60
        risk_reasons.append("suspicious wording")
    if weak_claim:
        risk += 15
        risk_reasons.append("conditional/weak payment claim")
    if archived:
        risk += 30
        risk_reasons.append("archived repository")
    if stars < 10:
        risk += 10
        risk_reasons.append("very low repository activity")
    if issue.get("comments", 0) == 0:
        risk += 5
        risk_reasons.append("no discussion")
    risk = min(risk, 100)

    confidence = (
        "high" if any(k in label_lower for k in ("bounty", "reward", "paid")) and not suspicious and not weak_claim
        else "medium" if not suspicious and not weak_claim
        else "low"
    )
    score = (
        min(value / 100, 50)
        + {"high": 10, "medium": 5, "low": 0}[confidence]
        + min(issue.get("comments", 0) / 10, 5)
        + repo_score + quality + history_score + maintainer
        - risk * 0.25
    )
    if risk >= 60:
        score -= 15

    competition = history.get("competition", "UNKNOWN")
    competition_reasons = list(history.get("competition_reasons", []))
    # Assigned issues are already claimed by someone; never label them GO.
    assignees = issue.get("assignees") or []
    if assignees:
        if competition != "HIGH":
            competition = "HIGH"
        competition_reasons.append(
            "%d contributor(s) already assigned" % len(assignees)
        )
    if competition == "HIGH":
        score -= 12
    elif competition in ("MEDIUM", "UNKNOWN"):
        score -= 5

    verdict = (
        "AVOID" if risk >= 60
        else "REVIEW" if competition in ("HIGH", "UNKNOWN")
        else "GO" if score >= 50 and risk <= 30
        else "REVIEW"
    )

    return {
        "value": value, "confidence": confidence, "risk": risk,
        "risk_reasons": risk_reasons, "quality": quality,
        "quality_reasons": quality_reasons, "history": history_score,
        "maintainer": maintainer, "opportunity": score, "verdict": verdict,
        "competition": competition, "competition_reasons": competition_reasons,
    }
