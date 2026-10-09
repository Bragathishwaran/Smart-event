@echo off
title SmartEvent Dev
echo Starting SmartEvent backend + frontend...
start "SmartEvent Backend" cmd /k "cd /d %~dp0backend && .venv\Scripts\python -m uvicorn app.main:app --reload --port 8000"
start "SmartEvent Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"
echo.
echo Both servers are starting.
echo  - App:        http://localhost:5173
echo  - API docs:   http://localhost:8000/docs
echo Close their windows to stop the servers.