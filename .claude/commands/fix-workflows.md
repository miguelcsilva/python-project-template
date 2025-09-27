---
allowed-tools: Bash(gh:*), Bash(git:*), Read(*), Edit(*), MultiEdit(*), Glob(*), Grep(*), LS(*), Write(*)
description: Automatically detect and fix failing GitHub workflows on the current branch
---

# Fix Workflows Command

You are a GitHub workflow troubleshooter. Your task is to:

1. **Detect failing workflows** on the current branch using GitHub CLI
1. **Analyze failure logs** to understand what went wrong
1. **Apply automated fixes** based on the specific project's tools and configuration
1. **Commit the fixes** with a descriptive message

## Step-by-Step Process:

### 1. Check Current Branch and Workflow Status

- Use `git branch --show-current` to get the current branch
- Use `gh run list --branch <current-branch> --limit 5` to get recent workflow runs
- Identify failed runs with `gh run list --status failure --branch <current-branch> --limit 3`

### 2. Analyze Failure Details

For each failed run:

- Use `gh run view <run-id>` to get detailed information
- Use `gh run view <run-id> --log` to get full logs
- Parse the logs to identify failure types:
  - **Formatting issues**: Code formatting violations
  - **Linting issues**: Code quality/style violations
  - **Dependency issues**: Package installation or resolution failures
  - **Build failures**: Compilation or build process errors
  - **Test failures**: Test suite failures

### 3. Understand Project Configuration

- Examine workflow files in `.github/workflows/` to understand what commands failed
- Read project configuration files to understand the toolchain
- Look for scripts in package.json, Makefile, or other build files
- Identify the specific commands that were run and failed

### 4. Apply Fixes Based on Project Setup

- **For formatting issues**: Run the formatting commands found in the workflow or project scripts
- **For linting issues**: Run linting commands with auto-fix flags if available
- **For dependency issues**: Run the dependency installation commands from the workflow
- **For build issues**: Address based on error messages and re-run build steps
- **For test failures**: Analyze test output to understand failures, then:
  - Fix obvious code issues causing test failures
  - Update tests if they're broken due to valid code changes
  - If tests reveal actual bugs, fix the underlying code issues
  - Run tests locally to verify fixes before committing

The key is to use the exact same commands and tools that the project already uses, as defined in:

- Workflow YAML files
- Project configuration files
- Package manager scripts
- Build tool configurations

### 5. Commit and Push Changes

- Stage all changes: `git add .`
- Create a descriptive commit message:
  - Format: `fix: resolve <workflow-name> failures - <brief-description>`
  - Include what was fixed and why
- Create the commit with `git commit`
- Ask user before pushing changes

## Error Handling:

- If no failing workflows found, inform the user
- If GitHub CLI is not authenticated, provide setup instructions
- If fixes cannot be determined automatically, provide manual guidance
- If unsure about a fix, explain findings and ask for confirmation

## Output:

Provide clear feedback on:

- Which workflows were failing and why
- What fixes were applied
- The commit that was created

Start by checking the current branch and recent workflow runs.
