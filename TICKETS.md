# Tickets — Django Weather Dashboard

## T1: Implement view — API call and error handling
**Status:** Done
**File:** `weather/views.py`

Fill in `weather_page(request)`:
- Call `requests.get(API_URL, params=DEFAULT_PARAMS, timeout=10)`
- Wrap in `try/except requests.exceptions.RequestException`
- On success: call `response.json()` and parse the data
- On failure: set an `error` message string

## T2: Implement view — Build bullets list
**Status:** In Progress
**File:** `weather/views.py`

After parsing the API JSON:
- Extract current temp, wind speed, daily high/low, precipitation
- Use `.get()` for safe key access (handle missing keys)
- Build a `bullets` list of human-readable strings (e.g. `"Current temperature: 72°F"`)
- If API failed, set `bullets` to an empty list

## T3: Implement view — Render template with context
**Status:** In Progress
**File:** `weather/views.py`

- Build a context dict with `title`, `bullets`, `error`, `fetched_at`
- `fetched_at` = current timestamp via `datetime.now()`
- Return `render(request, "weather/weather.html", context)`

## T4: Create the HTML template
**Status:** Not Started
**File:** `weather/templates/weather/weather.html`

- Display `{{ title }}` as a heading
- If `{{ error }}`: show a friendly error message
- Loop `{% for bullet in bullets %}` and render as `<li>` items
- Show `{{ fetched_at }}` timestamp at the bottom

## T5: End-to-end verification
**Status:** Not Started

- Run `python manage.py runserver 8001`
- Visit http://127.0.0.1:8001/weather/
- Confirm bullet points render with live Chicago weather data
- Test error path (e.g. disconnect network) — page should still render with error message
