# SGE — Society of Geoinformatics Engineers (Flask site)

A single-page site for SGE (Institute of Remote Sensing, CEG, Anna University),
built with Flask + Jinja templates, plain CSS, and vanilla JS. No database —
all content lives in `app.py` as simple Python data structures, so it's easy
to edit copy, add events, or swap sponsors without touching HTML.

## Run it locally

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install flask
python app.py
```

Then open **http://localhost:5000** in your browser.

## Project structure

```
sge_site/
├── app.py                 # Flask app + all site content (edit copy here)
├── templates/
│   ├── base.html          # <head>, fonts, shared scaffolding
│   └── index.html         # nav, hero, about, vision/mission, events, gallery, sponsors, alumni, footer
├── static/
│   ├── css/style.css      # design system (tokens, layout, components)
│   ├── js/main.js         # nav scroll state + mobile menu toggle
│   └── images/            # logo + event/campus photos (extracted from the source PDF)
└── README.md
```

## Editing content

Open `app.py` and edit the constants near the top:
- `SITE` — org name, tagline, coordinates
- `ABOUT_TEXT`, `VISION_TEXT`, `MISSION_TEXT`
- `EVENTS` — list of dicts (GEOHORIZON, CELESTIA, SPACE WEEK); add a new dict to add a new event section automatically
- `GALLERY` — image + caption pairs shown in the gallery grid
- `SPONSORS` — list of sponsor names, rendered as a numbered "benchmark" ledger
- `ALUMNI` — list of alumni support entries

## Deploying for free (Render)

1. Push this folder to a new GitHub repo.
2. Go to [render.com](https://render.com) → **New** → **Web Service** → connect the repo.
3. Render should auto-detect Python. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
4. Click **Create Web Service**. Render assigns a free `*.onrender.com` URL and redeploys automatically on every push.

The free tier spins the app down after ~15 minutes of no traffic and takes a few seconds to wake back up on the next visit — fine for a low-traffic association site.

`requirements.txt` and `Procfile` are already included for this.

## Notes

- Images were extracted from the supplied `WEBSITE_CONTENT.pdf` and resized/compressed for the web.
- Social links in the footer (Instagram, X) use the handles printed on the GEOHORIZON poster; double-check them before publishing.
- This is a Flask **development server** (`app.run(debug=True)`). For production, run behind a real WSGI server (gunicorn, etc.) and set `debug=False`.
