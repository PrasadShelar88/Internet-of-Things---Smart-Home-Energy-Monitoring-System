# Smart Home Energy Monitoring System

## Project Overview

The **Smart Home Energy Monitoring System** is an IoT-based project designed to monitor real-time electrical energy consumption in a home, hostel, lab, or small building.

The system measures important electrical parameters such as:

* Voltage
* Current
* Power consumption
* Energy usage
* Estimated electricity cost
* Appliance/circuit status
* High consumption alerts

This project helps users understand how much electricity is being consumed and where energy wastage is happening. It can also generate alerts when power consumption crosses a predefined limit.

This project supports both:

* Hardware implementation using ESP32 and current/voltage sensors
* Virtual simulation using Python backend and web dashboard

It is beginner-friendly, GitHub-ready, and suitable for IoT course projects, academic submissions, and placement portfolios.

---

## Problem Statement

In many homes and buildings, electricity consumption is checked only through monthly bills. Users do not know which appliance or circuit is consuming more power in real time.

This causes problems such as:

* High electricity bills
* Unnoticed standby power consumption
* Overload conditions
* Energy wastage
* Lack of appliance-level monitoring
* No real-time alert system
* No historical energy usage analysis

This project solves these problems by continuously monitoring energy usage and displaying real-time values on a dashboard.

---

## Objectives

The main objectives of this project are:

* Monitor voltage and current in real time
* Calculate power consumption
* Calculate energy usage in kWh
* Estimate electricity cost
* Generate high consumption alerts
* Simulate relay ON/OFF appliance control
* Store energy logs
* Export CSV and PDF reports
* Provide a dashboard for visualization
* Support virtual simulation without hardware
* Build a complete GitHub-ready IoT project

---

## Features

* Real-time voltage monitoring
* Real-time current monitoring
* Power calculation in watts
* Energy calculation in kWh
* Estimated electricity cost calculation
* High power alert
* High current alert
* Low voltage alert
* Overload detection
* Appliance/circuit monitoring
* Relay ON/OFF simulation
* Manual reading input
* Virtual simulation modes
* CSV report download
* PDF report generation
* SQLite data logging
* REST API backend
* Frontend dashboard
* Beginner-friendly setup

---

## IoT Concepts Used

This project demonstrates the following IoT concepts:

* Sensor data collection
* ESP32-based monitoring
* Current and voltage sensing
* Real-time data processing
* Energy calculation
* Threshold-based alert generation
* Dashboard visualization
* Data logging
* Remote monitoring
* API communication
* Smart home automation concept

---

## System Workflow

```text
Current / Voltage Sensor
        ↓
ESP32 / Python Simulation
        ↓
Energy Calculation
        ↓
Threshold Checking
        ↓
Alert Generation
        ↓
Dashboard Update
        ↓
CSV / PDF Report
        ↓
Energy Saving Decision
```

---

## Architecture

