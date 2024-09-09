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

if temp > 100 or temp <= 32 or is_raining:
    print(f"The temp is: {temp}. The outdoor event has been postponed.")
else:
    print(f"The temp is: {temp}. The outdoor event is still scheduled.")

#Outdoor Event (AND logical operators)
is_sunny = True
#and
if temp >= 88 and is_sunny:
    print("It is hot outside!")
    print("It is sunny 🌞")
    print("Be sure to bring sunscreen!")
elif temp <= 33 and is_sunny:
    print("It is quite chilly out today, bring a jacket as well.")
    print("It is sunny 🌞")
elif 87 > temp >= 50 and is_sunny:
    print("It is warm outside")
    print("It is sunny 🌞")
#not
elif temp >= 88 and not is_sunny:
    print("It is hot outside!")
    print("It is cloudy ⛅")
elif temp <= 32 and not is_sunny:
    print("It is quite chilly out today.")
    print("It is cloudy ⛅")
elif 87 >= temp >= 50 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy ⛅")