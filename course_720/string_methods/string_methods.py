# A String is just a series of characters

name = input("Enter your full name: ")

# The LENGTH function will give you the length of the string ---> len()
len_result = len(name)  # store the len() within a variable
print(len_result)

# The FIND Method ---> .find()
# The first occurrence/first position of a given character
find_result = name.find(" ")  # this will return the position of the FIRST space in the user's input
print(find_result)
# To find the last occurrence ---> .rfind()
last_result = name.rfind(" ")  # this will return the position of the LAST space in the user's input
print(last_result)
# NOTE: If there is no occurrence in the string, then it will return negative one (-1)


# The CAPITALIZATION Method ---> .capitalize()
# To capitalize the firs letter in the string
cap_name = name.capitalize()
print(cap_name)  # this only capitalizes the first letter of the string

# The UPPER Method ---> .upper()
upper_name = name.upper()
print(upper_name)

# The LOWER Method ---> .lower()
lower_name = name.lower()
print(lower_name)

# The ISDIGIT Method ---> .isdigit()
# Will return a boolean true or false if ths String contains only digits
digits_only = name.isdigit()
print(digits_only)
#NOTE: Only returns true if it's only digits in the string (THERE CAN BE NO SPACES EITHER)

# The ISALPHA Method ---> .isalpha()
# Will return a boolean true or false if ths String contains only alphabetical characters
alpha_only = name.isalpha()
print(alpha_only)
#NOTE: Spaces in the String will result in false

phone_number = input("Enter your phone #: ")

# The COUNT Method ---> .count()
# Count how many characters are in the String
count_phone = phone_number.count("-")
print(f"There are {count_phone} dashes in the phone number")

# The REPLACE Method ---> .replace("old", "new")
# Replace any occurrence of one character with another
replace_phone = phone_number.replace("-", " ")
print(replace_phone, "---> The dashes have been replaced with spaces")

# A Comprehensive list of all the String Methods available
print(help(str))


