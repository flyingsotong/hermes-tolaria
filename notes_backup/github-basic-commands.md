---
type: Note
---

**Clone** — download a repo from GitHub to your machine. You do this once.

```bash
git clone https://github.com/flyingsotong/magenta-theme.git /Users/alansoon/magenta-theme
```

---

**Commit** — save a snapshot of your changes locally. Think of it like hitting Save in a video game — it creates a named checkpoint.

```bash
git add -A                        # stage all changed files
git commit -m "what you changed"  # save the snapshot with a label
```

---

**Push** — send your local commits up to GitHub. Until you push, your snapshots only exist on your machine.

```bash
git push
```

---

**Pull** — download changes from GitHub to your machine. Use this if you ever edit on another computer and need to sync before working.

```bash
git pull
```

---

**Status** — see what files have changed since your last commit. Useful to check before committing.

```bash
git status
```

---

**Your normal workflow every time you make changes:**

```bash
git add -A
git commit -m "describe what you did"
git push
```

That's it. Clone is once. Add/commit/push is your loop every time you work.