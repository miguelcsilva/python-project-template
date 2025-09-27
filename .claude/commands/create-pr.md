---
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git branch:*), Bash(git log:*), Bash(gh pr create:*), Read, Grep
description: Create a pull request using gh CLI following the repository's PR template
---

## Context

- Current git status: !`git status`
- Current git diff from main branch: !`git diff main...HEAD`
- Current branch: !`git branch --show-current`
- Recent commits on branch: !`git log --oneline main..HEAD`

## Your task

1. Read the `.github/PULL_REQUEST_TEMPLATE.md` file
2. Create a pull request using `gh pr create` that follows the template structure and format
3. **IMPORTANT:** Include these flags in the `gh pr create` command:
   - `--label <appropriate-label>` to add the appropriate GitHub label
   - `--assignee <username>` to add assignees (check the template for recommended reviewers)
4. After creating the PR, provide only:
   - The PR URL
   - A one sentence summary of what was changed
