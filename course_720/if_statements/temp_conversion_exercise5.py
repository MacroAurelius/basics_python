# Exercise 5: Temperature Conversion

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))
degree_symbol = "\u00b0"

# While creating if statements, you can use the keyword PASS to be a space filler until you set the condition
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}{degree_symbol}F")
elif unit == "F":
    pass
else:
    print(f"{unit} is an invalid unit of measurement")