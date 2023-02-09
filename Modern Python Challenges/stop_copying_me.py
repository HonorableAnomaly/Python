# my attempt

# print("Hey, how's it going?")
# copy = input()
# while copy == "":
#     if copy == "stop copying me":
#         print("Alright, you win. Please forgive me.")
#     else:
#         input(copy)

# the solution
# msg = input("Hey, how's it going?")

# while msg != "stop copying me":
#     print(msg)
#     msg = input()
# print("Alright, you win. Please forgive me.")

# the solution refactored
msg = input("Hey, how's it going?")

while msg != "stop copying me":
    msg = input(f"{msg}\n")
print("Alright, you win. Please forgive me.")
