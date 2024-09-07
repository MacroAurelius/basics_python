#Area of a Circle
import math

#A = pi * r^2
radius = float(input("Enter the radius of a circle: "))

#This is one way to raise to the power of 2
area = math.pi * radius**2

# This is another way using the pow() built in function
# area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area,2)}cm^2")
