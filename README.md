# Paid Issue Finder

Open-source tool for finding GitHub issues that appear to contain monetary bounties and ranking the opportunities.

## 💜 Support the project

If Paid Issue Finder saves you time, consider supporting its development through **GitHub Sponsors**.

- [Sponsor Leonardo / Paid Issue Finder](https://github.com/sponsors/Lthighway)

GitHub Sponsors supports one-time and monthly sponsorships. For personal accounts, GitHub currently states that it charges no sponsorship fee, so 100% of personal-account sponsorships go to the sponsored developer.

## Free GitHub-native MVP

This repository can run the finder directly through **GitHub Actions**, without Render, Asaas, or a paid server.

Public repositories can use GitHub's standard hosted runners for free and without a usage limit for those standard runners.

### Run a search

1. Open the **Actions** tab.
2. Select **Paid Issue Finder**.
3. Click **Run workflow**.
4. Enter a GitHub search query, for example:
   `bounty state:open`
   or
   `bounty language:Python state:open`
5. Choose the number of results.
6. Run the workflow.
7. Open the workflow run and read the results in the job log.

The workflow uses the repository's GitHub token and does not require a personal access token for the basic public-repository search.

## Detection

The finder looks for monetary amounts such as `$500`, `US$500`, `500 USD`, and `500 dollars`.

It then considers bounty/reward labels, comments and suspicious text patterns to rank results.

**Important:** detected amounts are signals, not proof that a bounty will actually be paid. Always inspect the original issue and repository before doing work.

## Local API version

The FastAPI implementation in `app/` remains available for future deployment. It contains the earlier credit/payment prototype, but the GitHub-native workflow is the recommended zero-cost MVP.

## Roadmap

- Better bounty verification
- Repository reputation signals
- Duplicate/scam detection
- Saved searches
- Optional web interface
- Optional commercial API when the project has enough users to justify hosting costs

## License

MIT
