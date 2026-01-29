"""
main.py - FastAPI Entry Point
The API that exposes the Organism's internal state to the God View.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
from dotenv import load_dotenv

from watcher import start_watcher, watcher

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="Project Ouroboros API",
    description="The Living Software - Backend API",
    version="1.0.0"
)

# Enable CORS for Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "https://*.vercel.app",
        "*"  # In production, replace with specific domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class ChaosRequest(BaseModel):
    chaos_type: Optional[str] = "random"


class StatusResponse(BaseModel):
    generation: int
    status: str
    last_mutation: str
    crash_count: int
    successful_runs: int
    avg_execution_time: float
    recent_execution_times: List[float]
    uptime: int
    last_error: Optional[str]


class LogsResponse(BaseModel):
    logs: List[str]
    count: int


class ChaosResponse(BaseModel):
    message: str
    chaos_type: str


class GenomeVersion(BaseModel):
    generation: int
    timestamp: str
    context: str


class GenomeHistoryResponse(BaseModel):
    versions: List[GenomeVersion]
    count: int


@app.on_event("startup")
async def startup_event():
    """Start the watcher when the API starts"""
    print("🚀 Starting Project Ouroboros...")
    print("=" * 60)
    start_watcher()
    print("✅ Watcher thread started")
    print("🌐 API ready to serve")
    print("=" * 60)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "project": "Ouroboros",
        "status": "alive",
        "message": "The Living Software is running",
        "endpoints": {
            "status": "/status",
            "logs": "/logs",
            "chaos": "/chaos"
        }
    }


@app.get("/status", response_model=StatusResponse)
async def get_status():
    """
    Get the current status of the organism.
    
    Returns:
        - generation: Current generation number
        - status: ALIVE, CRASHED, MUTATING, etc.
        - last_mutation: Description of last mutation
        - crash_count: Total number of crashes
        - successful_runs: Total successful cycles
        - avg_execution_time: Average execution time
        - recent_execution_times: Last 5 execution times
        - uptime: Number of log entries (proxy for uptime)
        - last_error: Last error message if any
    """
    try:
        status = watcher.get_status()
        return StatusResponse(**status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/logs", response_model=LogsResponse)
async def get_logs(limit: int = 50):
    """
    Get recent execution logs.
    
    Args:
        limit: Number of log entries to return (default: 50)
    
    Returns:
        - logs: List of log entries
        - count: Number of log entries returned
    """
    try:
        logs = watcher.get_logs(limit)
        return LogsResponse(logs=logs, count=len(logs))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chaos", response_model=ChaosResponse)
async def inject_chaos(request: ChaosRequest):
    """
    Inject chaos into the organism (Chaos Monkey).
    
    Supported chaos types:
        - delete_line: Delete a random line of code
        - syntax_error: Inject a syntax error
        - division_by_zero: Add division by zero
        - random: Random chaos (default)
    
    Args:
        chaos_type: Type of chaos to inject
    
    Returns:
        - message: Confirmation message
        - chaos_type: Type of chaos injected
    """
    try:
        chaos_type = request.chaos_type or "random"
        
        # Map random to a specific chaos type
        if chaos_type == "random":
            import random
            chaos_type = random.choice(["delete_line", "syntax_error", "division_by_zero"])
        
        watcher.inject_chaos(chaos_type)
        
        return ChaosResponse(
            message=f"Chaos injected successfully",
            chaos_type=chaos_type
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Kubernetes/Railway health check endpoint"""
    return {"status": "healthy"}


@app.get("/genome", response_model=GenomeHistoryResponse)
async def get_genome_history():
    """
    Get the genome history (previous code versions).
    
    Returns:
        - versions: List of previous code versions
        - count: Number of versions in history
    """
    try:
        history = watcher.genome_history
        versions = [
            GenomeVersion(
                generation=v["generation"],
                timestamp=v["timestamp"],
                context=v["context"]
            )
            for v in history
        ]
        return GenomeHistoryResponse(versions=versions, count=len(versions))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    
    print("=" * 60)
    print("🧬 PROJECT OUROBOROS - THE LIVING SOFTWARE")
    print("=" * 60)
    print(f"🌐 API Server: http://localhost:{port}")
    print(f"📚 Docs: http://localhost:{port}/docs")
    print(f"🔍 Status: http://localhost:{port}/status")
    print("=" * 60)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )
