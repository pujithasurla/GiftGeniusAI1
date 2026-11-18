# GiftGenius AI

Agentic AI Smart Gift Recommendation Platform built with Python, Flask, and Ollama.

## Phase 1 (complete)

- Project folder structure
- Flask application factory and Blueprint architecture
- Environment-based configuration (`.env`)
- Reusable Ollama client
- Bootstrap 5 navigation and premium landing page
- Light / dark theme toggle

## Phase 2 (complete)

- `InterviewAgent` with 17 guided questions (Mode 1)
- One-question-at-a-time interview UI with progress, back, and skip
- Session-persisted answers, AI acknowledgements, and closing gift brief
- Offline-safe fallbacks when Ollama is unavailable
- Search history of completed interviews

## Shopping suite (complete)

- Smart Gift Shop Locator (OpenStreetMap + Leaflet map)
- Online Price Comparison (estimate bands + Amazon/Flipkart/… search links)
- Shopping Checklist (save / print / download)
- Gift Match Score with animated ring + breakdown
- Occasion Countdown with tips and celebration state
- Gift Wrapping Design Agent
- Personalized Greeting Card Agent
- AI Shopping Assistant with recommendation memory
- Premium Dashboard aggregating all of the above

## Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| AI | Ollama (`llama3`) |
| Data / reports (later phases) | SQLite, Pandas, Plotly, FPDF |

## Quick start

```bash
cd GiftGeniusAI
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # or: cp .env.example .env
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Environment

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
SECRET_KEY=change-this-to-a-long-random-secret-in-production
```

Ollama is optional for Phase 1–2. When available, the Interview Agent uses it for warmer acknowledgements and summaries; otherwise curated fallbacks are used.

## Project structure

```
GiftGeniusAI/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── agents/
├── routes/
├── templates/
├── static/
├── utils/
└── reports/
```

## Application flow (full product)

Home → AI Interview → Multi-Agent Analysis → Recommendations → Budget → Comparison → Report → AI Chat

Later phases unlock dashboards, comparisons, PDF reports, category/occasion explorers, and chat.
