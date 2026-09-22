# Grihome

Household Document & Warranty Expiry Tracker — a BCA final year major project.

Grihome lets users upload household documents (warranty cards, insurance policies,
AMC contracts, rental agreements), automatically extracts expiry dates from the
document using OCR, and proactively reminds users before those dates lapse —
solving the real-world problem of missed warranty claims and lapsed policies due
to documents being scattered across WhatsApp, email, and physical folders.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL, Alembic
- **OCR:** Tesseract (via pytesseract)
- **Auth:** JWT
- **Scheduler:** APScheduler (in-app notifications for upcoming expiries)
- **Frontend:** React (Vite) + Tailwind CSS

## Project Structure

```
grihome/
├── backend/    # FastAPI application
└── frontend/   # React application
```

## Setup

See project documentation for full setup steps (PostgreSQL install, Tesseract
install, virtual environment, and running the dev servers).

## Status

🚧 In development — Phase 0 (project scaffolding) complete.