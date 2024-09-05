# input() = A function that prompts the user to enter datat
#           Returns the entered data as a string

name = input("What is your name?: ")

# We can assign an input to a variable
favorite_color = input("What is your favorite color?: ")

# We can then use the assigned variable to perform actions as needed
# print(f"Your favorite color is: {favorite_color}.")

print(f"Hi {name}! It's nice to know that your favorite color is {favorite_color}.")

# Using input with Integers
# It may be necessary to type cast the input if an integer is involved

age = input("How old are you?: ")

###**** age += 1 # this causes a type error because you can only concatenate a str (not "int") to str ****###
print(age) # Here, age is currently a string due to the input

# To change that, type cast to convert the input's string to an integer
age_convert = age
age_convert = int(age_convert)
age_convert += 1
print(f"You have now converted your age from {age} to {age_convert}. CONGRATULATIONS!")

# You also can type cast your user input
pieces_of_gum = int(input("How many pieces of gum do you have left? "))
#share = input("May I have a piece? ")
pieces_of_gum -= 1

print(f"Now you have {pieces_of_gum} pieces of gum left because I took one. :)")
