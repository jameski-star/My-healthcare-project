# CareBridge — Full‑Stack Healthcare App

This is a starter project for CareBridge: a full-stack healthcare platform with FastAPI, React, PostgreSQL, and M-Pesa STK Push.

## Quick Start

1. Copy `.env.example` to `.env`
2. Run `docker-compose up --build`
3. Apply migrations: `alembic upgrade head`
4. Seed database: `python -m infra.db.seed`
5. Open: 
   - API: http://localhost:8000/docs
   - Web: http://localhost:5173


---
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green)
![React](https://img.shields.io/badge/React-18+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
