"""Python refresher: errors and exception handling."""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
CSV_FILE_PATH = DATA_DIR / "temperature_readings.csv"


def parse_temperature(row):
    """Parse a temperature row and validate its fields."""
    try:
        sensor_id = row["id"]
        temperature = float(row["temperature"])
        location = row["location"]
    except KeyError as exc:
        raise ValueError(f"missing required column: {exc.args[0]}") from exc
    except ValueError as exc:
        raise ValueError(f"invalid temperature value: {row.get('temperature')}") from exc

    if sensor_id == "":
        raise ValueError("sensor id cannot be empty")

    return sensor_id, temperature, location


def load_measurements(path):
    """Load measurements from a CSV file with error handling."""
    measurements = []
    try:
        with open(path, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    record = parse_temperature(row)
                    measurements.append(record)
                except ValueError as exc:
                    print("Skipping invalid row:", exc)
    except FileNotFoundError:
        print(f"CSV file not found: {path}")
    except PermissionError:
        print(f"No permission to read file: {path}")
    else:
        print(f"Loaded {len(measurements)} valid measurements")
    finally:
        print("Finished reading CSV file")

    return measurements


def validate_sensor_id(sensor_id):
    if not isinstance(sensor_id, str):
        raise TypeError("sensor_id must be a string")
    if not sensor_id.startswith("S"):
        raise ValueError("sensor_id must start with 'S'")
    return True


if __name__ == "__main__":
    print("=== exception handling demo ===")

    measurements = load_measurements(CSV_FILE_PATH)
    print()

    print("validate sensor IDs:")
    for sensor_id, temperature, location in measurements:
        try:
            validate_sensor_id(sensor_id)
            print(f"{sensor_id} is valid")
        except (TypeError, ValueError) as exc:
            print(f"invalid sensor id {sensor_id!r}:", exc)

    print()
    print("demonstrate explicit raise:")
    try:
        validate_sensor_id(123)
    except Exception as exc:
        print("caught exception:", type(exc).__name__, exc)
