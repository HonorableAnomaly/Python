print("How many kilometers did you complete today?")
# Takes user input
kms = input()
# Converts input to floated miles
miles = float(kms)/1.60934
# Rounds conversion to 2 deciaml places
miles = round(miles, 2)
print(f"Excellent! You did {miles} miles!")

# A secondary option for round

# print(f"Excellent! You did {round(miles, 2)} miles!")