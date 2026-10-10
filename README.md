# Paid Issue Finder

Open-source tool for finding GitHub issues that appear to contain monetary bounties and ranking the opportunities.

**Status: experimental MVP.** The finder can produce ranked reports, but it does not guarantee that a reward is real or that a contributor will be paid. Verify the original issue and the maintainer's reward terms before spending time on a task.

## Free GitHub-native MVP

This repository can run the finder directly through **GitHub Actions**, without Render, Asaas, or a paid server.

**Try it now:** [view the latest public report](https://github.com/Lthighway/paid-issue-finder/blob/main/REPORT.md) · [run your own search in GitHub Actions](https://github.com/Lthighway/paid-issue-finder/actions/workflows/paid-issue-finder.yml)

### Run a search

1. Open the **Actions** tab.
2. Select **Paid Issue Finder**.
3. Click **Run workflow**.
4. Enter a GitHub search query, for example:
   \`bounty state:open\`
   or
   \`bounty language:Python state:open\`
5. Choose the number of results.
6. Run the workflow.
7. Open the workflow run and read the results in the job log or the generated \`REPORT.md\`.

The workflow uses the repository's GitHub token and does not require a personal access token for basic public-issue search.

## Detection and verification

The finder detects monetary amounts such as \`$500\`, \`US$500\`, \`500 USD\`, and \`500 dollars\`, then evaluates labels, issue detail, repository activity, history, and suspicious wording.

When a candidate is a mirrored bounty post, the workflow fetches the original GitHub issue and uses the original issue as the source of truth. A mirror is skipped if its original cannot be fetched or is no longer open.

**A detected amount is not proof of payment.** The score is a prioritization aid, not a guarantee. Confirm eligibility, acceptance criteria, reward terms, deadlines, and the maintainer's legitimacy before doing work.

## Commercialization status

The payment API in \`app/\` is a prototype, not a launched paid service. Before accepting customers, deploy it to a stable HTTPS host, configure production Asaas credentials and a strong webhook authentication token, test payment and refund/chargeback handling, and publish clear terms and support details.

The Asaas integration charges in **Brazilian reais (BRL)**. Never put API keys or webhook tokens in source control.

### Revenue hypothesis to validate

Keep the public report free to attract users. Interview active bounty hunters and validate demand before investing in hosting or marketing. Potential paid features include:

- Personalized filters by language, stack, bounty size, and risk.
- Email/Discord alerts for newly verified open issues.
- Saved searches and a daily or weekly digest.
- Exportable opportunity lists and transparent evidence for each score.

Potential subscription prices should be tested with users before being treated as final. Do not claim that the service guarantees earnings or verified payment.

### Give product feedback

Are you looking for paid GitHub issues? Tell us how you search today, which features would save you time, and whether personalized alerts or filters would be valuable.

- [Share product feedback](https://github.com/Lthighway/paid-issue-finder/issues/new?template=product_feedback.yml)

We are validating demand before investing in paid hosting or launching subscriptions. Feedback helps prioritize the product; it does not imply that paid features or a launch date are committed.

## 💜 Support the project

If Paid Issue Finder saves you time, consider supporting its development through **GitHub Sponsors**:

- [Sponsor Leonardo / Paid Issue Finder](https://github.com/sponsors/Lthighway)

A sponsorship is voluntary support for development; it is not a purchase of the paid API.

## License

MIT
