"""Python refresher: control flow."""

scores = [78, 92, 85, 61, 99]

# Conditional logic
for score in scores:
    if score >= 90:
        level = "excellent"
    elif score >= 80:
        level = "good"
    elif score >= 70:
        level = "okay"
    else:
        level = "needs improvement"
    print(score, "->", level)

# While loop
counter = 0
while counter < 3:
    print("repeat", counter)
    counter += 1

# break / continue
for item in [10, 0, 5, 3]:
    if item == 0:
        print("skip zero")
        continue
    if item > 5:
        print("stop at", item)
        break
    print("item", item)

# enumerate and zip
names = ["sensorA", "sensorB", "sensorC"]
values = [12.3, 15.1, 9.8]
for index, name in enumerate(names, start=1):
    print(index, name)

for name, value in zip(names, values):
    print(name, "=>", value)
