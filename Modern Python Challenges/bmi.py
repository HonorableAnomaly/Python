# bmi formula
# (weight in pounds x 703) / (height in inches x height in inches)

# bmi chart
# <16.0 Severely underweight
# 16.0 - 18.4 Underweight
# 18.5 - 24.9 Normie
# 25.0 - 29.9 Overweight
# 30.0 - 34.9 Moderately Obese
# 35.0 - 39.9 Severely Obese
# >39.9 Morbidly Obese


# my attempt

# inches = int(input("Enter your height in inches: "))
# pounds = int(input("Enter your weight in pounds: "))

# # weight conversion

# # unit = print(int(input("Which unit of weight are you using (p or k)? ")))
# # if unit == "k":
# #     print(int(input("Enter your weight in kilograms: ")))
# #     conversion = round(unit * 2.20462)
# # else:
# #     pounds = print(int(input("Enter your weight in pounds: ")))

# # vvv BROKEN (pseudo-code??) vvv
# bmi = round((pounds * 703) / (inches * inches), 2)

# if bmi < 16.0:
#     rating = "Severely underweight"
# elif bmi >= 16.0 or bmi <= 18.4:
#     rating = "Underweight"
# elif bmi >= 18.5 or bmi <= 24.9:
#     rating = "Normie"
# elif bmi >= 25.0 or bmi <= 29.9:
#     rating = "Overweight"
# elif bmi >= 30.0 or bmi <= 34.9:
#     rating = "Moderately Obese"
# elif bmi >= 35.0 or bmi <= 39.9:
#     rating = "Severely Obese"
# else:
#     rating = "Morbidly Obese"

# print(f"Your BMI of {bmi} makes you {rating}.")

# the solution

height = float((input("Enter your height in inches: ")))
weight = float((input("Enter your weight in pounds: ")))
bmi = weight * 703 / height ** 2
bmi = round(bmi, 1)

if bmi < 16.0:
    rating = "Severely underweight"
elif bmi >= 16.0 or bmi <= 18.4:
    rating = "Underweight"
elif bmi >= 18.5 or bmi <= 24.9:
    rating = "Normie"
elif bmi >= 25.0 or bmi <= 29.9:
    rating = "Overweight"
elif bmi >= 30.0 or bmi <= 34.9:
    rating = "Moderately Obese"
elif bmi >= 35.0 or bmi <= 39.9:
    rating = "Severely Obese"
else:
    rating = "Morbidly Obese"

print(f"Your BMI of {bmi} makes you {rating}.")
