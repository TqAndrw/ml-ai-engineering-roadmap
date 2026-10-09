# Git Workflows, Conflicts & Recovery

## Merge vs Rebase

### Merge

Merge preserves the existing commit history and combines branches.

If two branches have diverged, Git may create a merge commit.

Example:

```text
        D --- E
       /       \
A --- B --- C --- M
```

Existing commits are not rewritten.

### Rebase

Rebase replays commits on top of a new base.

Example:

```text
Before:

        D --- E   feature
       /
A --- B --- C     main
```

After rebasing `feature` onto `main`:

```text
A --- B --- C --- D' --- E'
```

`D'` and `E'` are new commits with new commit identities/hashes.

Rebase is generally safer for local/private history than for already shared history.

---

## Fast-Forward Merge

A fast-forward merge is possible when the current branch is an ancestor of the branch being merged.

Example:

```text
A --- B --- C --- D --- E
          ^           ^
         main       feature
```

Running:

```bash
git switch main
git merge feature
```

can simply move the `main` pointer forward to `E`.

No merge commit is required.

---

## Merge Conflict

The lab created two competing changes to the same line.

Main:

```text
MODE=production
```

Feature:

```text
MODE=development
```

Git produced:

```text
<<<<<<< HEAD
MODE=production
=======
MODE=development
>>>>>>> feature
```

`HEAD` represented the currently checked-out branch, which was `main`.

The conflict was manually resolved to:

```text
MODE=production
```

Then:

```bash
git add config.txt
git commit -m "merge feature and resolve config conflict"
```

`git add` marked the conflict resolution in the staging area.

---

## Revert

A temporary commit was created:

```text
b986854 enable debug
```

Then:

```bash
git revert HEAD
```

created:

```text
9d7cff3 Revert "enable debug"
```

The original commit remained in history.

`git revert` creates a new commit that reverses the effect of an earlier commit without rewriting the existing history.

This makes it generally safer for shared history.

---

## Reset Modes

### `git reset --soft`

- moves HEAD/current branch
- keeps staging area
- keeps working tree

```text
HEAD      → moved
Staging   → kept
Working   → kept
```

### `git reset --mixed`

- moves HEAD/current branch
- resets staging area
- keeps working tree

```text
HEAD      → moved
Staging   → reset
Working   → kept
```

### `git reset --hard`

- moves HEAD/current branch
- resets staging area
- resets working tree

```text
HEAD      → moved
Staging   → reset
Working   → reset
```

`--hard` can discard uncommitted working-tree changes and should be used carefully.

---

## Reset vs Revert

`reset` moves branch history and can rewrite local history.

`revert` preserves existing history and adds a new inverse commit.

Practical rule:

```text
Local/private mistake  → reset may be appropriate
Shared/published mistake → revert is usually safer
```

---

## Stash

`git stash` temporarily stores uncommitted work so another task or branch can be worked on without creating a commit.

Lab command:

```bash
git stash push -m "temporary reset-lab change"
```

The stash was recorded as:

```text
stash@{0}: On reset-lab: temporary reset-lab change
```

It can later be restored using:

```bash
git stash pop
```

---

## Tags

A Git tag is a named reference to a commit.

The lab created:

```text
v0.1.0
```

pointing to:

```text
9d7cff3 Revert "enable debug"
```

This can represent a release or milestone.

---

## `.gitignore`

`.gitignore` prevents matching untracked files from normally being considered for tracking.

It does not automatically stop tracking a file that is already tracked.

For example:

```bash
git rm --cached .env
```

would remove `.env` from the Git index while leaving the local file available.

---

## Lab Commit Graph

The completed lab history included:

```text
* 9d7cff3 (main, tag: v0.1.0) Revert "enable debug"
* b986854 enable debug
*   d812844 merge feature and resolve config conflict
|\
| * 3bac045 feature config
* | d6b7de6 production config
|/
* b994a04 base config
```

A separate `reset-lab` branch was used to safely practise reset behaviour without damaging `main`.

---

## Key Takeaways

- Merge preserves existing commit history.
- Rebase rewrites the commits being replayed.
- Fast-forward merge only moves a branch pointer when no divergence exists.
- Merge conflicts require manual resolution when Git cannot safely combine changes.
- `reset --soft`, `--mixed`, and `--hard` affect HEAD, staging and working tree differently.
- Revert is usually safer for shared history.
- Stash is useful for temporary uncommitted work.
- Tags identify important commits such as releases.

