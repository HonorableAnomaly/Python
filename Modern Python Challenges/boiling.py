# my attempt

# f - 212
# c - 100
# k - 373

unit = input("What unit are you using (f, c, or k?) ")
# if unit != "f" or unit != "c" or unit != "k":
#     print("Nice try. That is not a measurement of heat!")
#     unit = input("What unit are you using (f, c, or k?) ")

temp = int(input("What temperature is the water? "))
# if int(temp) != True:
#     print("Wow. I didn't know that could be a temperature!")
#     temp = input("What temperature is the water? ")

boiling = "Your water is boiling!"

if unit == "f" and temp == "212":
    print(boiling)
elif unit == "c" and temp == "100":
    print(boiling)
elif unit == "k" and temp == "373":
    print(boiling)
else:
    print("Not yet...")


# the solution
# unit = input("What unit are you using (f, c, or k?) ")
# temp = int(input("What temperature is the water? "))

# if unit == "f":
#     if temp == "212":
#         print("Your water is boiling!")
#     else:
#         print("Not yet...")
# elif unit == "c":
#     if temp == "100":
#         print("Your water is boiling!")
#     else:
#         print("Not yet...")
# elif unit == "k":
#     if temp == "373":
#         print("Your water is boiling!")
#     else:
#         print("Not yet...")
# else:
#     print("Wow. I didn't know you could measure heat that way!")
#     print("Try again...")
