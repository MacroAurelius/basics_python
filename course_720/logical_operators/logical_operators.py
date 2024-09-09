# Logical Operators - evaluate multiple conditions (or, and, not)
#                                                  or = at least one condition must be True
#                                                  and = both conditions must be True
#                                                  not = inverts the condition (not False, not True)

#Outdoor Event (OR logical operators)
temp = int(input("What is the temperature for the day?: "))
degree_symbol = "\u00b0"

is_raining = False

#If the temperature is too hot, too cold or it's raining, then the outdoor event will be cancelled
#Check using an if statement

if temp > 98 or temp < 45 or is_raining:
    print(f"The temp is: {temp}. The outdoor event has been postponed.")
else:
    print(f"The temp is: {temp}. The outdoor event is still scheduled.")

#Outdoor Event (AND logical operators)
is_sunny = True

if temp >= 80 and is_sunny:
    print("It is sunny!")
    print("Be sure to bring sunscreen!")
elif temp <= 75 and is_sunny:
    print("It is quite chilly out today, bring a jacket as well.")
elif 79 > temp > 46 and is_sunny:
    print("It is warm outside")