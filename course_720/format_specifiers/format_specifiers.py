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

# .(number)f = round to that many decimal places (fixed point)
print(f"Price 1 is {price1:.2f}") #After the : is called a flag. It will format the value a specific way, depending on what you place there
print(f"Price 2 is {price2:.2f}") #Decimal point precision with 2 decimal places
print(f"Price 3 is {price3:.1f}") #For 1 decimal point

