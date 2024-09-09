# Logical Operators - evaluate multiple conditions (or, and, not)
#                                                  or = at least one condition must be True
#                                                  and = both conditions must be True
#                                                  not = inverts the condition (not False, not True)

#Outdoor Event (using logical operators)
temp = 83
is_raining = False
#If the temperature is too hot, too cold or it's raining, then the outdoor event will be cancelled
#Check using an if statement

if temp > 98 or temp < 69 or is_raining:
    print("The outdoor event has been postponed")
else:
    print("The outdoor event is still scheduled")