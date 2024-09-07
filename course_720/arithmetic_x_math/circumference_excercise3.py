#Exercise 3: Circumference Calc
import math

#C = 2 * pi * r
radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
trunc_circumference = round(circumference)

# We can also truncate the circumference
# ---> print(f"The circumference is: {round(circumference)}")

print(f"The circumference is: {circumference}")
print(f"The circumference (truncated) is: {trunc_circumference}")


