"""Python refresher: object-oriented programming with temperature measurements."""

import csv

class TemperatureMeasurement:
    """A single temperature measurement event."""

    def __init__(self, value_celsius, timestamp, quality="good"):
        self.value_celsius = value_celsius
        self.timestamp = timestamp
        self.quality = quality

    @classmethod
    def from_fahrenheit(cls, value_fahrenheit, timestamp, quality="good"):
        celsius = (value_fahrenheit - 32) * 5 / 9
        return cls(celsius, timestamp, quality=quality)

    def to_celsius(self):
        return self.value_celsius

    def to_fahrenheit(self):
        return self.value_celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.value_celsius + 273.15

    def is_valid(self):
        return self.value_celsius is not None and self.quality == "good"

    def describe(self, sensor_unit="C"):
        if sensor_unit == "F":
            value = self.to_fahrenheit()
            unit = "F"
        elif sensor_unit == "K":
            value = self.to_kelvin()
            unit = "K"
        else:
            value = self.to_celsius()
            unit = "C"

        return f"{self.timestamp}: {value:.1f}{unit} ({self.quality})"

    def to_dict(self, sensor_unit="C"):
        return {
            "timestamp": self.timestamp,
            "value": round(self.to_fahrenheit() if sensor_unit == "F" else self.to_celsius(), 2),
            "unit": sensor_unit,
            "quality": self.quality,
        }

    def is_anomaly(self, low=-20.0, high=80.0):
        return not (low <= self.value_celsius <= high)


class Sensor:
    """A temperature sensor that stores measurements and supports simple analysis."""

    def __init__(self, sensor_id, location, unit="C"):
        self.sensor_id = sensor_id
        self.location = location
        self.unit = unit
        self.measurements = []

    def add_measurement(self, measurement):
        """Store a TemperatureMeasurement object."""
        if not isinstance(measurement, TemperatureMeasurement):
            raise TypeError("measurement must be TemperatureMeasurement")
        self.measurements.append(measurement)

    def latest(self):
        return self.measurements[-1] if self.measurements else None

    def average(self):
        valid_values = [m.value_celsius for m in self.measurements if m.is_valid()]
        if not valid_values:
            return None
        average_c = sum(valid_values) / len(valid_values)
        return average_c if self.unit == "C" else average_c * 9 / 5 + 32

    def filter_measurements(self, min_value=None, max_value=None):
        results = []
        for measurement in self.measurements:
            value = measurement.to_fahrenheit() if self.unit == "F" else measurement.to_celsius()
            if min_value is not None and value < min_value:
                continue
            if max_value is not None and value > max_value:
                continue
            results.append(measurement)
        return results

    def _stats(self):
        values = [m.value_celsius for m in self.measurements if m.is_valid()]
        if not values:
            return None, None
        mean = sum(values) / len(values)
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        return mean, variance ** 0.5

    def anomalies(self, low=-20.0, high=80.0, z_threshold=2.0):
        mean, std = self._stats()
        results = []
        for m in self.measurements:
            if m.quality != "good" or m.is_anomaly(low, high):
                results.append((m, None))
                continue

            if mean is not None and std and std > 0:
                z_score = abs((m.value_celsius - mean) / std)
                if z_score > z_threshold:
                    results.append((m, z_score))

        return results

    def export_to_csv(self, file_path):
        fieldnames = ["timestamp", "value", "unit", "quality"]
        with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for measurement in self.measurements:
                writer.writerow(measurement.to_dict(sensor_unit=self.unit))

    def __repr__(self):
        return f"Sensor(id={self.sensor_id!r}, location={self.location!r}, unit={self.unit!r})"

    def __str__(self):
        return f"Sensor {self.sensor_id} at {self.location} ({self.unit})"


# Create sensors
sensor_a = Sensor("S-101", "cleanroom", unit="C")
sensor_b = Sensor("S-102", "test bench", unit="F")

# Create measurements
m1 = TemperatureMeasurement(22.5, "2026-05-02 10:00")
m2 = TemperatureMeasurement(23.0, "2026-05-02 10:05")
m3 = TemperatureMeasurement(22.8, "2026-05-02 10:10")
m4 = TemperatureMeasurement(22.9, "2026-05-02 10:12")
m5 = TemperatureMeasurement(23.1, "2026-05-02 10:14")
m6 = TemperatureMeasurement(80.0, "2026-05-02 10:15")
m7 = TemperatureMeasurement.from_fahrenheit(75.2, "2026-05-02 10:20")
m8 = TemperatureMeasurement(100.0, "2026-05-02 10:25", quality="suspect")

# Add measurements to sensors
sensor_a.add_measurement(m1)
sensor_a.add_measurement(m2)
sensor_a.add_measurement(m3)
sensor_a.add_measurement(m4)
sensor_a.add_measurement(m5)
sensor_a.add_measurement(m6)
sensor_b.add_measurement(m7)
sensor_b.add_measurement(m8)

print(sensor_a)
print("latest:", sensor_a.latest().describe(sensor_unit=sensor_a.unit))
print("average:", f"{sensor_a.average():.1f}{sensor_a.unit}")
print(sensor_b)
print("latest:", sensor_b.latest().describe(sensor_unit=sensor_b.unit))
print("average:", f"{sensor_b.average():.1f}{sensor_b.unit}")

# Filter measurements by value
warm_readings = sensor_a.filter_measurements(min_value=22.0)
print("warm readings for sensor_a:")
for reading in warm_readings:
    print(" -", reading.describe(sensor_unit=sensor_a.unit))

# Show anomalies for sensor_a
print("anomalies for sensor_a:")
for anomaly, z_score in sensor_a.anomalies():
    if z_score is None:
        print(" -", anomaly.describe(sensor_unit=sensor_a.unit), "(quality/fixed-range anomaly)")
    else:
        print(f" - {anomaly.describe(sensor_unit=sensor_a.unit)} (z={z_score:.2f})")

# Show anomalies for sensor_b
print("anomalies for sensor_b:")
for anomaly, z_score in sensor_b.anomalies():
    if z_score is None:
        print(" -", anomaly.describe(sensor_unit=sensor_b.unit), "(quality/fixed-range anomaly)")
    else:
        print(f" - {anomaly.describe(sensor_unit=sensor_b.unit)} (z={z_score:.2f})")

# Export measurements to CSV
sensor_a.export_to_csv("sensor_S-101.csv")
sensor_b.export_to_csv("sensor_S-102.csv")
print("Exported sensor data to CSV files")
