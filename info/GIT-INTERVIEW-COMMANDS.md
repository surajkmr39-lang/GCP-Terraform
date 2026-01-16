# 🎯 GIT COMMANDS FOR INTERVIEWS - Complete Reference

## 🔥 TOP 20 MOST USED GIT COMMANDS

### **1. git init** - Initialize Repository
```bash
git init
# Creates new Git repository in current directory
```

**When to use**: Starting a new project
**Interview tip**: "Initializes a new Git repository by creating a .git directory"

---

### **2. git clone** - Copy Repository
```bash
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my-folder
```

**When to use**: Getting a copy of existing repository
**Interview tip**: "Clones a remote repository to local machine with full history"

**Example**:
```bash
git clone https://github.com/surajkmr39-lang/GCP-Terraform.git
cd GCP-Terraform
```

---

### **3. git status** - Check Status
```bash
git status
git status -s  # Short format
```

**When to use**: See what files changed
**Interview tip**: "Shows working tree status - modified, staged, untracked files"

**Output example**:
```
On branch main
Changes not staged for commit:
  modified:   main.tf
  
Untracked files:
  new-file.txt
```

---

### **4. git add** - Stage Changes
```bash
git add file.txt           # Add specific file
git add .                  # Add all in current directory
git add -A                 # Add all changes everywhere
git add *.js               # Add all JavaScript files
git add src/               # Add entire directory
```

**When to use**: Prepare files for commit
**Interview tip**: "Stages changes for the next commit"

---

### **5. git commit** - Save Changes
```bash
git commit -m "Add login feature"
git commit -am "Fix bug"   # Add and commit modified files
git commit --amend         # Modify last commit
```

**When to use**: Save staged changes
**Interview tip**: "Creates a snapshot of staged changes with a message"

**Good commit messages**:
```bash
git commit -m "Fix: Resolve authentication timeout"
git commit -m "Feature: Add user dashboard"
git commit -m "Docs: Update API documentation"
git commit -m "Refactor: Optimize database queries"
git commit -m "Test: Add unit tests for login"
```

---

### **6. git push** - Upload to Remote
```bash
git push                        # Push current branch
git push origin main            # Push to main branch
git push -u origin main         # Push and set upstream
git push origin feature-branch  # Push specific branch
git push --force                # Force push (DANGEROUS)
```

**When to use**: Share commits with team
**Interview tip**: "Uploads local commits to remote repository"

---

### **7. git pull** - Download from Remote
```bash
git pull                   # Fetch and merge
git pull origin main       # Pull from main branch
git pull --rebase          # Pull and rebase instead of merge
```

**When to use**: Get latest changes from team
**Interview tip**: "Fetches and merges changes from remote repository"

**Difference**:
```bash
git pull = git fetch + git merge
```

---

### **8. git fetch** - Download Without Merge
```bash
git fetch                  # Fetch all branches
git fetch origin           # Fetch from origin
git fetch origin main      # Fetch specific branch
```

**When to use**: See remote changes without merging
**Interview tip**: "Downloads remote changes but doesn't merge them"

---

### **9. git branch** - Manage Branches
```bash
git branch                      # List local branches
git branch -a                   # List all branches (local + remote)
git branch feature-login        # Create new branch
git branch -d feature-login     # Delete branch
git branch -D feature-login     # Force delete
git branch -m old-name new-name # Rename branch
```

**When to use**: Work on features separately
**Interview tip**: "Manages branches for parallel development"

---

### **10. git checkout** - Switch Branches
```bash
git checkout main                    # Switch to main
git checkout -b feature-login        # Create and switch
git checkout -- file.txt             # Discard changes in file
git checkout abc123                  # Checkout specific commit
```

**When to use**: Switch between branches or restore files
**Interview tip**: "Switches branches or restores working tree files"

**Modern alternative**:
```bash
git switch main              # Switch branch
git switch -c feature-login  # Create and switch
git restore file.txt         # Restore file
```

---

### **11. git merge** - Combine Branches
```bash
git merge feature-branch     # Merge into current branch
git merge --no-ff feature    # Merge with merge commit
git merge --squash feature   # Squash commits
```

**When to use**: Integrate feature branch into main
**Interview tip**: "Combines changes from different branches"

**Example workflow**:
```bash
git checkout main
git merge feature-login
# Merges feature-login into main
```

---

### **12. git log** - View History
```bash
git log                          # Full history
git log --oneline                # Compact view
git log --graph --oneline        # Visual graph
git log -n 5                     # Last 5 commits
git log --author="John"          # By author
git log --since="2 weeks ago"    # By date
git log file.txt                 # File history
```

**When to use**: See commit history
**Interview tip**: "Shows commit history with details"

