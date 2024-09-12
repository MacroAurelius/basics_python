# Validate User Input Exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Create a Username: ")

# 1.
if len(username) > 12:
    print("Username must be no longer than 12 characters")
# 2.
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
# 3.
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}, you are signed up")
