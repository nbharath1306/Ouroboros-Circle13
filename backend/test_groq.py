#!/usr/bin/env python3
"""Quick test script to verify Groq integration"""

import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from architect import get_architect
    print("✅ Groq SDK imported successfully")
    
    architect = get_architect()
    print(f"✅ Architect initialized with model: {architect.model}")
    print(f"✅ API key configured: {architect.api_key[:10]}...")
    
    print("\n🧬 Phase 2 is READY! The organism can now self-heal with AI!")
    print("🚀 Run: python main.py")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    sys.exit(1)
