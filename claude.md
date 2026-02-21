# CLAUDE.md — Django Weather Dashboard

## Context
A tiny Django app to learn the “Controller + View” pattern:
- Call an external API from a Django view (server-side).
- Render results on a page as bullet points (template).
- No database persistence yet (Models come later).

The developer is new to web development. Keep explanations clear and approachable.

## Project Structure
- **Project:** `dashboard/` (settings, root URLs)
- **App:** `weather/` (views, app URLs, templates)
- **Tracking:** `PROGRESS.md` (high-level status), `TICKETS.md` (specific work items)

## Definition of Done (DoD)
- `python manage.py runserver` works locally
- `/weather/` renders bullet points derived from live API data
- API call happens server-side (in the Django view), not in browser JS
- Basic error handling: if the API fails, the page still renders with a friendly message
- Code is simple, readable, and follows Django conventions

## Tech Constraints
- Django 6.x, Python 3.13
- `requests` library for HTTP calls
- No API keys required (uses Open-Meteo)
- Server-side templates only (no React, no SPA)

## API Reference (Open-Meteo, No Auth)
Default city: Chicago (41.8781, -87.6298)

Endpoint: `https://api.open-meteo.com/v1/forecast`

Params: `latitude`, `longitude`, `current` (temperature_2m, wind_speed_10m), `daily` (temperature_2m_max, temperature_2m_min, precipitation_sum), `timezone` (America/Chicago)

## Style / Quality
- Keep code concise and conventional
- Constants for API URL and default params (already in `views.py`)
- Function-based views (no class-based views)
- No database models
- Inline comments only where they reduce confusion

## Environment
- Venv: `.venv/` (activate with `source .venv/bin/activate`)
- Dev server: `python manage.py runserver 8001` (port 8000 is occupied)
- Test URL: http://127.0.0.1:8001/weather/
- Migration warnings are safe to ignore (no DB used)

## Commit Style
Use conventional commits: `type: short description`
- `feat` — new functionality
- `fix` — bug fix
- `docs` — documentation only
- `chore` — config, tooling, maintenance
- `refactor` — code restructuring, no behavior change

## Stretch (only after core DoD is met)
- 10-minute caching via Django cache framework, OR
- Small form to choose city (no DB)