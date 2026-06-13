from datetime import datetime
import random

DEFAULT_THRESHOLDS = {
    "max_power_watts": 1500.0,
    "max_current_amps": 10.0,
    "electricity_rate_per_kwh": 8.0,
}

relay_status = "ON"
thresholds = DEFAULT_THRESHOLDS.copy()

APPLIANCES = [
    {"name": "LED Lights", "current": (0.1, 0.6)},
    {"name": "Ceiling Fan", "current": (0.3, 0.8)},
    {"name": "Laptop Charger", "current": (0.2, 0.7)},
    {"name": "Refrigerator", "current": (0.8, 2.5)},
    {"name": "Washing Machine", "current": (2.0, 6.0)},
    {"name": "Water Heater", "current": (6.0, 13.0)},
]


def calculate_energy(voltage: float, current: float, duration_minutes: float, appliance: str = "Main Circuit"):
    power = round(voltage * current, 2)
    energy_kwh = round((power / 1000) * (duration_minutes / 60), 5)
    cost = round(energy_kwh * thresholds["electricity_rate_per_kwh"], 2)

    alerts = []
    if power > thresholds["max_power_watts"]:
        alerts.append("HIGH_POWER_CONSUMPTION")
    if current > thresholds["max_current_amps"]:
        alerts.append("OVER_CURRENT")
    if voltage < 200:
        alerts.append("LOW_VOLTAGE")
    if voltage > 250:
        alerts.append("HIGH_VOLTAGE")
    if relay_status == "OFF":
        alerts.append("RELAY_OFF_LOAD_DISABLED")

    alert_status = "NORMAL" if not alerts else ", ".join(alerts)
    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "voltage": round(voltage, 2),
        "current": round(current, 2),
        "power": power,
        "energy_kwh": energy_kwh,
        "estimated_cost": cost,
        "appliance": appliance,
        "relay_status": relay_status,
        "alert_status": alert_status,
    }


def simulate_reading(mode: str = "normal"):
    voltage = random.uniform(220, 240)
    appliance = random.choice(APPLIANCES)
    current_low, current_high = appliance["current"]

    if mode == "high":
        appliance = {"name": "Water Heater + Washing Machine", "current": (8.0, 15.0)}
        current_low, current_high = appliance["current"]
    elif mode == "overload":
        appliance = {"name": "Multiple Heavy Loads", "current": (12.0, 20.0)}
        current_low, current_high = appliance["current"]
    elif mode == "low_voltage":
        voltage = random.uniform(170, 199)
    elif mode == "standby":
        appliance = {"name": "Standby Devices", "current": (0.05, 0.25)}
        current_low, current_high = appliance["current"]

    current = random.uniform(current_low, current_high)
    return calculate_energy(voltage, current, duration_minutes=1, appliance=appliance["name"])


def update_thresholds(max_power_watts: float, max_current_amps: float, electricity_rate_per_kwh: float):
    thresholds["max_power_watts"] = max_power_watts
    thresholds["max_current_amps"] = max_current_amps
    thresholds["electricity_rate_per_kwh"] = electricity_rate_per_kwh
    return thresholds


def set_relay(status: str):
    global relay_status
    relay_status = status
    return relay_status
