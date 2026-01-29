"""
watcher.py - The Immune System
Monitors organism.py and triggers mutations when errors occur.
"""
import subprocess
import sys
import time
import os
import shutil
from datetime import datetime
from typing import Dict, List
import threading

from architect import get_architect


class OrganismWatcher:
    """The Immune System that watches and heals the Organism"""
    
    def __init__(self):
        self.generation = 1
        self.status = "INITIALIZING"
        self.last_mutation = "None"
        self.logs: List[str] = []
        self.max_logs = 100
        self.execution_times: List[float] = []
        self.target_latency = float(os.getenv("TARGET_LATENCY", "1.0"))
        self.crash_count = 0
        self.successful_runs = 0
        self.is_running = False
        self.last_error = None
        self.genome_history: List[Dict] = []  # Track code versions
        self.architect = None  # Lazy load to avoid startup errors
        
    def log(self, message: str):
        """Add a log entry with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        self.logs.append(log_entry)
        if len(self.logs) > self.max_logs:
            self.logs.pop(0)
    
    def run_organism(self) -> Dict:
        """Execute organism.py as a subprocess"""
        start_time = time.time()
        
        try:
            result = subprocess.run(
                [sys.executable, "organism.py"],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=os.path.dirname(os.path.abspath(__file__))
            )
            
            execution_time = time.time() - start_time
            self.execution_times.append(execution_time)
            
            # Keep only last 10 execution times
            if len(self.execution_times) > 10:
                self.execution_times.pop(0)
            
            # Log the output
            if result.stdout:
                for line in result.stdout.strip().split('\n'):
                    self.log(f"🧬 {line}")
            
            if result.returncode == 0:
                self.status = "ALIVE"
                self.successful_runs += 1
                self.log(f"✅ Cycle complete in {execution_time:.3f}s")
                
                # Check if optimization is needed
                if execution_time > self.target_latency:
                    self.log(f"⚠️  Slow execution detected: {execution_time:.3f}s > {self.target_latency}s")
                    if len(self.execution_times) >= 5 and all(t > self.target_latency for t in self.execution_times[-5:]):
                        self.log("🧬 Triggering optimization mutation...")
                        self.mutate_code("OPTIMIZATION_NEEDED", result.stdout)
                
                return {
                    "success": True,
                    "execution_time": execution_time,
                    "output": result.stdout
                }
            else:
                # Organism crashed
                self.status = "CRASHED"
                self.crash_count += 1
                self.last_error = result.stderr
                self.log(f"💀 CRASH DETECTED (Exit code: {result.returncode})")
                self.log(f"📋 Error: {result.stderr}")
                
                # Trigger mutation
                self.mutate_code(result.stderr, result.stdout)
                
                return {
                    "success": False,
                    "error": result.stderr,
                    "execution_time": execution_time
                }
                
        except subprocess.TimeoutExpired:
            self.status = "TIMEOUT"
            self.log("⏱️  TIMEOUT - Organism frozen")
            self.mutate_code("TIMEOUT_ERROR", "Process exceeded 10 second limit")
            return {"success": False, "error": "Timeout"}
        
        except Exception as e:
            self.status = "ERROR"
            self.log(f"🚨 Watcher Error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def mutate_code(self, error_log: str, output: str = ""):
        """
        Use AI to mutate the code and fix errors.
        Now with REAL Groq LLM integration!
        """
        self.status = "MUTATING"
        
        self.log("=" * 60)
        self.log("🧬 MUTATION TRIGGERED")
        self.log("=" * 60)
        self.log(f"📊 Error Context: {error_log[:200]}")
        
        try:
            # Initialize architect if needed
            if self.architect is None:
                self.log("🤖 Initializing AI Brain (Groq)...")
                self.architect = get_architect()
            
            # Read current code
            with open("organism.py", "r") as f:
                current_code = f.read()
            
            # Save current version to genome history
            self._save_genome_version(current_code, error_log)
            
            # Determine mutation type
            mutation_type = "OPTIMIZATION" if "OPTIMIZATION_NEEDED" in error_log else "ERROR"
            
            self.log(f"🧠 Calling Groq AI ({self.architect.model})...")
            self.log(f"🎯 Mutation Type: {mutation_type}")
            
            # Get AI-generated fix
            fixed_code, explanation = self.architect.analyze_and_fix(
                error_log, 
                current_code, 
                mutation_type
            )
            
            # Validate the fixed code
            if not self._validate_code(fixed_code):
                self.log("❌ AI generated invalid code, reverting...")
                self.status = "ALIVE"
                return
            
            # Save the fixed code
            self.generation += 1
            backup_path = f"organism_v{self.generation}.py"
            
            # Backup current version
            shutil.copy("organism.py", backup_path)
            
            # Write fixed code
            with open("organism.py", "w") as f:
                f.write(fixed_code)
            
            self.last_mutation = explanation
            
            self.log("✅ AI mutation successful!")
            self.log(f"💾 Saved as: {backup_path}")
            self.log(f"🧬 Generation: {self.generation}")
            self.log(f"📝 Changes: {explanation}")
            self.log("=" * 60)
            
        except Exception as e:
            self.log(f"❌ Mutation failed: {str(e)}")
            self.log("🔄 Continuing with current code...")
            self.status = "ALIVE"
    
    def _validate_code(self, code: str) -> bool:
        """Validate that the code is syntactically correct"""
        try:
            compile(code, '<string>', 'exec')
            return True
        except SyntaxError as e:
            self.log(f"⚠️ Validation failed: {str(e)}")
            return False
    
    def _save_genome_version(self, code: str, context: str):
        """Save code version to genome history"""
        self.genome_history.append({
            "generation": self.generation,
            "timestamp": datetime.now().isoformat(),
            "code": code,
            "context": context[:200]
        })
        
        # Keep only last 10 versions
        if len(self.genome_history) > 10:
            self.genome_history.pop(0)
    
    def inject_chaos(self, chaos_type: str = "random"):
        """Simulate an error by corrupting organism.py"""
        self.log(f"☢️  CHAOS INJECTED: {chaos_type}")
        
        try:
            with open("organism.py", "r") as f:
                lines = f.readlines()
            
            if chaos_type == "delete_line":
                # Delete a random line
                import random
                if len(lines) > 10:
                    idx = random.randint(5, len(lines) - 5)
                    deleted = lines.pop(idx)
                    self.log(f"🗑️  Deleted line {idx}: {deleted.strip()}")
            
            elif chaos_type == "syntax_error":
                # Add a syntax error
                lines.insert(10, "this is not valid python!!!\n")
                self.log("💥 Injected syntax error")
            
            elif chaos_type == "division_by_zero":
                # Add division by zero
                lines.insert(15, "    result = 1 / 0  # Chaos!\n")
                self.log("💥 Injected division by zero")
            
            with open("organism.py", "w") as f:
                f.writelines(lines)
            
            self.log("☢️  Organism corrupted successfully")
            
        except Exception as e:
            self.log(f"❌ Chaos injection failed: {str(e)}")
    
    def start_watch_loop(self):
        """Main watch loop (runs in background thread)"""
        self.is_running = True
        self.log("👁️  Watcher initialized")
        self.log(f"🎯 Target latency: {self.target_latency}s")
        
        while self.is_running:
            self.log("\n" + "=" * 60)
            self.log(f"🔄 CYCLE START - Generation {self.generation}")
            self.log("=" * 60)
            
            result = self.run_organism()
            
            # Wait before next cycle
            time.sleep(3)
    
    def stop(self):
        """Stop the watch loop"""
        self.is_running = False
        self.log("🛑 Watcher stopped")
    
    def get_status(self) -> Dict:
        """Get current status for API"""
        avg_execution_time = sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0
        
        return {
            "generation": self.generation,
            "status": self.status,
            "last_mutation": self.last_mutation,
            "crash_count": self.crash_count,
            "successful_runs": self.successful_runs,
            "avg_execution_time": round(avg_execution_time, 3),
            "recent_execution_times": [round(t, 3) for t in self.execution_times[-5:]],
            "uptime": len(self.logs),
            "last_error": self.last_error
        }
    
    def get_logs(self, limit: int = 50) -> List[str]:
        """Get recent logs"""
        return self.logs[-limit:]


# Global watcher instance
watcher = OrganismWatcher()


def start_watcher():
    """Start the watcher in a background thread"""
    thread = threading.Thread(target=watcher.start_watch_loop, daemon=True)
    thread.start()
    return watcher


if __name__ == "__main__":
    # Test the watcher standalone
    print("🧬 Project Ouroboros - Watcher Test Mode")
    print("=" * 60)
    
    try:
        watcher.start_watch_loop()
    except KeyboardInterrupt:
        watcher.stop()
        print("\n👋 Watcher stopped by user")
