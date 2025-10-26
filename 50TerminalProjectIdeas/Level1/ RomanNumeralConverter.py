print("Roman Numeral Converter")
print("-" * 30)

print("Enter a number between 1 and 3999 to convert it to a Roman numeral.")
num = int(input("Enter a number: "))

if num < 1 or num > 3999:
    print("Please enter a valid number between 1 and 3999.")
else:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    print(f"The Roman numeral is: {roman_numeral}")
    