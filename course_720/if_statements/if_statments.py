# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

#Example:
# ----> In order to apply for this particular credit card, the applicant has to be 18 yrs old or older
if age >= 100:
    print("Sorry, you are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:  #you can also add an else-if statement in between
    print("You haven't been born yet!!!")
else:
    print("You must be 18+ to sign up.")

# *** Be careful where you place your if statements. It wouldn't operate correctly if age >= 100 was lower in the list *** #

response = input("Would you like food? (Y/N): ")

#For comparisons use double equal "==" and triple equal "===" a more concrete comparison operator
if response == "Y":
    print("Here, have some food!")
else:
    print("No food for you.")

#Example of a text field being left blank
adding_name = input("Enter your name: ")
name = adding_name

if name == "":
    print("You did not type in your name")
else:
    print(f"Good day, {name}!")

#TODO How can i make it where if the user doesn't type anything, then it will print the statement and prompt you to try again

