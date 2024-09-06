import math

friends = 0

friends = friends + 1
friends += 15 #Augmented Assignment Operator
friends = friends - 1
friends -= 1 #Augmented Assignment Operator
friends *= 3
friends /= 2
friends **= 2 # Exponentiation
remainder = friends % 2 # Modulus

print(friends)
print(remainder)

#Built in Math related options

x = 3.14
y = 4
z = 5

#Round Functions: round(number, ndigits)
round_result = round(x)
print(f"The round for x is: {round_result}")

#Absolute Value Functions: abs(__x)
y = -4
absolute_result = abs(y)
print(f"The absolute value of y is: {absolute_result}")

#Power Function: pow(base, exponent, mod)
power_result = pow(4, 3)

#Max Function: max()
max_result = max(x, y, z)
print(f"The maximum value between x, y, and z is: {max_result}")

#Minimum Function: min()
min_result = min(x, y, z)
print(f"The minimum value btween x. y, and z is: {min_result}")

