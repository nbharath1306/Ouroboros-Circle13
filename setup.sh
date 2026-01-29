#!/bin/bash

# Quick Start Script for Project Ouroboros
# This script helps you get the project running locally

echo "🧬 PROJECT OUROBOROS - QUICK START"
echo "=================================="
echo ""

# Check if we're in the right directory
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python
if ! command_exists python3; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

# Check Node
if ! command_exists node; then
    echo "❌ Node.js is required but not installed"
    exit 1
fi

echo "✅ Python $(python3 --version) found"
echo "✅ Node $(node --version) found"
echo ""

# Setup Backend
echo "📦 Setting up Backend..."
cd backend

if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit backend/.env and add your OPENAI_API_KEY (for Phase 2)"
fi

if [ ! -d "venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "📥 Installing Python dependencies..."
source venv/bin/activate
pip install -q -r requirements.txt

echo "✅ Backend setup complete!"
echo ""

# Setup Frontend
echo "📦 Setting up Frontend..."
cd ../frontend

if [ ! -f ".env.local" ]; then
    echo "📝 Creating .env.local file..."
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
fi

if [ ! -d "node_modules" ]; then
    echo "📥 Installing Node dependencies (this may take a minute)..."
    npm install --silent
else
    echo "✅ Node modules already installed"
fi

echo "✅ Frontend setup complete!"
echo ""

cd ..

# Create run scripts
echo "📝 Creating run scripts..."

# Backend run script
cat > run-backend.sh << 'EOF'
#!/bin/bash
cd backend
source venv/bin/activate
python main.py
EOF
chmod +x run-backend.sh

# Frontend run script
cat > run-frontend.sh << 'EOF'
#!/bin/bash
cd frontend
npm run dev
EOF
chmod +x run-frontend.sh

echo "✅ Run scripts created!"
echo ""
echo "=================================="
echo "🎉 SETUP COMPLETE!"
echo "=================================="
echo ""
echo "To start the project:"
echo ""
echo "1️⃣  Terminal 1 - Backend:"
echo "   ./run-backend.sh"
echo "   or manually:"
echo "   cd backend && source venv/bin/activate && python main.py"
echo ""
echo "2️⃣  Terminal 2 - Frontend:"
echo "   ./run-frontend.sh"
echo "   or manually:"
echo "   cd frontend && npm run dev"
echo ""
echo "Then open: http://localhost:3000"
echo ""
echo "📚 Read README.md for full documentation"
echo "🚀 Read DEPLOYMENT.md for deployment instructions"
echo ""
