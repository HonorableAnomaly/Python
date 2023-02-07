color = input("Enter a color:")
# if color != "":   #can be refactored to line below
if color:
    print(f"Sweet! {color} is a great color!")
elif color == "cerulean":
    print(f"{color} is my favorite color too!")
