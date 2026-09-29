# Linux Basics

## Absolute vs Relative Paths

An **absolute path** starts from the root directory `/`.

Example:

```text
/home/tristan/projects/ml-ai-engineering-roadmap
```

A **relative path** is interpreted from the current working directory.

Example:

```text
projects/ml-ai-engineering-roadmap
```

Useful path symbols:

- `.` = current directory
- `..` = parent directory
- `~` = current user's home directory
- `/` = filesystem root

For my current user:

```text
~ = /home/tristan
```

---

## Filesystem Hierarchy

Linux uses a single filesystem tree that starts from `/`.

Common directories:

- `/home` = user home directories
- `/etc` = system configuration
- `/usr` = user-space programs and libraries
- `/var` = logs and variable data
- `/tmp` = temporary files
- `/mnt` = mount points
- `/bin` = essential command-line programs

In WSL, Windows drives are mounted under `/mnt`.

Example:

```text
C:\Users\admin
```

is accessible from WSL as:

```text
/mnt/c/Users/admin
```

---

## Permissions

Linux permissions use:

- `r` = read
- `w` = write
- `x` = execute or traverse

Permissions are divided into three groups:

```text
owner | group | others
```

Example:

```text
-rw-r--r--
```

means:

```text
owner  = rw-
group  = r--
others = r--
```

Numeric values:

```text
r = 4
w = 2
x = 1
```

### 644

```text
644 = rw-r--r--
```

The owner can read and write.

The group and others can only read.

### 755

```text
755 = rwxr-xr-x
```

The owner can read, write and execute.

The group and others can read and execute.

For a file:

```text
x = execute the file
```

For a directory:

```text
x = traverse/access the directory
```

---

## Users and Groups

Linux uses users and groups to control access to files and system resources.

Useful commands:

```bash
whoami
id
groups
```

Example:

```text
uid=1000(tristan)
gid=1000(tristan)
```

A file can have:

- an owner
- a group
- permissions for owner, group and others

Example:

```text
-rw-r--r-- 1 tristan tristan demo.txt
```

Here:

- owner = `tristan`
- group = `tristan`

---

## Program vs Process

A **program** is code or an executable stored on disk.

Examples:

```text
/usr/bin/python3
/usr/bin/git
/usr/bin/sleep
```

A **process** is a running instance of a program.

A process has its own:

- PID
- memory
- environment variables
- open files
- runtime state

The same program can create multiple processes.

Example:

```text
python3 app.py
python3 app.py
```

These can create two different processes with different PIDs.

Useful process commands:

```bash
ps
ps aux
jobs
kill <PID>
```

The command:

```bash
sleep 300 &
```

starts `sleep` as a background process.

The `&` allows the shell to return the prompt immediately while the process continues running.

---

## PATH and `which`

`PATH` is an environment variable containing an ordered list of directories that the shell searches when resolving a command.

Example:

```text
/usr/local/bin:/usr/bin:/bin
```

When I run:

```bash
python3
```

the shell searches directories in `PATH` from left to right and uses the first matching executable.

The command:

```bash
which python3
```

shows which executable will be used.

Example:

```text
/usr/bin/python3
```

---

## Environment Variables

An environment variable stores key-value information available to a shell or process.

Example:

```bash
export MY_PROJECT="ml-roadmap"
```

Then:

```bash
echo $MY_PROJECT
```

returns:

```text
ml-roadmap
```

Using `export` makes the variable available to child processes started from the current shell.

Example:

```bash
python3 -c "import os; print(os.environ.get('MY_PROJECT'))"
```

can access the exported value.

Common environment variables include:

- `PATH`
- `HOME`
- `USER`

---

## Key Commands Practised

```bash
pwd
ls
ls -la
find
cd
whoami
id
groups
chmod
ps
jobs
kill
echo
which
export
```