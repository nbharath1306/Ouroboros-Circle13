# Project Ouroboros - Backend (The Organism)

## Setup

```bash
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and add your OpenAI API key.

## Run

```bash
python main.py
```

The API will be available at `http://localhost:8000`

## Endpoints

- `GET /status` - Get organism status
- `GET /logs` - Get recent execution logs  
- `POST /chaos` - Inject chaos (simulate errors)
