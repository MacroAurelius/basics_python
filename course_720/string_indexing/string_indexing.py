# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step] (We can access a staring point, an end point, or points at each step)

credit_number = "1234-5678-9012-3456"

# Note: that the index count starts at 0 (example below)
print(f"Index 0 is the first character of the string. Which is: {credit_number[0]}")
print(f"The second: {credit_number[1]}")
print(f"The third: {credit_number[2]}")
print(f"At the ninth index of the card number: {credit_number[9]}")

# With the Indexing Operator there are up to 3 fields that we can fill in [start:end:step]
# If there is only one index listed without any colons : , then it will assume youre filling in the start position

# Print out the first 4 digits of the string/credit card number
print(f"Here are the first 4 digits of the card number: {credit_number[0:4]}")
# You can also type it as ---> credit_number[:4] <--- even though there isn't a starting index, it will assume to start from the beginning of the string

# Print out the next 4 digits
print(f"The next 4 digits of the card are: {credit_number[5:9]}")

# To print the rest of the card number use the end indexing field ---> variable[start:] (just add the start point and the colon
print(f"The remaining digits are: {credit_number[9:].replace("-", " ")}")
# Note: I removed the dashes

# You can also use negative numbers as the index for the string to index backwards
# If you need the last character of a string use -1
print(f"The last character in the card number is: {credit_number[-1]}")

print(f"The second to last character in the card number is: {credit_number[-2]}")
print(f"The last 2 digits character in the card number is: {credit_number[-2:]}")

# Using the step field we can access the characters in a string by a given step (you can count y 2's, 3's etc.)
# NOTE: While using the step field you have to write it out as such ---> [::] (USE TWO COLONS for start and end fields
print(f"Every 2nd character of the card number is: {credit_number[::2]}") # This will print every 2nd character of the string
print(f"Every 3rd character of the card number is: {credit_number[::3]}")

# Example: Get the last 4 digits of the card number
last_digits = credit_number[-4:]
print(f"Last 4 digits visible: XXXX-XXXX-XXXX-{last_digits}")

print(f"All digits visible: {credit_number}")

# Example: Reverse the characters in card number
print(f"The card number backwards is: {credit_number[::-1]}")