**Output example**:
```
abc123 (HEAD -> main) Add login feature
def456 Fix authentication bug
ghi789 Update documentation
```

---

### **13. git diff** - Show Changes
```bash
git diff                    # Unstaged changes
git diff --staged           # Staged changes
git diff main feature       # Between branches
git diff abc123 def456      # Between commits
git diff file.txt           # Specific file
```

**When to use**: See what changed
**Interview tip**: "Shows differences between commits, branches, or files"

---

### **14. git reset** - Undo Changes
```bash
git reset HEAD file.txt     # Unstage file
git reset --soft HEAD~1     # Undo commit, keep changes staged
git reset --mixed HEAD~1    # Undo commit, unstage changes
git reset --hard HEAD~1     # Undo commit, discard changes
git reset --hard origin/main # Match remote exactly
```

**When to use**: Undo commits or unstage files
**Interview tip**: "Resets current HEAD to specified state"

**Danger levels**:
```
--soft   = Safe (keeps changes)
--mixed  = Medium (unstages changes)
--hard   = DANGEROUS (deletes changes)
```

---

### **15. git revert** - Undo Commit Safely
```bash
git revert abc123           # Revert specific commit
git revert HEAD             # Revert last commit
git revert HEAD~3           # Revert 3rd last commit
```

**When to use**: Undo commit without rewriting history
**Interview tip**: "Creates new commit that undoes previous commit"

**reset vs revert**:
```
reset  = Rewrites history (dangerous for shared branches)
revert = Creates new commit (safe for shared branches)
```

---

### **16. git stash** - Save Work Temporarily
```bash
git stash                   # Save changes
git stash save "message"    # Save with message
git stash list              # List stashes
git stash pop               # Apply and remove
git stash apply             # Apply but keep
git stash drop              # Delete stash
git stash clear             # Delete all stashes
```

**When to use**: Switch branches without committing
**Interview tip**: "Temporarily stores modified files"

**Example**:
```bash
# Working on feature, need to fix bug
git stash
git checkout main
# Fix bug
git checkout feature
git stash pop
```

---

### **17. git remote** - Manage Remotes
```bash
git remote                      # List remotes
git remote -v                   # List with URLs
git remote add origin URL       # Add remote
git remote remove origin        # Remove remote
git remote rename old new       # Rename remote
git remote set-url origin URL   # Change URL
```

**When to use**: Connect to GitHub/GitLab
**Interview tip**: "Manages remote repository connections"

---

### **18. git tag** - Mark Releases
```bash
git tag                     # List tags
git tag v1.0.0              # Create tag
git tag -a v1.0.0 -m "msg"  # Annotated tag
git push origin v1.0.0      # Push tag
git push origin --tags      # Push all tags
git tag -d v1.0.0           # Delete local tag
```

**When to use**: Mark release versions
**Interview tip**: "Creates named references to specific commits"

---

### **19. git rebase** - Reapply Commits
```bash
git rebase main             # Rebase onto main
git rebase -i HEAD~3        # Interactive rebase
git rebase --continue       # Continue after conflict
git rebase --abort          # Cancel rebase
```

**When to use**: Clean up commit history
**Interview tip**: "Reapplies commits on top of another base"

**merge vs rebase**:
```
merge  = Creates merge commit (preserves history)
rebase = Linear history (cleaner but rewrites history)
```

---

### **20. git cherry-pick** - Apply Specific Commit
```bash
git cherry-pick abc123      # Apply commit
git cherry-pick abc123 def456 # Multiple commits
```

**When to use**: Apply specific commit from another branch
**Interview tip**: "Applies changes from specific commits"

---

## 🎯 REAL-WORLD SCENARIOS

### **Scenario 1: Start New Feature**
```bash
git checkout main
git pull origin main
git checkout -b feature/user-dashboard
# Make changes
git add .
git commit -m "Add user dashboard"
git push origin feature/user-dashboard
```

### **Scenario 2: Fix Merge Conflict**
```bash
git pull origin main
# CONFLICT in file.txt
# Edit file.txt to resolve
git add file.txt
git commit -m "Resolve merge conflict"
git push
```

### **Scenario 3: Undo Last Commit**
```bash
# Keep changes
git reset --soft HEAD~1

# Discard changes
git reset --hard HEAD~1
```

### **Scenario 4: Update Feature Branch**
```bash
git checkout feature-branch
git rebase main
# Or
git merge main
```

### **Scenario 5: Save Work Temporarily**
```bash
git stash
git checkout main
# Do something
git checkout feature-branch
git stash pop
```

---

## 🎤 INTERVIEW QUESTIONS & ANSWERS

