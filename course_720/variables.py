# Variable = a container for a value (string, integer, float, boolean)
#            a variable behaves as if it was the value it contains


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