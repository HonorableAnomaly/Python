# 2 ways to import random

# import random
from random import randint

print("rock.....")
print("paper.....")
print("scissors.....")

print("Pick yer poison!")
p1_choice = input().lower()
print(p1_choice)

rand_num = randint(0, 2)  # random.randint if using first import option
print("SHOOT, y'all!")
if rand_num == 0:
    comp_choice = "rock"
elif rand_num == 1:
    comp_choice = "paper"
else:
    comp_choice = "scissors"
print(f"Computer plays: {comp_choice}")

win_1 = "Dagum! Player One's a sharpshooter!"
win_2 = "Dagum! This here compy's a sharpshooter!"

if p1_choice == comp_choice:
    print("It's a DRAW, varmint!")
elif p1_choice == "rock":
    if comp_choice == "scissors":
        print(win_1)
    else:
        print(win_2)
elif p1_choice == "paper":
    if comp_choice == "rock":
        print(win_1)
    else:
        print(win_2)
elif p1_choice == "scissors":
    if comp_choice == "paper":
        print(win_1)
    else:
        print(win_2)
else:
    print("Come on now! Don't be a yella-belly!")
