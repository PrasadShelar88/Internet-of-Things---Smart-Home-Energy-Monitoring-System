# API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Use |
|---|---|---|
| GET | `/` | Health check |
| GET | `/docs` | Swagger API testing page |
| POST | `/api/simulate?mode=normal` | Create simulated normal reading |
| POST | `/api/simulate?mode=high` | Create high usage reading |
| POST | `/api/simulate?mode=overload` | Create overload alert reading |
| POST | `/api/readings` | Save manual voltage/current reading |
| GET | `/api/readings` | Get recent readings |
| GET | `/api/latest` | Get latest reading |
| GET | `/api/summary` | Dashboard summary |
| PUT | `/api/thresholds` | Update power/current/cost thresholds |
| POST | `/api/relay` | Turn relay ON/OFF |
| GET | `/api/export/csv` | Download CSV report |
| GET | `/api/export/pdf` | Download PDF report |
