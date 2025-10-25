print("Metric Conversion Tool")
print("-"*30)

print("User Instructions:")

print("1. Enter the value you want to convert.")
print("2. Enter the unit you want to convert from (cm, m, km, in, ft, yd, mi).")
print("3. Enter the unit you want to convert to (cm, m, km, in, ft, yd, mi).")
print("-"*30)

answer = input("Enter the value you want to convert:    ")

value = float(answer)
unit = input("Enter the unit you want to convert from (cm, m, km, in, ft, yd, mi):    ").lower()
target_unit = input("Enter the unit you want to convert to (cm, m, km, in, ft, yd, mi):    ").lower()

if unit == "cm":
    if target_unit == "m":
        converted_value = value / 100
    elif target_unit == "km":
        converted_value = value / 100000
    elif target_unit == "in":
        converted_value = value / 2.54
    elif target_unit == "ft":
        converted_value = value / 30.48
    elif target_unit == "yd":
        converted_value = value / 91.44
    elif target_unit == "mi":
        converted_value = value / 160934
    else:
        converted_value = value
elif unit == "m":
    if target_unit == "cm":
        converted_value = value * 100
    elif target_unit == "km":
        converted_value = value / 1000
    elif target_unit == "in":
        converted_value = value * 39.3701
    elif target_unit == "ft":
        converted_value = value * 3.28084
    elif target_unit == "yd":
        converted_value = value * 1.09361
    elif target_unit == "mi":
        converted_value = value / 1609.34
    else:
        converted_value = value
elif unit == "km":
    if target_unit == "cm":
        converted_value = value * 100000
    elif target_unit == "m":
        converted_value = value * 1000
    elif target_unit == "in":
        converted_value = value * 39370.1
    elif target_unit == "ft":
        converted_value = value * 3280.84
    elif target_unit == "yd":
        converted_value = value * 1093.61
    elif target_unit == "mi":
        converted_value = value / 1.60934
    else:
        converted_value = value
elif unit == "in":
    if target_unit == "cm":
        converted_value = value * 2.54
    elif target_unit == "m":
        converted_value = value / 39.3701
    elif target_unit == "km":
        converted_value = value / 39370.1
    elif target_unit == "ft":
        converted_value = value / 12
    elif target_unit == "yd":
        converted_value = value / 36
    elif target_unit == "mi":
        converted_value = value / 63360
    else:
        converted_value = value
elif unit == "ft":
    if target_unit == "cm":
        converted_value = value * 30.48
    elif target_unit == "m":
        converted_value = value / 3.28084
    elif target_unit == "km":
        converted_value = value / 3280.84
    elif target_unit == "in":
        converted_value = value * 12
    elif target_unit == "yd":
        converted_value = value / 3
    elif target_unit == "mi":
        converted_value = value / 5280
    else:
        converted_value = value
elif unit == "yd":
    if target_unit == "cm":
        converted_value = value * 91.44
    elif target_unit == "m":
        converted_value = value / 1.09361
    elif target_unit == "km":
        converted_value = value / 1093.61
    elif target_unit == "in":
        converted_value = value * 36
    elif target_unit == "ft":
        converted_value = value * 3
    elif target_unit == "mi":
        converted_value = value / 1760
    else:
        converted_value = value
elif unit == "mi":
    if target_unit == "cm":
        converted_value = value * 160934
    elif target_unit == "m":
        converted_value = value * 1609.34
    elif target_unit == "km":
        converted_value = value * 1.60934
    elif target_unit == "in":
        converted_value = value * 63360
    elif target_unit == "ft":
        converted_value = value * 5280
    elif target_unit == "yd":
        converted_value = value * 1760
    else:
        converted_value = value
else:
    converted_value = value

print(f"{value} {unit} is equal to {converted_value} {target_unit}")