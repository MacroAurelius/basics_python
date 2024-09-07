#Hypotenuse of a Right Triangle
import math

#Have the user input both the values of a and b
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

#To get c, raise a and b to the power of 2 pow() and use the square root func math.sqrt() to surround a & b
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {round(c, 2)}")

