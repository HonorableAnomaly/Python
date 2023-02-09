# My attempt

# x = 0
# for x in range(1, 21):
#     if x == 4 or x == 13:
#         print(f"{x} is UNLUCKY!")
#     elif x == 7:
#         print(f"{x} is LUCKY!!!")
#     elif x % 2 == 0:
#         print(f"{x} is even.")
#     else:
#         print(f"{x} is odd.")

# The solution
# for num in range(1, 21):
#     if num == 4 or num == 13:
#         print(f"{num} is UNLUCKY!")
#     elif num == 7:
#         print(f"{num} is LUCKY!")
#     elif num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")

# Solution refactored
for num in range(1, 21):
    if num == 4 or num == 13:
        state = "UNLUCKY!"
    elif num == 7:
        state = "LUCKY!!!"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}.")
