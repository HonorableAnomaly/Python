# My attempt
print("rock.....")
print("paper.....")
print("scissors.....")

print("Player One, Pick yer poison!")
p1_choice = input()
print(p1_choice)
print("NO CHEATING\n\n" * 20)

print("Player Two, Pick yer poison!")
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
# print("rock.....")
# print("paper.....")
# print("scissors.....")

# player_1 = input("Player One, make your move:")
# print("NO CHEATING\n\n" * 20)
# player_2 = input("Player Two, make your move:")

# if player_1 == player_2:
#     print("It's a DRAW, varmint!")
# elif player_1 == "rock" and player_2 == "scissors":
#     print("Player One wins!")
# elif player_1 == "rock" and player_2 == "paper":
#     print("Player Two wins!")
# elif player_1 == "paper" and player_2 == "rock":
#     print("Player One wins!")
# elif player_1 == "paper" and player_2 == "scissors":
#     print("Player Two wins!")
# elif player_1 == "scissors" and player_2 == "rock":
#     print("Player Two wins!")
# elif player_1 == "scissors" and player_2 == "paper":
#     print("Player One wins!")

# if player_1 == player_2:
#     print("It's a tie!")
# else:
#     print("Something went wrong...")

# The solution: Refactored
# print("rock.....")
# print("paper.....")
# print("scissors.....")

# player_1 = input("Player One, make your move:")
# print("NO CHEATING\n\n" * 20)
# player_2 = input("Player Two, make your move:")

# if player_1 == player_2:
#     print("It's a tie!")
# elif player_1 == "rock":
#     if player_2 == "scissors":
#         print("Player One wins!")
#     elif player_2 == "paper":
#         print("Player Two wins!")
# elif player_1 == "paper":
#     if player_2 == "rock":
#         print("Player One wins!")
#     elif player_2 == "scissors":
#         print("Player Two wins!")
# elif player_1 == "scissors":
#     if player_2 == "rock":
#         print("Player Two wins!")
#     elif player_2 == "paper":
#         print("Player One wins!")
# else:
#     print("Something went wrong...")

# SUPER CLEAN SOLUTION
# No error handling
# p1 = input("Player 1: rock, paper, or scissors ")
# p2 = input("Player 2: rock, paper, or scissors ")

# if p1 == p2:
#     print("Draw")
# elif p1 == "rock" and p2 == "scissors":
#     print("p1 wins")
# elif p1 == "paper" and p2 == "rock":
#     print("p1 wins")
# elif p1 == "scissors" and p2 == "paper":
#     print("p1 wins")
# else:
#     print("p2 wins")
