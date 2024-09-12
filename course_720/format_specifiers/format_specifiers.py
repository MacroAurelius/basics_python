# Format Specifiers (when use in the context of an f-string) = {value:flags} format a value based on what flags are inserted
# USES:
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left just
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place a sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

#PRACTICE
price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 34.654345
price5 = 55.44543543432

# .(number)f = round to that many decimal places (fixed point)
print(".(number)f = round to that many decimal places (fixed point)")
print(f"Price 1 is ${price1:.2f}")  #After the : is called a flag. It will format the value a specific way, depending on what you place there
print(f"Price 2 is ${price2:.2f}")  #Decimal point precision with 2 decimal places
print(f"Price 3 is ${price3:.1f}")  #For 1 decimal places
print(f"Price 4 is ${price4:.3f}")  #For 3 decimal places

# :(number) = allocate that many spaces
print("\n:(number) = allocate that many spaces")
print(f"Price 5 is ${price5:30}")
print(f"Price 5 is ${price5:030}") #Padding with 0s

# :< = left just (NOTE: ADDS UNIFORM SPACE AT THE END)
print("\n:< = left just")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
# :> = right justify
print(":> = right justify")
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price1:>10}")
# :^ = center align
print(":^ = center align")
print(f"Price 1 is ${price1:^30}")
print(f"Price 2 is ${price2:^10}")

