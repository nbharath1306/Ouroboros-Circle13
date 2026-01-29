# 🧬 Project Ouroboros - Self-Healing Repository

**A GitHub repository that heals itself using AI.**

## 🌟 The Concept

This repository contains code that **automatically detects and fixes its own bugs** using GitHub Actions and Groq AI. No external hosting required - everything happens in GitHub!

### How It Works

```
1. GitHub Actions runs main.py every 30 minutes
         ↓
2. If it crashes → Captures error to error.log
         ↓
3. Triggers healer.py (AI Doctor)
         ↓
4. Groq AI analyzes the error + code
         ↓
5. Generates fixed code
         ↓
6. Commits the fix back to the repo
         ↓
7. Next run uses the healed code ✅
```

## 🏗️ Architecture

### The Organism (`main.py`)
- A simple Fibonacci calculator
- **Contains an intentional bug** (ValueError for input > 10)
- Will crash on first run

### The AI Doctor (`healer.py`)
- Reads the broken code and error log
- Calls Groq AI (llama-3.3-70b-versatile)
- Generates fixed code
- Overwrites `main.py` with the healed version

### The Evolution Workflow (`.github/workflows/evolve.yml`)
- **Triggers:**
  - Manual button (workflow_dispatch)
  - Automatic every 30 minutes (cron schedule)
- **Process:**
  1. Runs `main.py`
  2. If it fails → Runs `healer.py`
  3. Commits the fixed code automatically
- **Permissions:** Write access to commit changes

## 🚀 Setup

### 1. Add Groq API Key to GitHub Secrets

1. Go to your repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `GROQ_API_KEY`
4. Value: Your Groq API key (get it from https://console.groq.com)
5. Click **Add secret**

### 2. Enable GitHub Actions

1. Go to your repo → **Actions** tab
2. If prompted, click **"I understand my workflows, go ahead and enable them"**

### 3. Run the First Evolution

1. Go to **Actions** → **🧬 Self-Healing Evolution**
2. Click **Run workflow** → **Run workflow**
3. Watch the magic happen! ✨

## 📊 What You'll See

### First Run (The Bug):
```
💀 Organism crashed!
ValueError: Input too large! This organism is weak and will crash.
```

### AI Doctor Activates:
```
🏥 AI Doctor activated...
🧬 Analyzing error and generating fix...
✅ Code healed successfully!
```

### Auto-Commit:
```
🧬 Auto-Evolution: Fixed Bug (Generation 1)
```

### Second Run:
```
✅ Organism is healthy and functioning!
Calculation successful
```

## 🎮 Features

✅ **Fully GitHub-Native**
- No Vercel, no Render, no external hosting
- Everything runs in GitHub Actions
- Free for public repos!

✅ **Automatic Self-Healing**
- Detects crashes automatically
- Uses Groq AI to fix bugs
- Commits fixes to the repo

✅ **Multiple Triggers**
- Manual button for testing
- Automatic every 30 minutes
- Can customize schedule

✅ **Evolution Tracking**
- Each fix is a new "generation"
- Full Git history of all mutations
- See how the code evolved over time

## 🧪 Testing Locally

```bash
# Test the organism (will crash)
python main.py 2> error.log

# Run the healer
export GROQ_API_KEY=your_key_here
python healer.py

# Check the fixed code
cat main.py
```

## 📁 File Structure

```
Ouroboros-Circle13/
├── main.py                    # The Organism (has bug)
├── healer.py                  # The AI Doctor
├── requirements.txt           # Python dependencies
├── .github/
│   └── workflows/
│       └── evolve.yml         # Self-healing workflow
└── README.md
```

## 🔧 Customization

### Change the Schedule

Edit `.github/workflows/evolve.yml`:
```yaml
schedule:
  - cron: '*/30 * * * *'  # Every 30 minutes
  # Examples:
  # - cron: '0 * * * *'   # Every hour
  # - cron: '0 0 * * *'   # Every day at midnight
  # - cron: '*/5 * * * *' # Every 5 minutes
```

### Add More Test Cases

Edit `main.py` to add different types of bugs:
```python
# Add more intentional bugs for the AI to fix
if n > 10:
    raise ValueError("Bug 1")
if n < 0:
    return 1/0  # Bug 2: Division by zero
```

### Use Different AI Models

Edit `healer.py`:
```python
model="llama-3.3-70b-versatile"  # Current
# Try: "mixtral-8x7b-32768" or "llama3-70b-8192"
```

## 📊 Monitoring Evolution

### View Workflow Runs
1. Go to **Actions** tab
2. See all evolution cycles
3. Click any run to see details

### Check Evolution History
```bash
# See all auto-commits
git log --grep="Auto-Evolution"

# Compare generations
git diff HEAD~1 main.py
```

### Watch the Summary
Each workflow run generates a summary:
- ✅ Status (Healthy/Healed)
- 🧬 Generation number
- ⏰ Timestamp

## 🎯 Use Cases

### 1. Self-Healing Production Code
- Deploy code with known edge case bugs
- Let AI fix them automatically
- Review and merge the fixes

### 2. Code Evolution Experiments
- Start with intentionally bad code
- Watch it improve over time
- Study the AI's fixing patterns

### 3. Continuous Optimization
- AI not only fixes bugs but optimizes code
- Performance improvements over time
- Automatic refactoring

### 4. Educational Tool
- Learn about AI-assisted debugging
- See real-world error fixing
- Understand evolutionary programming

## 🔒 Security Notes

- ✅ GROQ_API_KEY stored in GitHub Secrets (encrypted)
- ✅ Workflow only has write access to contents
- ✅ All changes tracked in Git history
- ⚠️ Review AI-generated code before production use

## 📈 Advantages Over Traditional Deployment

| Feature | Traditional | Ouroboros |
|---------|------------|-----------|
| Hosting | Vercel/Railway | GitHub (Free) |
| Self-Healing | Manual | Automatic |
| Evolution History | Separate logs | Git commits |
| Cost | $5-20/month | $0 |
| Setup Complexity | Multiple services | Single repo |

## 🎓 What You Learn

- GitHub Actions workflows
- AI-powered code generation
- Error handling and recovery
- Automated testing and fixing
- Git automation
- Cron scheduling

## 🚀 Next Steps

1. **Add More Organisms**: Create multiple Python files that heal each other
2. **Add Tests**: Include pytest to verify fixes work
3. **Multi-Language**: Extend to JavaScript, Go, etc.
4. **Slack Notifications**: Alert when evolution occurs
5. **Rollback System**: Automatically revert bad fixes

## 💡 Pro Tips

1. **Watch the first run live** - It's fascinating to see the AI fix in real-time
2. **Check the diff** - See exactly what the AI changed
3. **Add more bugs** - Test different error types
4. **Customize the prompt** - Make the AI more creative or conservative

## 🏆 Achievement: Self-Healing Repository

You've created a repository that:
- Monitors itself continuously
- Detects its own failures
- Fixes itself using AI
- Commits improvements automatically
- Evolves over time

**This is truly living code in a GitHub repository!** 🧬

---

## 📚 Learn More

- [Groq API Documentation](https://console.groq.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Cron Schedule Syntax](https://crontab.guru/)

---

**Status**: Self-Healing Active 🧬  
**Platform**: GitHub Actions  
**AI Model**: llama-3.3-70b-versatile  
**Cost**: FREE ✅
