'use client'

import { useState, useEffect } from 'react'
import { Activity, AlertCircle, Zap, TrendingUp, Terminal, Skull, Siren } from 'lucide-react'

interface OrganismStatus {
  generation: number
  status: string
  last_mutation: string
  crash_count: number
  successful_runs: number
  avg_execution_time: number
  recent_execution_times: number[]
  uptime: number
  last_error: string | null
}

interface LogEntry {
  logs: string[]
  count: number
}

export default function GodView() {
  const [status, setStatus] = useState<OrganismStatus | null>(null)
  const [logs, setLogs] = useState<string[]>([])
  const [error, setError] = useState<string | null>(null)
  const [isConnected, setIsConnected] = useState(false)

  const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

  // Fetch status
  const fetchStatus = async () => {
    try {
      const response = await fetch(`${API_URL}/status`, { 
        signal: AbortSignal.timeout(3000) // 3 second timeout
      })
      if (!response.ok) throw new Error('Failed to fetch status')
      const data = await response.json()
      setStatus(data)
      setIsConnected(true)
      setError(null)
    } catch (err) {
      setError('Backend not deployed. Deploy backend to Railway/Render first.')
      setIsConnected(false)
      // Set demo data to show the UI works
      if (!status) {
        setStatus({
          generation: 0,
          status: "WAITING",
          last_mutation: "Backend not connected",
          crash_count: 0,
          successful_runs: 0,
          avg_execution_time: 0,
          recent_execution_times: [],
          uptime: 0,
          last_error: "Backend API not available"
        })
      }
    }
  }

  // Fetch logs
  const fetchLogs = async () => {
    try {
      const response = await fetch(`${API_URL}/logs?limit=20`, {
        signal: AbortSignal.timeout(3000)
      })
      if (!response.ok) throw new Error('Failed to fetch logs')
      const data: LogEntry = await response.json()
      setLogs(data.logs)
    } catch (err) {
      // Silently fail - we'll show demo message in UI
      if (logs.length === 0) {
        setLogs([
          '[--:--:--] 🧬 Project Ouroboros - GitHub Self-Healing Architecture',
          '[--:--:--] ⚠️ Backend not deployed yet',
          '[--:--:--] 📝 To activate self-healing:',
          '[--:--:--] 1. Deploy backend to Railway or Render',
          '[--:--:--] 2. Add NEXT_PUBLIC_API_URL to Vercel',
          '[--:--:--] 3. Or use GitHub Actions for self-healing (see GITHUB_ARCHITECTURE.md)',
          '[--:--:--] ✨ Frontend UI is working!'
        ])
      }
    }
  }

  // Inject chaos
  const injectChaos = async (chaosType: string = 'random') => {
    try {
      const response = await fetch(`${API_URL}/chaos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chaos_type: chaosType })
      })
      if (!response.ok) throw new Error('Failed to inject chaos')
      await fetchStatus()
    } catch (err) {
      console.error('Failed to inject chaos:', err)
    }
  }

  // Poll for updates
  useEffect(() => {
    fetchStatus()
    fetchLogs()
    
    const statusInterval = setInterval(fetchStatus, 1000)
    const logsInterval = setInterval(fetchLogs, 2000)
    
    return () => {
      clearInterval(statusInterval)
      clearInterval(logsInterval)
    }
  }, [])

  // Status color
  const getStatusColor = () => {
    if (!status) return 'text-gray-500'
    switch (status.status) {
      case 'ALIVE': return 'text-cyber-green'
      case 'CRASHED': return 'text-cyber-red'
      case 'MUTATING': return 'text-cyber-yellow'
      default: return 'text-cyber-blue'
    }
  }

  return (
    <div className="min-h-screen bg-cyber-bg scanlines p-4">
      {/* Header */}
      <header className="border-b-2 border-cyber-green pb-4 mb-6">
        <h1 className="text-4xl font-bold glow text-cyber-green mb-2">
          🧬 PROJECT OUROBOROS
        </h1>
        <p className="text-cyber-green/60 text-sm">
          THE GOD VIEW // THE LIVING SOFTWARE
        </p>
        <div className="flex items-center gap-2 mt-2">
          <div className={`w-2 h-2 rounded-full ${isConnected ? 'bg-cyber-green animate-pulse-fast' : 'bg-cyber-red'}`} />
          <span className="text-xs text-cyber-green/80">
            {isConnected ? 'CONNECTED' : 'DISCONNECTED'}
          </span>
        </div>
      </header>

      {error && (
        <div className="bg-cyber-yellow/10 border border-cyber-yellow p-4 mb-6 rounded">
          <div className="flex items-center gap-2">
            <AlertCircle className="text-cyber-yellow" />
            <span className="text-cyber-yellow font-bold">Demo Mode: Backend Not Connected</span>
          </div>
          <p className="text-cyber-yellow/80 text-sm mt-2">
            ✅ Frontend is working!<br />
            📝 To enable full functionality:<br />
            • Deploy backend to Railway/Render, OR<br />
            • Use GitHub Actions self-healing (no backend needed!)
          </p>
          <p className="text-cyber-yellow/60 text-xs mt-2">
            See GITHUB_ARCHITECTURE.md for GitHub-only setup
          </p>
        </div>
      )}

      {status && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-6">
          {/* Status Card */}
          <div className="bg-cyber-surface border border-cyber-border p-6 rounded">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-cyber-green font-bold">VITAL SIGNS</h2>
              <Activity className={`${getStatusColor()} animate-pulse-fast`} />
            </div>
            <div className="space-y-3">
              <div>
                <span className="text-cyber-green/60 text-xs">STATUS</span>
                <div className={`text-2xl font-bold ${getStatusColor()} glow`}>
                  {status.status}
                </div>
              </div>
              <div>
                <span className="text-cyber-green/60 text-xs">GENERATION</span>
                <div className="text-xl font-bold text-cyber-blue">
                  Gen {status.generation}
                </div>
              </div>
              <div>
                <span className="text-cyber-green/60 text-xs">AVG EXECUTION</span>
                <div className="text-lg text-cyber-green">
                  {status.avg_execution_time.toFixed(3)}s
                </div>
              </div>
            </div>
          </div>

          {/* Stats Card */}
          <div className="bg-cyber-surface border border-cyber-border p-6 rounded">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-cyber-green font-bold">STATISTICS</h2>
              <TrendingUp className="text-cyber-blue" />
            </div>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-cyber-green/60 text-sm">Successful Runs</span>
                <span className="text-cyber-green font-mono">{status.successful_runs}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-cyber-green/60 text-sm">Crashes</span>
                <span className="text-cyber-red font-mono">{status.crash_count}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-cyber-green/60 text-sm">Uptime Events</span>
                <span className="text-cyber-blue font-mono">{status.uptime}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-cyber-green/60 text-sm">Success Rate</span>
                <span className="text-cyber-green font-mono">
                  {status.successful_runs + status.crash_count > 0
                    ? ((status.successful_runs / (status.successful_runs + status.crash_count)) * 100).toFixed(1)
                    : 0}%
                </span>
              </div>
            </div>
          </div>

          {/* Chaos Controls */}
          <div className="bg-cyber-surface border border-cyber-red p-6 rounded">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-cyber-red font-bold">CHAOS CONTROLS</h2>
              <Siren className="text-cyber-red animate-pulse-fast" />
            </div>
            <div className="space-y-2">
              <button
                onClick={() => injectChaos('syntax_error')}
                className="w-full bg-cyber-red/10 hover:bg-cyber-red/20 border border-cyber-red text-cyber-red py-2 px-4 rounded transition text-sm font-bold"
              >
                💥 SYNTAX ERROR
              </button>
              <button
                onClick={() => injectChaos('division_by_zero')}
                className="w-full bg-cyber-red/10 hover:bg-cyber-red/20 border border-cyber-red text-cyber-red py-2 px-4 rounded transition text-sm font-bold"
              >
                ⚠️ DIVISION BY ZERO
              </button>
              <button
                onClick={() => injectChaos('delete_line')}
                className="w-full bg-cyber-red/10 hover:bg-cyber-red/20 border border-cyber-red text-cyber-red py-2 px-4 rounded transition text-sm font-bold"
              >
                🗑️ DELETE CODE LINE
              </button>
              <button
                onClick={() => injectChaos('random')}
                className="w-full bg-cyber-yellow/10 hover:bg-cyber-yellow/20 border border-cyber-yellow text-cyber-yellow py-2 px-4 rounded transition text-sm font-bold"
              >
                🎲 RANDOM CHAOS
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Mutation History */}
      {status && (
        <div className="bg-cyber-surface border border-cyber-border p-6 rounded mb-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-cyber-green font-bold">LAST MUTATION</h2>
            <Zap className="text-cyber-yellow" />
          </div>
          <div className="text-cyber-green/80 font-mono text-sm">
            {status.last_mutation}
          </div>
          {status.last_error && (
            <div className="mt-3 p-3 bg-cyber-red/5 border border-cyber-red/30 rounded">
              <div className="flex items-center gap-2 mb-2">
                <Skull className="text-cyber-red w-4 h-4" />
                <span className="text-cyber-red text-xs font-bold">LAST ERROR</span>
              </div>
              <div className="text-cyber-red/80 font-mono text-xs overflow-x-auto">
                {status.last_error}
              </div>
            </div>
          )}
        </div>
      )}

      {/* Live Terminal */}
      <div className="bg-cyber-surface border border-cyber-border p-6 rounded">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-cyber-green font-bold">LIVE TERMINAL</h2>
          <Terminal className="text-cyber-green" />
        </div>
        <div className="bg-black/50 p-4 rounded h-96 overflow-y-auto font-mono text-xs">
          {logs.length === 0 ? (
            <div className="text-cyber-green/40">Waiting for logs...</div>
          ) : (
            logs.map((log, i) => (
              <div
                key={i}
                className={`${
                  log.includes('💀') || log.includes('ERROR')
                    ? 'text-cyber-red'
                    : log.includes('✅')
                    ? 'text-cyber-green'
                    : log.includes('🧬')
                    ? 'text-cyber-blue'
                    : log.includes('⚠️')
                    ? 'text-cyber-yellow'
                    : 'text-cyber-green/70'
                } leading-relaxed`}
              >
                {log}
              </div>
            ))
          )}
          <div className="cursor text-cyber-green inline-block"></div>
        </div>
      </div>

      {/* Footer */}
      <footer className="mt-8 text-center text-cyber-green/40 text-xs">
        <p>PROJECT OUROBOROS v1.0 // THE LIVING SOFTWARE</p>
        <p className="mt-1">Deployed on Railway (Backend) + Vercel (Frontend)</p>
      </footer>
    </div>
  )
}
