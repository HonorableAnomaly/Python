# My attempt
# SUCCESS!!!
print("Oh, you want entry into the hottest nightclub in the city?")
answer = input()
if answer[0] == "n":
    print("Get lost, kid.")
else:
    print("Lemme see some identification...")

age = input()
if age >= "18" and age <= "20":
    print("Here's your wristband. NO drinks.")
elif age >= "21":
    print("You're good.")
else:
    print("Get outta here!")

# Solution
age = input("How old are you?")
if age:  # nested conditionals
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband.")
    elif age >= 21:
        print("You are good to enter and can drink!")
    else:
        print("You can't come in, little one :(")
else:
    print("Please enter.")
