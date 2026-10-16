#!/usr/bin/env bash
set -euo pipefail
cd treasure-state
git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git add monitor.sqlite REPORT.md results.json evidence.json index.html
if ! git diff --cached --quiet; then
  git commit -m 'Persist Treasure Hunter audit and delivery state'
  git push origin HEAD:refs/heads/treasure-data
fi
