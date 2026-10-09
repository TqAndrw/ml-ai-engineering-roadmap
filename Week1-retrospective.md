# Week 1 Retrospective — Engineering Foundations

## What I learned

This week I built a stronger foundation in Linux, shell scripting, reproducible environments, and Git.

I learned how Python environments can differ because of operating systems, interpreter versions, dependencies, environment variables, and PATH configuration. I also learned that activating a virtual environment modifies the shell environment so that the virtual environment's executables are resolved before system-level Python executables.

For Linux, I practised filesystem navigation, users and groups, file permissions, processes, environment variables, and PATH resolution. I also learned how Unix tools can be composed using stdin, stdout, stderr, pipes, and redirection.

I created Bash scripts and Make targets to automate repeatable tasks. I learnt why idempotency matters and how Make uses dependencies and timestamps to decide whether a target should be rebuilt.

Finally, I developed a more precise Git mental model covering the working tree, staging area, commits, HEAD, branches, merge, rebase, reset, revert, stash, tags, and conflict resolution.

## What was difficult

The most difficult part was being precise about concepts that initially seemed similar.

Examples included:

- understanding that `git add` stages a snapshot rather than simply marking a file;
- distinguishing the working tree, staging area, and HEAD;
- remembering that a branch is a movable pointer to a commit;
- understanding that `origin/main` is a local remote-tracking reference;
- distinguishing `2>` from `2>&1`;
- remembering that `uniq` only collapses adjacent duplicate lines;
- understanding the differences between `reset --soft`, `--mixed`, and `--hard`;
- distinguishing merge, rebase, and fast-forward behaviour.

## Mental Models I Corrected

Several mental models became more precise during the week.

### PATH

The shell searches directories in `PATH` from left to right and uses the first matching executable.

### Virtual environments

A virtual environment isolates the Python-level project environment and dependencies. Activating it changes the shell environment, including placing the virtual environment's executable directory earlier in `PATH`.

### Unix pipelines

A pipe connects:

```text
stdout of command A -> stdin of command B
```

### Git areas

```text
Working Tree
    |
    | git add
    v
Staging Area / Index
    |
    | git commit
    v
Repository History
```

`HEAD` normally refers to the current branch, while the current branch points to a commit.

### Git branches

A branch is a movable pointer to a commit rather than a separate copy of the repository.

### Merge vs Rebase

Merge preserves the existing history structure.

Rebase replays commits onto a new base and therefore creates new commit identities.

Rebasing shared history can be dangerous because other developers may already depend on the old commit history.

### Reset vs Revert

`reset` can move branch history and change the staging area or working tree depending on the mode.

`revert` preserves history and creates a new commit that reverses the effect of an earlier commit.

## Evidence / Commits

Week 1 evidence includes:

- `6aa687d` — establish reproducible WSL development environment
- `0477e99` — Linux filesystem, permissions and process fundamentals
- `5f7e4ed` — shell pipelines and redirection lab
- `80a4873` — idempotent Bash setup and Make workflow
- `77d3fb5` — Git mental model and commit DAG
- `b4f8f31` — Git workflows, conflicts and recovery lab
- `94a7b98` — Week 1 retrospective

The repository also contains practical evidence including Bash scripts, Makefiles, shell pipeline outputs, Linux notes, Git DAGs, conflict-resolution exercises, reset/revert experiments, and reproducible environment documentation.

## Next Week Focus

The next stage is Python foundations.

The main focus will be moving from engineering environment fundamentals into a precise understanding of Python execution, objects, references, mutability, functions, iteration, and other core language behaviour.

I will continue using the same learning process:

1. understand the mental model;
2. predict behaviour before running code;
3. implement small experiments;
4. explain the result using active recall;
5. record evidence in Git.
