# Smart Home Energy Monitoring System - Backend

This is the backend for an IoT-based Smart Home Energy Monitoring System. It simulates or accepts voltage/current data, calculates power, energy consumption, estimated electricity cost, detects high usage alerts, stores readings in SQLite, and exports CSV/PDF reports.

## Features

- FastAPI backend
- Real-time simulated energy readings
- Manual voltage/current entry
- Power calculation: `Power = Voltage × Current`
- Energy calculation: `Energy kWh = Power kW × Time hours`
- Estimated electricity cost calculation
- High power, over-current, low voltage, and high voltage alerts
- Relay ON/OFF simulation
- SQLite data logging
- CSV export
- PDF report generation
- Swagger API testing page

## Folder Structure

```text
smart_home_energy_backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── logic.py
│   ├── models.py
│   └── reports.py
├── data/
├── outputs/
├── reports/
├── docs/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Backend Run Commands

Use a simple folder path without `&` in the name. Example:

```powershell
cd C:\Projects\IOT
mkdir energy_project
```

Copy/extract this backend folder inside:

```text
C:\Projects\IOT\energy_project\smart_home_energy_backend
```

Then run:

```powershell
cd "C:\Projects\IOT\energy_project\smart_home_energy_backend"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Test Simulation

In Swagger `/docs`, try:

```text
POST /api/simulate?mode=normal
POST /api/simulate?mode=high
POST /api/simulate?mode=overload
GET /api/readings
GET /api/summary
GET /api/export/csv
GET /api/export/pdf
```

## Manual Reading Example

Endpoint: `POST /api/readings`

```json
{
  "voltage": 230,
  "current": 6.5,
  "appliance": "Water Heater",
  "duration_minutes": 10
}
```

## Notes for Students

This backend is suitable even without real IoT hardware. You can use the simulation endpoint as virtual sensor data and connect a frontend dashboard to the API.

For real hardware, ESP32 can read data from ACS712/current sensor and voltage sensor, then send voltage/current readings to `POST /api/readings`.
