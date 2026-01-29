# Project Ouroboros - Frontend (God View)

The real-time monitoring dashboard for the living software.

## Setup

```bash
npm install
```

## Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

## Environment Variables

Create a `.env.local` file:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

For production (Vercel), set this to your Railway/Render backend URL.

## Build

```bash
npm run build
npm start
```

## Deploy to Vercel

```bash
vercel
```

Make sure to set the `NEXT_PUBLIC_API_URL` environment variable in Vercel dashboard.
