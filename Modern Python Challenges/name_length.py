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

print("**********************************************")
print(f"{full_name} is {length} the average American name.")
print("**********************************************")
