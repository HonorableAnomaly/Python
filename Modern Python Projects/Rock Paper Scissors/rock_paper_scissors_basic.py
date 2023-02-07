# My attempt
print("rock.....")
print("paper.....")
print("scissors.....")

print("Pick yer poison!")
p1_choice = input()
print(p1_choice)
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")
print("           ")
print("NO CHEATING")

print("Pick yer poison!")
p2_choice = input()
print("SHOOT, y'all!")
print(p2_choice)

win_1 = "Dagum! Player One is a sharpshooter!"
win_2 = "Dagum! Player Two is a sharpshooter!"

if p1_choice == p2_choice:
    print("It's a DRAW, varmint!")
elif p1_choice == "rock" and p2_choice == "scissors":
    print(win_1)
elif p1_choice == "rock" and p2_choice == "paper":
    print(win_2)
elif p1_choice == "paper" and p2_choice == "rock":
    print(win_1)
elif p1_choice == "paper" and p2_choice == "scissors":
    print(win_2)
elif p1_choice == "scissors" and p2_choice == "rock":
    print(win_2)
elif p1_choice == "scissors" and p2_choice == "paper":
    print(win_1)
else:
    print("Come on now! Don't be a yella-belly!")

# The solution
