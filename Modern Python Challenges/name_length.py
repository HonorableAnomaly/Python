# My attempt
first_name = input("What is your first name?")
last_name = input("What is your last name?")

full_name = first_name + " " + last_name

if len(full_name) < 12:
    length = "shorter than"
elif len(full_name) == 12:
    length = "the exact length of"
else:
    length = "longer than"

print("*"*50)
print(f"{full_name} is {length} the average American name.")
print("*"*50)

# The solution
# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# name_length = len(first_name) + len(last_name)

# print("*"*50)
# if name_length == 12:
#     print(f"{first_name}{last_name} is exactly the average length of American names.")
# elif name_length < 12:
#     print(f"{first_name}{last_name} is shorter than the average length of American names.")
# else:
#     print(f"{first_name}{last_name} is longer than the average length of American names.")
# print("*"*50)
