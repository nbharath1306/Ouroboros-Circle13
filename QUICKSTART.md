# 🚀 QUICK START GUIDE
# Project Ouroboros - The Living Software

## ⚡ Super Quick Start (3 Minutes)

### Prerequisites
- Python 3.11+ installed
- Node.js 18+ installed  
- Git installed

### Step 1: Clone/Navigate to Project
```bash
cd /workspaces/Ouroboros-Circle13
```

### Step 2: Run Setup Script
```bash
chmod +x setup.sh
./setup.sh
```

This installs all dependencies for both backend and frontend.

### Step 3: Start Backend
Open Terminal 1:
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python main.py
```

You should see:
```
🧬 PROJECT OUROBOROS - THE LIVING SOFTWARE
🌐 API Server: http://localhost:8000
```

### Step 4: Start Frontend
Open Terminal 2:
```bash
cd frontend
npm run dev
```

You should see:
```
▲ Next.js 14.0.4
- Local: http://localhost:3000
```

### Step 5: Open Dashboard
Visit http://localhost:3000 in your browser

You should see:
- 🟢 Green "CONNECTED" indicator
- Live status updates
- Real-time logs in terminal

### Step 6: Test Chaos Injection
Click any chaos button:
- "💥 SYNTAX ERROR"
- "⚠️ DIVISION BY ZERO"  
- "🗑️ DELETE CODE LINE"
- "🎲 RANDOM CHAOS"

Watch the logs to see the error detection!

---

## 📋 Detailed Setup

### Backend Setup (Manual)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Edit .env (optional for Phase 1)
# Add OPENAI_API_KEY for Phase 2

# Run the server
python main.py
```

The backend API will be available at http://localhost:8000

### Frontend Setup (Manual)

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Create environment file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Run development server
npm run dev
```

The frontend will be available at http://localhost:3000

---

## 🧪 Test the System

Run the test script to verify everything works:

```bash
# Make sure backend is running first!
chmod +x test.sh
./test.sh
```

Expected output:
```
Testing Health Check... ✅ PASS
Testing Status Endpoint... ✅ PASS
Testing Logs Endpoint... ✅ PASS
Testing Chaos Injection... ✅ PASS

🎉 All tests passed!
```

---

## 📡 API Endpoints

Once backend is running, try these:

```bash
# Get status
curl http://localhost:8000/status

# Get logs
curl http://localhost:8000/logs

# Inject chaos
curl -X POST http://localhost:8000/chaos \
  -H "Content-Type: application/json" \
  -d '{"chaos_type":"syntax_error"}'

# API documentation
open http://localhost:8000/docs
```

---

## 🎮 How to Use

### 1. Monitor the Organism
- Watch the **Vital Signs** panel for status
- **Generation** shows how many times code has evolved
- **Status** shows ALIVE, CRASHED, or MUTATING
- **Avg Execution** shows performance

### 2. View Statistics
- **Successful Runs**: Number of successful cycles
- **Crashes**: How many times it crashed
- **Success Rate**: Percentage of successful runs

### 3. Inject Chaos
Click any chaos button to corrupt the organism:
- **Syntax Error**: Adds invalid Python code
- **Division by Zero**: Adds `1/0` to cause crash
- **Delete Line**: Randomly removes code
- **Random**: Surprise me!

### 4. Watch Recovery
In **Phase 1** (current):
- System detects the error
- Logs the crash
- Continues running (without actually fixing yet)

In **Phase 2** (coming soon):
- System detects error
- Calls LLM (OpenAI/Gemini)
- LLM generates fixed code
- System saves new version
- Automatically restarts with fixed code

### 5. Monitor Logs
The **Live Terminal** shows real-time activity:
- 🧬 Blue = Organism output
- ✅ Green = Success
- 💀 Red = Crash/Error
- ⚠️ Yellow = Warning

---

## 🗂️ Project Structure

```
Ouroboros-Circle13/
│
├── backend/              # Python Backend
│   ├── main.py          # ⭐ FastAPI server
│   ├── watcher.py       # ⭐ Immune system  
│   ├── organism.py      # ⭐ Living worker
│   └── requirements.txt # Dependencies
│
├── frontend/            # Next.js Frontend
│   ├── app/
│   │   └── page.tsx    # ⭐ God View dashboard
│   └── package.json    # Dependencies
│
├── README.md           # Main documentation
├── ARCHITECTURE.md     # System diagrams
├── DEPLOYMENT.md       # Deploy to production
├── IMPLEMENTATION.md   # Technical details
├── setup.sh           # Quick setup script
└── test.sh            # Test script
```

---

## 🔧 Troubleshooting

### Backend won't start
```bash
# Check Python version
python3 --version  # Should be 3.11+

