# Typecasting is the process of converteing a variable from one data type to another
#             str(), int(), float(), bool()


name = "Cupahnoodle"
platform = "Twitch"
viewers = 1300
live_time = 2.5
subscribers = 15000
is_online = True

# To get the data type of a variable/value use the type function ---> type(variable)
print(type(name))
print(type(platform))
print(type(viewers))
print(type(subscribers))
print(type(is_online))

# Using these type cast unctions ---> str(), int(), float(), bool() --- we can convert to one data type to another

# converting from a float to a integer
live_time_int = int(live_time)
print(live_time)
print(live_time_int)

# converting from an integer to a float
subscribers_float = float(subscribers)
print(subscribers)
print(subscribers_float)

# converting int() to str()
viewers_str = str(viewers)
print(viewers_str)
print(type(viewers))
print(type(f"Type String: {viewers_str}"))
