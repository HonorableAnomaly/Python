from random import randint

# my attempt

# die1 = print(randint(1, 6))
# die2 = print(randint(1, 6))

# while die1 != 1 and die2 != 1:
#     die1 = print(randint(1, 6))
#     die2 = print(randint(1, 6))

# if die1 == 1 and die2 == 1:
#     print("SNAKE EYES!!!")
# elif die1 == die2:
#     print("A pair! Keep trying!")
# else:
#     print("Keep rollin' rollin' rollin' rollin' rollin'!")

# the solution

die1 = randint(1, 6)
die2 = randint(1, 6)
roll_count = 1

while die1 != 1 or die2 != 1:
    print(die1, die2)
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    roll_count += 1

print(die1, die2)
print("SNAKE EYES!!!")
print(f"It took {roll_count} rolls!")