# Reinstall dependencies
cd backend
pip install -r requirements.txt --force-reinstall

# Check for port conflicts
lsof -i :8000  # Kill any process using port 8000
```

### Frontend won't start
```bash
# Check Node version
node --version  # Should be 18+

# Clear cache and reinstall
cd frontend
rm -rf node_modules package-lock.json .next
npm install

# Check for port conflicts
lsof -i :3000  # Kill any process using port 3000
```

### Frontend can't connect to backend
1. Make sure backend is running (check Terminal 1)
2. Check `.env.local` has correct URL:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```
3. Test backend directly:
   ```bash
   curl http://localhost:8000/status
   ```
4. Check browser console for CORS errors

### Chaos injection not working
1. Check backend logs in Terminal 1
2. Verify organism.py exists in backend/
3. Try different chaos types
4. Check file permissions

---

## 🎯 What to Expect

### Normal Operation
```
[12:34:56.123] 🔄 CYCLE START - Generation 1
[12:34:56.150] 🧬 Organism Generation 1 - ALIVE
[12:34:56.151] 🧬 Processing data: [45, 23, 67, ...]
[12:34:56.653] 🧬 ✅ Sorted: [12, 23, 34, ...]
[12:34:56.655] ✅ Cycle complete in 0.502s
```

### After Chaos Injection
```
[12:35:10.123] ☢️ CHAOS INJECTED: syntax_error
[12:35:10.124] 💥 Injected syntax error
[12:35:13.234] 🔄 CYCLE START - Generation 2
[12:35:13.456] 💀 CRASH DETECTED (Exit code: 1)
[12:35:13.457] 🧬 MUTATION TRIGGERED
[12:35:13.458] 🤖 [PLACEHOLDER] AI will analyze...
[12:35:15.678] ✅ Mutation complete (placeholder)
```

---

## 📚 Next Steps

### Learn More
- Read [README.md](README.md) for full overview
- Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design
- Read [DEPLOYMENT.md](DEPLOYMENT.md) to deploy to production
- Read [IMPLEMENTATION.md](IMPLEMENTATION.md) for technical details

### Extend the System
- Add OpenAI API key for real LLM mutations (Phase 2)
- Deploy to Railway + Vercel (see DEPLOYMENT.md)
- Customize organism.py to do different tasks
- Modify the dashboard styling
- Add more chaos types

### Deploy to Production
1. Push code to GitHub
2. Deploy backend to Railway (see DEPLOYMENT.md)
3. Deploy frontend to Vercel (see DEPLOYMENT.md)
4. Share with the world! 🌍

---

## 🎓 Understanding the System

### The Organism (organism.py)
- A simple Python script that does work
- Intentionally uses slow bubble sort
- Can be corrupted and (eventually) healed
- Prints status updates

### The Watcher (watcher.py)
- Runs organism.py as a subprocess
- Monitors for crashes and performance
- Captures all output and errors
- Triggers mutations when needed
- Runs in background thread

### The API (main.py)
- FastAPI server exposing organism state
- CORS enabled for frontend
- Real-time status endpoints
- Chaos injection endpoint

### The God View (page.tsx)
- React dashboard for monitoring
- Polls API every 1 second
- Displays vital signs and logs
- Controls for chaos injection
- Cyberpunk aesthetic

---

## 💡 Tips

1. **Keep both terminals visible** so you can see backend logs and frontend
2. **Watch the generation number** increment after chaos injection
3. **Try different chaos types** to see different errors
4. **Check the Live Terminal** for detailed activity
5. **Monitor success rate** as you inject chaos

---

## 🎉 You're Ready!

You now have a working self-healing software system!

- ✅ Backend running on http://localhost:8000
- ✅ Frontend running on http://localhost:3000
- ✅ Real-time monitoring active
- ✅ Chaos injection working
- ✅ Ready for Phase 2 (LLM integration)

**Enjoy watching your living software evolve!** 🧬

---

## 🆘 Need Help?

1. Check the logs (backend terminal)
2. Run `./test.sh` to diagnose issues
3. Review the troubleshooting section above
4. Read the full documentation in README.md
5. Check environment variables are set correctly

**Status**: Phase 1 Complete ✅  
**Next**: Add your OpenAI API key for true self-healing! 🤖
