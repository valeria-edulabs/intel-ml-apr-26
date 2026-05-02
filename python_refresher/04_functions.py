"""Python refresher: functions."""

# Basic function
def format_reading(sensor_name, reading):
    """Return a formatted sensor reading message."""
    return f"{sensor_name}: {reading:.2f} units"

print(format_reading("SensorA", 12.345))

# Default and keyword arguments
def power(status="off", level=1):
    return f"power={status}, level={level}"

print(power())
print(power(status="on", level=3))

# *args and **kwargs
def summarize(name, *values, **options):
    total = sum(values)
    label = options.get("label", name)
    return f"{label}: {total} (count={len(values)})"

print(summarize("temps", 21.2, 22.0, 23.5))
print(summarize("temps", 21.2, 22.0, label="three temps"))

# Lambda expression
double = lambda x: x * 2
print(double(7))

# Lambda with filter/map
values = [10, 15, 20, 25, 30]
print("even values:", list(filter(lambda x: x % 2 == 0, values)))
print("scaled values:", list(map(lambda x: x * 1.5, values)))

# Function used as a helper
def apply_to_all(values, func):
    return [func(value) for value in values]

numbers = [1, 2, 3]
print(apply_to_all(numbers, lambda x: x + 10))
