# 🧠 Git & GitHub Beginner Cheat Sheet

A simple, beginner-friendly cheat sheet for everyday Git and GitHub commands.

---

## 🔧 1. Initial Setup

```bash
git config --global user.name "Your Name"
# Sets your name for all commits

git config --global user.email "you@example.com"
# Sets your email for all commits

git config --list
# Lists all current Git config settings
```

---

## 📁 2. Starting a Project

```bash
git init
# Creates a new Git repo in the current folder

git clone https://github.com/user/repo.git
# Copies a GitHub repo to your local system
```

---

## 📄 3. Checking Status

```bash
git status
# Shows which files are new, modified, staged, or ignored
```

---

## ➕ 4. Adding Files

```bash
git add filename.ext
# Stages a single file

git add .
# Stages ALL modified and new files in the current folder
```

---

## ✅ 5. Committing Changes

```bash
git commit -m "Describe what you did"
# Saves your staged changes with a message
```

Example:

```bash
git commit -m "Fixed login bug and added validation"
```

---

## 🔄 6. Pulling and Pushing Code

```bash
git pull
# Gets the latest changes from the remote repo (e.g., GitHub)

git push
# Sends your committed changes to the remote repo
```

---

## 🌿 7. Working with Branches

```bash
git branch
# Lists all branches in your local repo

git branch new-branch
# Creates a new branch (but does NOT switch to it)

git checkout branch-name
# Switches to an existing branch

git checkout -b new-branch
# Creates AND switches to a new branch

git merge branch-name
# Merges another branch into your current one
```

---

## 🔙 8. Undoing Changes

```bash
git reset filename.ext
# Unstages a file (keeps the changes)

git checkout -- filename.ext
# Reverts the file to its last committed state (loses changes)

git reset --hard
# WARNING: Resets ALL changes and staging — use carefully!
```

---

## 📜 9. Viewing History

```bash
git log
# Shows full commit history with author, date, message

git log --oneline
# Shows a compact one-line-per-commit history
```

---

## 🛠️ 10. Everyday Workflow

```bash
git status
git add .
git commit -m "Your message"
git pull
git push
```

---

## 💡 Bonus Tips

- Always use `git status` to know what’s going on.
- Use meaningful commit messages.
- Use branches for new features or fixes.
- Pull before you push to avoid conflicts.
