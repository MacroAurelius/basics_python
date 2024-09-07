# Variable = a container for a value (string, integer, float, boolean)
#            a variable behaves as if it was the value it contains

#Strings Examples
first_name = "Shaquille Sunflower"

print(first_name)
nickname = "Martin Payne"

# You can use a varaible with text by using an f-string
# ---> begin a string with f or F before the opening quotation mark. Inside this string, you can write a Python expression between a pair of    {  } that can refer to variables or literal values

print(f"Hey, my name is {first_name}, but my friends call me {nickname}")
# the f-string is very useful

# Another f-string example
school = "Massachusetts Institute of Technology"

print(f"Hey everyone, my name is {first_name} and I attend {school}!")

color = "black"
sec_color = "yellow"

print(f"I like to see the colors {color} and {sec_color} together!")

#Integer Examples
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Integers do not use quotes

#Float Examples (floating point number has a decimal)
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance}km")


#Boolean (True or False)
#---> Booleans only have two options True or False)
is_student = True

print(f"Are you a student?: {is_student}")

# Booleans are not normally printed directly, they are used in internally in a program e.g. if statements use Booleans

if is_student:
    print("You are a student!")
else:
    print("You are NOT a student")

if gpa > 3.0:
    print("You have an above average GPA. Keep up the good work!")
else:
    print("Get to work and get those grades up!")