```text
+----------------------------+
| Sensors / Simulation       |
|----------------------------|
| Voltage                    |
| Current                    |
| Appliance Status           |
+-------------+--------------+
              |
              v
+----------------------------+
| Processing Unit            |
| ESP32 / FastAPI Backend    |
|----------------------------|
| Power Calculation          |
| Energy Calculation         |
| Cost Estimation            |
| Threshold Checking         |
+-------------+--------------+
              |
              v
+----------------------------+
| Dashboard                  |
|----------------------------|
| Real-time Values           |
| Alerts                     |
| Relay Control              |
| Logs                       |
| CSV/PDF Reports            |
+----------------------------+
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLite
* Uvicorn
* CSV report generation
* PDF report generation

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS
* Dashboard UI
* API integration

### Hardware / Simulation

* ESP32
* ACS712 Current Sensor
* Voltage Sensor Module
* Relay Module
* Buzzer
* LED Indicators
* Python-based virtual simulation

---

## Hardware Components

| Component             | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| ESP32                 | Reads sensor data and sends it to dashboard/cloud |
| ACS712 Current Sensor | Measures current consumed by appliance/circuit    |
| Voltage Sensor Module | Measures voltage level                            |
| Relay Module          | Controls appliance ON/OFF                         |
| Buzzer                | Generates alert for overload/high usage           |
| LED                   | Shows system or alert status                      |
| OLED/LCD Display      | Optional local display for readings               |
| Power Supply          | Powers ESP32 and modules                          |
| Dashboard             | Shows real-time energy data                       |

---

## Folder Structure

```text
Smart-Home-Energy-Monitoring-System/
│
├── arduino_code/
│   └── smart_home_energy_esp32.ino
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── database.db
│   └── README.md
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   └── src/
│
├── python_simulation/
│   └── energy_simulation.py
│
├── data/
│   └── energy_logs.csv
│
├── outputs/
│   └── energy_report.pdf
│
├── images/
│   └── dashboard_screenshot.png
│
├── circuit_diagram/
│   └── circuit.png
│
├── reports/
│   └── project_report.md
│
├── docs/
│   └── setup_guide.md
│
├── README.md
└── .gitignore
```

---

## Backend Setup

### Step 1: Open PowerShell

Go to backend folder:

```powershell
cd "C:\Projects\IOT\energy_project\smart_home_energy_backend"
```

### Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

### Step 3: Activate Virtual Environment

```powershell
.\venv\Scripts\activate
```

### Step 4: Install Requirements

```powershell
pip install -r requirements.txt
```

### Step 5: Run Backend Server

```powershell
python -m uvicorn main:app --reload
```

### Step 6: Open API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Open a new PowerShell window.

### Step 1: Go to frontend folder

```powershell
cd "C:\Projects\IOT\energy_project\smart_home_energy_frontend"
```

### Step 2: Install Frontend Packages

```powershell
npm install
```

### Step 3: Run Frontend

```powershell
npm run dev
```

### Step 4: Open Dashboard

```text
http://localhost:5173
```

---

## API Endpoints

| Method | Endpoint          | Description                        |
| ------ | ----------------- | ---------------------------------- |
| GET    | `/`               | Backend health check               |
| GET    | `/latest`         | Get latest energy reading          |
| GET    | `/readings`       | Get all energy logs                |
| POST   | `/simulate`       | Generate virtual energy reading    |
| POST   | `/manual-reading` | Add manual voltage/current reading |
| POST   | `/relay/on`       | Turn relay ON                      |
| POST   | `/relay/off`      | Turn relay OFF                     |
| POST   | `/thresholds`     | Save threshold settings            |
| GET    | `/export/csv`     | Download CSV report                |
| GET    | `/export/pdf`     | Download PDF report                |
| DELETE | `/clear`          | Clear all logs                     |

---

## Sample Energy Data

```json
{
  "appliance": "Main Circuit",
  "voltage": 230,
  "current": 2.5,
  "power": 575,
  "energy_kwh": 0.0096,
  "cost": 0.08,
  "relay_status": "ON",
  "alert": "NORMAL"
}
```

---

## Power Calculation

Power is calculated using:

```text
Power (Watts) = Voltage × Current
```

Example:

```text
Voltage = 230 V
Current = 2.5 A

Power = 230 × 2.5
Power = 575 W
```

---

## Energy Calculation

Energy is calculated using:

```text
Energy (kWh) = Power (kW) × Time (Hours)
```

Example:

```text
Power = 1000 W = 1 kW
Time = 5 hours

Energy = 1 × 5
Energy = 5 kWh
```

---

## Cost Calculation

Electricity cost is calculated using:

```text
Cost = Energy (kWh) × Electricity Rate
```

Example:

```text
Energy = 5 kWh
Rate = ₹8 per kWh

Cost = 5 × 8
Cost = ₹40
```

---

## Alert Logic

The system generates alerts based on threshold values.

Example logic:

```text
If power > max power threshold:
    Generate HIGH POWER ALERT

If current > max current threshold:
    Generate HIGH CURRENT ALERT

If voltage < minimum voltage threshold:
    Generate LOW VOLTAGE ALERT

If power is too high:
    Mark condition as OVERLOAD
```

---

## Virtual Simulation

If real hardware is not available, this project supports virtual simulation.

Simulation modes include:

* Normal energy usage
* High energy usage
* Overload condition
* Low voltage condition
* Standby power consumption
* Multiple appliance usage

This makes the project suitable for students who want to demonstrate IoT concepts without physical sensors.

---

## Dashboard Features

The dashboard displays:

* Voltage
* Current
* Power
* Energy usage
* Estimated cost
* Alert count
* Latest system status
* Relay ON/OFF status
* Manual reading form
* Threshold settings
* Power trend chart
* Recent energy logs
* CSV download
* PDF download
* Clear logs option
* Simulation buttons

---

## ESP32 Wiring

### ACS712 Current Sensor to ESP32

| ACS712 Pin | ESP32   |
| ---------- | ------- |
| VCC        | 5V      |
| GND        | GND     |
| OUT        | GPIO 34 |

### Voltage Sensor Module to ESP32

| Voltage Sensor | ESP32   |
| -------------- | ------- |
| VCC            | 5V      |
| GND            | GND     |
| OUT            | GPIO 35 |

### Relay Module to ESP32

| Relay | ESP32   |
| ----- | ------- |
| IN    | GPIO 25 |
| VCC   | 5V      |
| GND   | GND     |

### Buzzer and LED

| Component | ESP32   |
| --------- | ------- |
| Buzzer    | GPIO 26 |
| LED       | GPIO 27 |

---

## Safety Note

This project involves electrical energy monitoring. For student demonstrations, use:

* Virtual simulation
* Low-voltage DC loads
* Ready-made sensor modules
* Non-invasive current clamps
* Smart plug based readings

Do not directly touch or modify live AC mains wiring. Any real AC mains installation should be handled only by a qualified electrician.

---

## ESP32 Code Concept

```cpp
#define CURRENT_PIN 34
#define VOLTAGE_PIN 35
#define RELAY_PIN 25
#define BUZZER_PIN 26

