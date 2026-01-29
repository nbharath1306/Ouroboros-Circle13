import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Project Ouroboros - God View',
  description: 'The Living Software - Real-time monitoring dashboard',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
