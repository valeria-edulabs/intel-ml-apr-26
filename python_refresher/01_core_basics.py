"""Python refresher: core basics."""


# Variables and values
count = 3
price = 12.50
name = "sensor"
is_active = True



print("count:", count)
print("price:", price)
print("name:", name)
print("active:", is_active)


# Type conversion
value = "42"
number = int(value)
print("converted number:", number, "type:", type(number))

# String formatting
temperature = 24.3
message = f"The current temperature is {temperature:.1f}°C"
print(message)

# Boolean expressions
x = 10
y = 5
print("x > y?", x > y)
print("x == y?", x == y)
print("x != y?", x != y)
print("truthiness:", bool([]), bool([1, 2, 3]), bool(0), bool(1))
