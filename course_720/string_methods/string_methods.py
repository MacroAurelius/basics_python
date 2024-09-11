# A String is just a series of characters

name = input("Enter your full name: ")

# The LENGTH function will give you the length of the string ---> len()
len_result = len(name)  # store the len() within a variable
print(len_result)

# FIND Method ---> .find()
# The first occurrence/first position of a given character
find_result = name.find(" ")  # this will return the position of the FIRST space in the user's input
print(find_result)
# To find the last occurrence ---> .rfind()
last_result = name.rfind(" ")  # this will return the position of the LAST space in the user's input
print(last_result)
# NOTE: If there is no occurrence in the string, then it will return negative one (-1)

