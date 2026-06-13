# Smart Home Energy Monitoring System - Frontend

React + Vite dashboard for the Smart Home Energy Monitoring FastAPI backend.

## Features

- Real-time voltage, current, power, energy and cost cards
- Alert status display
- Energy usage table
- Simulation buttons: normal, high, overload, low voltage, standby
- Manual reading form
- Threshold settings
- Relay ON/OFF controls
- CSV and PDF report download buttons

## Backend expected URL

Default backend URL:

```text
http://127.0.0.1:8000
```

Create `.env` if you need to change it:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Run Frontend

Use a clean path without special symbols like `&`.

```powershell
cd "C:\Projects\IOT\energy_project\smart_home_energy_frontend"
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

## Important for Windows

Do not run this project from a folder containing `&` in its name. Use a clean path such as:

```text
C:\Projects\IOT\energy_project\smart_home_energy_frontend
```
