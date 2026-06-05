# AGENTS

## Purpose
This repository is a small FastAPI exercise app with a static frontend for signing students up for extracurricular activities.

## What to know first
- `src/app.py` defines the FastAPI application and mounts `src/static` at `/static`.
- `src/static/index.html`, `src/static/app.js`, and `src/static/styles.css` implement the frontend.
- `requirements.txt` lists the runtime dependencies: `fastapi`, `uvicorn`, `httpx`, and `watchfiles`.
- The repo does not currently include a test suite.

## Run locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
   ```
3. Confirm in-browser behavior:
   - API docs: `http://localhost:8000/docs`
   - Frontend: `http://localhost:8000/static/index.html`

## Key behavior
- `GET /activities` returns the in-memory activities payload.
- `POST /activities/{activity_name}/signup?email=...` appends the email to the activity's participant list.
- Data is stored only in memory and resets on server restart.
- The frontend uses activity names as the API identifier.

## Agent guidance
- Keep changes aligned with this small learning exercise; avoid adding unnecessary architecture or persistence layers unless explicitly requested.
- If you change API request/response shapes, also update the frontend behavior in `src/static/app.js`.
- Prefer simple Python and vanilla JS fixes over large refactors.
- Use the existing `README.md` and `src/README.md` for project context rather than duplicating documentation.
