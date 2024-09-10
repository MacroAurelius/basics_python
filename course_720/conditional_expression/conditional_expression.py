# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 5
#Checking to see if the number is positive
print("Positive" if num > 0 else "Negative")

#Check to see if the number is Even or Odd
num2 = 9
print(f"{num2} is EVEN" if num2 % 2 == 0 else f"{num2} is ODD")

#Or you can ASSIGN the condition
num3 = 6
result = "EVEN" if num3 % 2 == 0 else "ODD"
print(f"{num3} is {result}")