### **Q1: "What's the difference between git pull and git fetch?"**

**Answer**:
"git fetch downloads changes from remote but doesn't merge them, while git pull does both fetch and merge in one command.

**fetch** is safer - you can review changes before merging:
```bash
git fetch origin
git diff origin/main
git merge origin/main
```

**pull** is quicker but automatic:
```bash
git pull origin main
# Same as: git fetch + git merge
```

I prefer fetch when I want to review changes first, especially in production environments."

---

### **Q2: "Explain git merge vs git rebase"**

**Answer**:
"Both integrate changes from one branch to another, but differently:

**merge** creates a merge commit, preserving full history:
```bash
git checkout main
git merge feature
# Creates merge commit
```
Pros: Safe, preserves history
Cons: Cluttered history with merge commits

**rebase** reapplies commits on top of another branch:
```bash
git checkout feature
git rebase main
# Moves feature commits after main
```
Pros: Clean, linear history
Cons: Rewrites history (dangerous for shared branches)

**Rule**: Use merge for shared branches, rebase for local cleanup."

---

### **Q3: "How do you undo a commit?"**

**Answer**:
"Depends on whether it's pushed and if history can be rewritten:

**Not pushed yet** (local only):
```bash
git reset --soft HEAD~1  # Keep changes
git reset --hard HEAD~1  # Discard changes
```

**Already pushed** (shared with team):
```bash
git revert abc123  # Creates new commit undoing changes
```

**Why revert for pushed commits?** Because reset rewrites history, which breaks others' work. Revert is safe - it creates a new commit that undoes changes without rewriting history."

---

### **Q4: "What is git stash and when to use it?"**

**Answer**:
"git stash temporarily saves uncommitted changes so you can switch branches:

**Scenario**: Working on feature, urgent bug fix needed:
```bash
git stash save "WIP: user dashboard"
git checkout main
git checkout -b hotfix/critical-bug
# Fix bug
git checkout feature-branch
git stash pop
```

**Commands**:
- `git stash` - Save changes
- `git stash list` - See all stashes
- `git stash pop` - Apply and remove
- `git stash apply` - Apply but keep

It's like a clipboard for your changes."

---

### **Q5: "Explain branching strategy in your project"**

**Answer**:
"We use Git Flow branching strategy:

**main** - Production-ready code
**develop** - Integration branch
**feature/** - New features
**hotfix/** - Urgent fixes
**release/** - Release preparation

**Workflow**:
```bash
# New feature
git checkout -b feature/user-login develop
# Work and commit
git checkout develop
git merge feature/user-login

# Hotfix
git checkout -b hotfix/security-patch main
# Fix and commit
git checkout main
git merge hotfix/security-patch
git checkout develop
git merge hotfix/security-patch
```

This keeps main stable, allows parallel development, and provides clear release process."

---

## 📊 GIT COMMAND CHEAT SHEET

```bash
# Setup
git config --global user.name "Your Name"
git config --global user.email "email@example.com"

# Basic
git init                    # Initialize repo
git clone URL               # Clone repo
git status                  # Check status
git add file                # Stage file
git commit -m "msg"         # Commit
git push                    # Push to remote
git pull                    # Pull from remote

# Branching
git branch                  # List branches
git branch name             # Create branch
git checkout name           # Switch branch
git checkout -b name        # Create and switch
git merge name              # Merge branch
git branch -d name          # Delete branch

# History
git log                     # View history
git log --oneline           # Compact view
git diff                    # Show changes
git show abc123             # Show commit

# Undo
git reset HEAD file         # Unstage
git checkout -- file        # Discard changes
git revert abc123           # Undo commit
git reset --hard HEAD~1     # Delete last commit

# Stash
git stash                   # Save changes
git stash pop               # Apply changes
git stash list              # List stashes

# Remote
git remote -v               # List remotes
git remote add origin URL   # Add remote
git fetch                   # Fetch changes
git push origin branch      # Push branch

# Advanced
git rebase main             # Rebase onto main
git cherry-pick abc123      # Apply commit
git tag v1.0.0              # Create tag
```

---

## 💡 BEST PRACTICES FOR INTERVIEWS

### **What Interviewers Want to Hear**
✅ "I use feature branches for isolation"
✅ "I write clear, descriptive commit messages"
✅ "I use git revert for shared branches"
✅ "I pull before pushing to avoid conflicts"
✅ "I use git stash to switch contexts"
✅ "I review changes with git diff before committing"

### **What to Avoid Saying**
❌ "I always force push"
❌ "I commit directly to main"
❌ "I don't use branches"
❌ "I use vague commit messages"
❌ "I never pull before pushing"

---

**Master these commands and you'll ace any Git interview question!** 🚀
