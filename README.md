# SmartEvent – Event Discovery & Ticket Booking System

A full-stack event discovery and ticket booking platform.

- **Backend:** FastAPI, SQLAlchemy, JWT auth, QR code generation
- **Frontend:** React + Vite, React Router, Axios, Context API

## Structure

```
smartevent/
├── backend/    # FastAPI API (see backend/README.md)
└── frontend/   # React + Vite client (see frontend/README.md)
```

## Run locally

**1. Backend**

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**2. Frontend** (new terminal)

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173. The backend seeds 4 sample events on first run.

## Modules

1. User authentication (JWT, bcrypt)
2. Event discovery (search, category filter, details)
3. Ticket booking (availability checks, price calc, history)
4. QR code tickets (unique codes, downloadable images)
5. Notifications (booking confirmations, reminders, unread badge)
6. Responsive React UI with protected routes
