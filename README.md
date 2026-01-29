# 🧬 Project Ouroboros - The Living Software

**An autonomous self-healing software system that monitors its own health and rewrites its own code in real-time.**

## 🌟 Overview

Project Ouroboros is a biological software organism that:
- ✅ Monitors itself for crashes and performance issues
- ✅ **Uses AI (Groq LLM) to fix its own bugs automatically**
- ✅ **Optimizes itself when running slow**
- ✅ Provides a real-time "God View" dashboard
- ✅ Survives chaos injection attacks
- ✅ **Tracks genome history with code versioning**

## 🏗️ Architecture

### Backend (The Organism) - Python
- **organism.py**: The worker that performs tasks
- **watcher.py**: The immune system that monitors organism.py
- **architect.py**: The brain that uses Groq AI to fix code
- **main.py**: FastAPI server exposing the organism's state
- **Hosting**: Railway/Render (requires writable filesystem)

### Frontend (God View) - Next.js 14
- Real-time status dashboard
- Live terminal logs
- Chaos injection controls
- Vital signs visualization
- **Hosting**: Vercel

## 🚀 Quick Start

### Backend

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your GROQ_API_KEY (get free key from console.groq.com)
python main.py
```

Backend runs on `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:3000`

## 📡 API Endpoints

- `GET /status` - Organism vital signs
- `GET /logs` - Recent execution logs
- `POST /chaos` - Inject chaos (simulate errors)
- `GET /genome` - Genome history (code versions)
- `GET /health` - Health check for deployment platforms


✅ **Backend Core (Phase 1)**
- Subprocess-based organism execution
- Error detection and logging
- Performance monitoring
- Chaos injection system
- FastAPI REST API with CORS

✅ **AI Self-Healing (Phase 2)** 🤖
- **Groq LLM integration** for code mutations
- **Automatic error fixing** - AI rewrites broken code
- **Performance optimization** - AI improves slow algorithms
- **Code validation** - Syntax checking before deployment
- **Genome history tracking** - Version control for mutations
- FastAPI REST API with CORS

✅ **FrFuture Enhancements

- [ ] 📝 Code diff viewer showing AI changes in real-time
- [ ] 🔌 WebSocket support for instant updates (replace polling)
- [ ] 📈 Advanced performance charts with Recharts
- [ ] 🎯 Fitness scoring system for mutations
- [ ] 🧪 A/B testing between code versions
- [ ] 🔐 Authentication for chaos endpoints
- [ ] 📊 Mutation success rate analytics
## 🔮 Coming in Phase 2

- 🤖 LLM integration (OpenAI/Gemini) for automatic code mutations
- 📝 Code diff viewer showing AI changes
- 💾 Genome history with rollback capability
- 🔌 WebSocket support for instant updates
- 📈 Advanced performance charts (Recharts)

## 🌐 Deployment

### Deploy Backend to Railway

1. Create new project on Railway
2. Connect your GitHub repo
3. Set root directory to `/backend`
4. Add environment variable: `OPENAI_API_KEY`
5. Railway will auto-detect Python and deploy

### Deploy Frontend to Vercel

1. Push code to GitHub
2. Import project in Vercel
3. Set root directory to `/frontend`
4. Add environment variable: `NEXT_PUBLIC_API_URL` (your Railway URL)
5. Deploy

## 🧪 Testing

### Test the Backend
```bash
cd backend
python organism.py  # Test organism directly
python watcher.py   # Test watcher standalone
python main.py      # Start API server
```

### Test the API
```bash
curl http://localhost:8000/status
curl http://localhost:8000/logs
curl -X POST http://localhost:8000/chaos -H "Content-Type: application/json" -d '{"chaos_type":"syntax_error"}'
```

## 📁 Project Structure

```
Ouroboros-Circle13/
├── backend/
│   ├── main.py           # FastAPI entry point
│   ├── watcher.py        # The immune system
│   ├── organism.py       # The living worker
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── app/
│   │   ├── page.tsx      # God View dashboard
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── package.json
│   └── tailwind.config.js
└── README.md
```

## 🎨 The God View Dashboard

Features:
- **Vital Signs Panel**: Status, generation, execution time
- **Statistics Panel**: Success rate, crash count, uptime
- **Chaos Controls**: Inject errors to test self-healing
- **Live Terminal**: Real-time log streaming
- **Mutation History**: Last mutation events
- **Connection Status**: Live backend connectivity indicator

## 💡 How It Works

1. **Watcher calls Groq AI** → "Fix this error"
4. **AI analyzes and generates fixed code** (llama-3.3-70b-versatile)
5. **Watcher validates the fix** → Syntax check
6. **Watcher saves new version** → `organism_v{N+1}.py`
7. **Watcher restarts with new code** → Organism lives!
8. LLM returns fixed code → Watcher saves as `organism_v{N+1}.py`
5. Watcher restarts with new code → Organism lives!
6. Frontend polls `/status` every 1 second to display state

## 🛡️ Chaos Engineering

Test the self-healing system:
- **Syntax Error**: Inject invalid Python syntax
- **Division by Zero**: Add `1/0` to cause runtime error
- **Delete Line**: Randomly remove code
- **Random**: Surprise me!

GROQ_API_KEY=gsk_...  # Get free key from console.groq.com

### Backend (.env)
```
OPENAI_API_KEY=sk-...
TARGET_LATENCY=1.0
PORT=8000
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 📚 Tech Stack

**Backend:**
- Python 3.11
- **Groq SDK** (llama-3.3-70b-versatile
- Uvicorn
- OpenAI SDK (Phase 2)

**Frontend:**
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Lucide Icons

## 🤝 Contributing

This is a demonstration project for agentic IDEs. Feel free to extend it!

## 📄 License

MIT

## 🙏 Acknowledgments

Built as a proof-of-concept for autonomous software systems.

---

**Status**: Phase 2 Complete ✅  
**AI Integration**: Groq LLM (llama-3.3-70b-versatile) 🤖  
**Self-Healing**: ACTIVE 🧬
