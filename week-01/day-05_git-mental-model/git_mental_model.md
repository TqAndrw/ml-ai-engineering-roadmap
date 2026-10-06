# Git Mental Model

## Core Areas

Working Tree
→ git add
Staging Area / Index
→ git commit
Repository History

HEAD usually points to the current branch.
The current branch points to a commit.

## git diff

- `git diff`: working tree vs staging area
- `git diff --cached`: staging area vs HEAD

## Branches

A branch is a movable pointer to a commit.

Example:

A <- B <- C <- D
          ^    ^
        main experiment

HEAD points to the currently checked-out branch.

## add vs commit vs push

- `git add`: stages the current content/snapshot for the next commit.
- `git commit`: creates a new commit from the staged snapshot and advances the current branch.
- `git push`: transfers required commits/refs to a remote repository and updates the remote branch.

## Remote Tracking

- `main`: local branch
- `origin/main`: local remote-tracking reference representing the last known state of remote `main`

## Scratch Lab Evidence

Commits created:

- `1371926` — add A
- `2790866` — add B
- `6ae16b8` — add C on experiment

Final graph:

```text
1371926 <- 2790866 <- 6ae16b8
             ^          ^
           main     experiment
             ^
            HEAD

Sau đó quay về repo chính và chạy:

```bash
cd ~/projects/ml-ai-engineering-roadmap

git status
git add week-01/day-05_git-mental-model/git_mental_model.md

git status
git diff --cached --stat
