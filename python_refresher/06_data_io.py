"""Python refresher: file I/O and simple data aggregation."""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
CSV_FILE_PATH = DATA_DIR / "temperature_readings.csv"
SUMMARY_FILE_PATH = DATA_DIR / "temperature_summary.csv"

print("parse plain text lines from CSV file:")
with open(CSV_FILE_PATH, newline="", encoding="utf-8") as csv_file:
    raw_lines = csv_file.read().splitlines()

for line in raw_lines[1:]:
    sensor_id, reading_str, location = line.split(",")
    reading = float(reading_str)
    print(sensor_id, reading, location)

print()
print("read structured CSV with DictReader:")
with open(CSV_FILE_PATH, newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    rows = [row for row in reader]
    for row in rows:
        print(row["id"], row["temperature"], row["location"])

print()
print("aggregate counts and averages from the CSV data:")
summary = {}
for row in rows:
    sensor_id = row["id"]
    temperature = float(row["temperature"])
    if sensor_id not in summary:
        summary[sensor_id] = {"count": 0, "total": 0.0}
    summary[sensor_id]["count"] += 1
    summary[sensor_id]["total"] += temperature

for sensor_id, stats in summary.items():
    avg = stats["total"] / stats["count"]
    print(sensor_id, "count=", stats["count"], "avg=", f"{avg:.2f}")

print()
print(f"write aggregate CSV output to {SUMMARY_FILE_PATH.name}:")
with open(SUMMARY_FILE_PATH, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "count", "avg_temp"])
    writer.writeheader()
    for sensor_id, stats in summary.items():
        avg = stats["total"] / stats["count"]
        writer.writerow({
            "id": sensor_id,
            "count": stats["count"],
            "avg_temp": f"{avg:.2f}",
        })

print("done")