float voltage = 230.0;
float current = 2.5;
float power = voltage * current;

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  power = voltage * current;

  if (power > 1500) {
    digitalWrite(BUZZER_PIN, HIGH);
    Serial.println("High power alert");
  } else {
    digitalWrite(BUZZER_PIN, LOW);
  }

  Serial.print("Power: ");
  Serial.println(power);

  delay(2000);
}
```

---

## Report Generation

The system can generate an energy consumption report containing:

* Timestamp
* Appliance/circuit name
* Voltage
* Current
* Power
* Energy used
* Estimated cost
* Relay status
* Alert status

Reports can be exported as:

* CSV
* PDF

---


## Applications

This project can be used in:

* Smart homes
* Hostels
* College labs
* PG rooms
* Small offices
* Smart buildings
* Energy monitoring labs
* IoT training projects
* Smart automation projects

---

## Industry Relevance

Smart energy monitoring systems are used by:

* Home automation companies
* Smart building companies
* Energy management companies
* Solar energy companies
* Factories
* Commercial buildings
* Utility monitoring systems

These systems help users reduce energy wastage, monitor power usage, identify overloads, and improve energy efficiency.

---

## Learning Outcomes

By completing this project, I learned:

* How IoT-based energy monitoring works
* How voltage and current are used to calculate power
* How energy consumption is calculated in kWh
* How electricity cost is estimated
* How threshold-based alerts are generated
* How relay control can simulate appliance automation
* How to build a FastAPI backend
* How to connect a frontend dashboard with backend APIs
* How to generate CSV and PDF reports
* How to document and upload a project on GitHub

---

## Future Improvements

Possible future improvements:

* Add MQTT support
* Add Grafana dashboard
* Add Home Assistant integration
* Add appliance-level monitoring
* Add smart plug integration
* Add solar energy monitoring
* Add mobile app notifications
* Add AI-based energy forecasting
* Add voice assistant support
* Add automated load balancing
* Add real-time cloud database integration

---

## Interview Preparation

### 1. Explain your project.

This is an IoT-based Smart Home Energy Monitoring System that monitors voltage, current, power consumption, and energy usage. The system calculates estimated electricity cost and displays real-time values on a dashboard. It also generates alerts when power consumption exceeds predefined limits.

### 2. What problem does this project solve?

This project helps users monitor electricity usage in real time, identify energy wastage, reduce electricity bills, and detect overload conditions.

### 3. Which sensors are used?

The project can use an ACS712 current sensor, voltage sensor module, relay module, buzzer, LED indicators, and ESP32 for IoT communication.

### 4. Why did you use ESP32?

ESP32 is used because it has built-in Wi-Fi, good processing capability, supports multiple sensors, and can send data to a dashboard or cloud platform.

### 5. How is power consumption calculated?

Power is calculated using the formula:

```text
Power = Voltage × Current
```

For example, if voltage is 230V and current is 2A, then power is 460W.

### 6. How is energy consumption calculated?

Energy consumption is calculated using:

```text
Energy = Power in kW × Time in hours
```

For example, a 1 kW appliance running for 5 hours consumes 5 kWh.

### 7. What output does the system generate?

The system generates voltage readings, current readings, power usage, energy consumption, estimated cost, relay status, alerts, dashboard charts, CSV logs, and PDF reports.

### 8. How does IoT help in this project?

IoT allows electrical consumption data to be sent from sensors to a dashboard where users can monitor usage remotely in real time.

### 9. What challenges did you face?

Challenges included sensor calibration, accurate power calculation, handling fluctuating sensor values, dashboard integration, and alert threshold configuration.

### 10. How can this project be improved?

It can be improved with MQTT, Grafana, Home Assistant, smart plug integration, mobile alerts, AI-based energy forecasting, solar monitoring, and appliance-level analytics.

---

## GitHub Repository Details

### Repository Name

```text
Smart-Home-Energy-Monitoring-System
```

### Description

```text
An IoT-based smart home energy monitoring system that measures voltage, current, power, energy usage, cost, alerts, relay status, dashboard visualization, CSV/PDF reports, and virtual simulation.
```

### GitHub Topics

```text
iot
smart-home
energy-monitoring
esp32
acs712
fastapi
python
react
iot-dashboard
electricity-monitoring
home-automation
energy-analytics
```

---

## Author

**Prasad Shelar**

---

## License

This project is created for educational and academic purposes. You can use and modify it for learning, college submissions, and portfolio building.

---

## Conclusion

The **Smart Home Energy Monitoring System** demonstrates how IoT can be used to monitor electricity usage, detect high consumption, estimate cost, and improve energy efficiency. It is beginner-friendly, simulation-ready, and suitable for GitHub portfolio, academic project submission, and placement preparation.
