"""Python refresher: collections."""

# Lists
temperatures = [21.0, 22.5, 23.1, 20.8]
print("first temp:", temperatures[0])
print("slice:", temperatures[1:3])
temperatures.append(24.0)
print("after append:", temperatures)

# Tuples
point = (10, 20)
x, y = point
print("tuple unpack:", x, y)

# Sets
tags = {"sensor", "temperature", "outdoor"}
more_tags = {"temperature", "indoor", "humidity"}
print("unique tags:", tags)
print("add a tag:", tags | {"pressure"})
print("intersection:", tags & more_tags)
print("difference:", tags - more_tags)
print("is subset?:", {"sensor", "temperature"} <= tags)
print("union of sets:", tags.union(more_tags))

# Modify set contents
tags.add("pressure")
tags.discard("outdoor")
print("after add/discard:", tags)

# Dictionaries
sensor = {
    "id": "S001",
    "location": "lab",
    "active": True,
}
print("sensor id:", sensor["id"])
print("keys:", list(sensor.keys()))
print("items:", list(sensor.items()))

# Nested collections
nested_list = [[1, 2], [3, 4], [5, 6]]
print("nested list:", nested_list)
print("first inner list second value:", nested_list[0][1])

nested_dict = {
    "S001": {"location": "lab", "readings": [21.0, 22.5]},
    "S002": {"location": "field", "readings": [19.8, 20.2]},
}
print("nested dict:", nested_dict)
print("S001 readings:", nested_dict["S001"]["readings"])

mixed = {
    "sensor_ids": ["S001", "S002"],
    "active_tags": {"temperature", "indoor"},
    "metadata": {"owner": "team-a", "count": 2},
}
print("mixed nested collection:", mixed)
print("active tags contains temperature?", "temperature" in mixed["active_tags"])

# Iteration patterns
for temp in temperatures:
    print("temp:", temp)

for key, value in sensor.items():
    print(key, "=", value)
