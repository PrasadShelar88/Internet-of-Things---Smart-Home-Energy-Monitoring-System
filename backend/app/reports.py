import csv
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
REPORT_DIR = BASE_DIR / "reports"
OUTPUT_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)


def export_csv(readings):
    path = OUTPUT_DIR / "energy_readings.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "timestamp", "voltage", "current", "power", "energy_kwh", "estimated_cost", "appliance", "relay_status", "alert_status"],
        )
        writer.writeheader()
        writer.writerows(readings)
    return str(path)


def export_pdf(readings):
    path = REPORT_DIR / "energy_consumption_report.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Smart Home Energy Monitoring Report")
    y -= 30
    c.setFont("Helvetica", 10)
    total_energy = sum(float(r.get("energy_kwh", 0)) for r in readings)
    total_cost = sum(float(r.get("estimated_cost", 0)) for r in readings)
    c.drawString(40, y, f"Total readings: {len(readings)} | Total energy: {total_energy:.4f} kWh | Estimated cost: Rs. {total_cost:.2f}")
    y -= 30
    c.setFont("Helvetica-Bold", 8)
    c.drawString(40, y, "Time")
    c.drawString(155, y, "Appliance")
    c.drawString(275, y, "V")
    c.drawString(320, y, "A")
    c.drawString(360, y, "W")
    c.drawString(410, y, "kWh")
    c.drawString(465, y, "Alert")
    y -= 15
    c.setFont("Helvetica", 8)
    for r in readings[:35]:
        if y < 60:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 8)
        c.drawString(40, y, str(r["timestamp"])[:19])
        c.drawString(155, y, str(r["appliance"])[:18])
        c.drawString(275, y, str(r["voltage"]))
        c.drawString(320, y, str(r["current"]))
        c.drawString(360, y, str(r["power"]))
        c.drawString(410, y, str(r["energy_kwh"]))
        c.drawString(465, y, str(r["alert_status"])[:22])
        y -= 14
    c.save()
    return str(path)
