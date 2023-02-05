name_here = input("Enter your name here: ")

# Input
# data = input("What's your favorite color?")
# print("You said " + data)

# Input #2
print("What's your favorite color?")
data = input()
print("You said " + data)

# Conditionals
# colons are important on conditionals in Python
name = "Charizard"
if name == "Charmander":
    print("Just you wait...")
elif name == "Charmeleon":
    print("One more second...")
else:
    print("Yeah baby! We've got Charizard!")

# Boolean
x = 1
x is 1  # Truthy
x is 0  # Falsy
# even without the x to prove, a 0 is inherent falsy while a 1 is inherent truthy

animal = input("Enter your favorite animal")
if animal:  # inherent truthy if anything exists
    print(animal + " is my favorite too! Jolly good!")
else:
    print("Please talk to me!")

# Comparison operators
1 == 1
1 == 2

1 != 3
1 != 1

color = "teal"
color != "purple"

3 > 1
4 < 2

# alphabetical ordering is called Lexigraphical

age = 18
age >= 13
if age >= 18:
    print("You have responsibilities!")
else:
    print("You have a paci!")

# Logical AND OR
# AND, OR, NOT
if drummer and has_drums:
    print("We got da beats!")

dating_age = 25
if dating_age > 20 and dating_age < 45:
    print("Let's date!")

city = input("Where do you live?")
if city == "San Diego" or city == "Los Angeles":
    print("You live in California!")
else:
    print("You live somewhere else")

if not is_weekend:
    print("Go to work")

child_age = 6
if not ((child_age >= 2 and child_age <= 8) or child_age >= 65):
    print("You pay normal rate!")
else:
    print("You are a child or senior")

# is vs. ==
a = 1
a == 1  # True
a is 1  # True

y = [1, 2, 3]
b = [1, 2, 3]
a == b  # True #checks values
a is b  # False #checks memory
