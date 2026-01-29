# 🚀 DEPLOYMENT GUIDE - Project Ouroboros

## Prerequisites

- GitHub account
- Railway account (railway.app) OR Render account (render.com)
- Vercel account (vercel.com)
- OpenAI API key (for Phase 2 LLM features)

---

## Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Project Ouroboros Phase 1"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ouroboros.git
git push -u origin main
```

---

## Step 2: Deploy Backend to Railway

### Option A: Railway (Recommended)

1. **Go to Railway**: https://railway.app
2. **New Project** → **Deploy from GitHub repo**
3. **Select your repository**
4. **Configure:**
   - Root Directory: `/backend`
   - Builder: Nixpacks (auto-detected)
5. **Add Environment Variables:**
   ```
   OPENAI_API_KEY=sk-your-key-here
   TARGET_LATENCY=1.0
   PORT=8000
   ```
6. **Deploy** (Railway will auto-deploy)
7. **Get your URL**: Should be like `https://your-app.railway.app`
8. **Test it**: Visit `https://your-app.railway.app/status`

### Option B: Render

1. **Go to Render**: https://render.com
2. **New** → **Web Service**
3. **Connect GitHub repository**
4. **Configure:**
   - Name: `ouroboros-backend`
   - Root Directory: `backend`
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Add Environment Variables:**
   ```
   OPENAI_API_KEY=sk-your-key-here
   TARGET_LATENCY=1.0
   ```
6. **Create Web Service**
7. **Get your URL**: Should be like `https://ouroboros-backend.onrender.com`

---

## Step 3: Deploy Frontend to Vercel

1. **Go to Vercel**: https://vercel.com
2. **Import Project** → **Import Git Repository**
3. **Select your repository**
4. **Configure:**
   - Framework Preset: Next.js
   - Root Directory: `frontend`
   - Build Command: `npm run build` (auto-detected)
   - Output Directory: `.next` (auto-detected)
5. **Add Environment Variable:**
   ```
   NEXT_PUBLIC_API_URL=https://your-railway-app.railway.app
   ```
   (Use the URL from Step 2)
6. **Deploy**
7. **Get your URL**: Should be like `https://your-app.vercel.app`

---

## Step 4: Test the Full Stack

1. **Visit your Vercel URL**: `https://your-app.vercel.app`
2. You should see the **God View Dashboard**
3. Check if the connection indicator is **GREEN**
4. Try clicking **"Inject Chaos"** buttons
5. Watch the **Live Terminal** for real-time logs

---

## Troubleshooting

### Backend not responding
- Check Railway/Render logs
- Verify environment variables are set
- Make sure PORT is set correctly

### Frontend can't connect to backend
- Check `NEXT_PUBLIC_API_URL` in Vercel settings
- Verify CORS is enabled in backend (it should be by default)
- Check browser console for errors

### "Module not found" errors
- Make sure all dependencies are in `requirements.txt` (backend)
- Make sure all dependencies are in `package.json` (frontend)
- Redeploy after adding dependencies

---

## Local Development

### Run Backend Locally
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your keys
python main.py
```

### Run Frontend Locally
```bash
cd frontend
npm install
npm run dev
```

Make sure backend is running on `http://localhost:8000` before starting frontend.

---

## Update Deployment

### Update Backend
```bash
git add backend/
git commit -m "Update backend"
git push
```
Railway/Render will auto-deploy.

### Update Frontend
```bash
git add frontend/
git commit -m "Update frontend"
git push
```
Vercel will auto-deploy.

---

## Environment Variables Reference

### Backend
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| OPENAI_API_KEY | OpenAI API key for LLM mutations | Phase 2 | - |
| TARGET_LATENCY | Target execution time in seconds | No | 1.0 |
| PORT | Server port | No | 8000 |

### Frontend
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| NEXT_PUBLIC_API_URL | Backend API URL | Yes | http://localhost:8000 |

---

## Custom Domain (Optional)

### Vercel (Frontend)
1. Go to project settings in Vercel
2. Domains → Add Domain
3. Follow DNS instructions

### Railway (Backend)
1. Go to project settings in Railway
2. Domains → Add Custom Domain
3. Follow DNS instructions

---

## Monitoring

### Railway
- View logs in Railway dashboard
- Monitor CPU/Memory usage
- Set up alerts

### Vercel
- View Analytics in Vercel dashboard
- Monitor function invocations
- Check deployment logs

---

## Cost Estimates

- **Railway**: Free tier includes 500 hours/month, $5/month after
- **Render**: Free tier available (may sleep after inactivity)
- **Vercel**: Free tier is generous for hobby projects
- **OpenAI API**: Pay-per-use (Phase 2)

---

## Security Notes

⚠️ **Important:**
- Never commit `.env` files
- Use environment variables for all secrets
- Restrict CORS in production to your frontend domain
- Add rate limiting for chaos endpoints (Phase 2)

---

## Next Steps (Phase 2)

1. Add OpenAI integration for real code mutations
2. Implement code diff viewer
3. Add genome history and rollback
4. Switch from polling to WebSockets
5. Add authentication for chaos endpoints
6. Implement performance charts

---

**Need Help?**
- Check the logs in Railway/Vercel dashboard
- Review the README.md for architecture details
- Test endpoints with curl or Postman
- Use browser DevTools to debug frontend

---

**Congratulations!** 🎉
Your living software is now deployed and running on the internet!
