from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

from app.database import init_db, insert_reading, fetch_readings, latest_reading, clear_readings
from app.logic import calculate_energy, simulate_reading, update_thresholds, set_relay, thresholds, relay_status
from app.models import EnergyReadingInput, ThresholdConfig, RelayCommand
from app.reports import export_csv, export_pdf

app = FastAPI(
    title="Smart Home Energy Monitoring System Backend",
    description="Backend API for voltage, current, power, energy, cost, alerts, relay control, simulation, CSV and PDF reports.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def root():
    return {
        "project": "Smart Home Energy Monitoring System",
        "status": "Backend running successfully",
        "docs": "http://127.0.0.1:8000/docs",
        "frontend_expected": "http://localhost:5173",
    }


@app.post("/api/readings")
def add_manual_reading(payload: EnergyReadingInput):
    reading = calculate_energy(
        voltage=payload.voltage,
        current=payload.current,
        duration_minutes=payload.duration_minutes,
        appliance=payload.appliance,
    )
    reading_id = insert_reading(reading)
    reading["id"] = reading_id
    return {"message": "Reading saved successfully", "reading": reading}


@app.post("/api/simulate")
def create_simulated_reading(mode: str = Query(default="normal", enum=["normal", "high", "overload", "low_voltage", "standby"])):
    reading = simulate_reading(mode)
    reading_id = insert_reading(reading)
    reading["id"] = reading_id
    return {"message": f"{mode} simulation reading saved", "reading": reading}


@app.get("/api/readings")
def get_readings(limit: int = Query(default=50, ge=1, le=500)):
    return {"readings": fetch_readings(limit)}


@app.get("/api/latest")
def get_latest():
    reading = latest_reading()
    if not reading:
        reading = simulate_reading("normal")
        reading_id = insert_reading(reading)
        reading["id"] = reading_id
    return {"reading": reading}


@app.get("/api/summary")
def get_summary():
    readings = fetch_readings(500)
    total_energy = round(sum(float(r["energy_kwh"]) for r in readings), 5)
    total_cost = round(sum(float(r["estimated_cost"]) for r in readings), 2)
    max_power = max([float(r["power"]) for r in readings], default=0)
    alerts = [r for r in readings if r["alert_status"] != "NORMAL"]
    return {
        "total_readings": len(readings),
        "total_energy_kwh": total_energy,
        "estimated_total_cost": total_cost,
        "peak_power_watts": max_power,
        "alert_count": len(alerts),
        "relay_status": relay_status,
        "thresholds": thresholds,
    }


@app.put("/api/thresholds")
def configure_thresholds(payload: ThresholdConfig):
    updated = update_thresholds(payload.max_power_watts, payload.max_current_amps, payload.electricity_rate_per_kwh)
    return {"message": "Thresholds updated", "thresholds": updated}


@app.get("/api/thresholds")
def get_thresholds():
    return {"thresholds": thresholds}


@app.post("/api/relay")
def control_relay(payload: RelayCommand):
    status = set_relay(payload.status)
    return {"message": f"Relay turned {status}", "relay_status": status}


@app.post("/api/clear")
def clear_data():
    clear_readings()
    return {"message": "All readings cleared"}


@app.get("/api/export/csv")
def download_csv():
    readings = fetch_readings(10000)
    path = export_csv(readings)
    return FileResponse(path, filename="energy_readings.csv", media_type="text/csv")


@app.get("/api/export/pdf")
def download_pdf():
    readings = fetch_readings(10000)
    path = export_pdf(readings)
    return FileResponse(path, filename="energy_consumption_report.pdf", media_type="application/pdf")
