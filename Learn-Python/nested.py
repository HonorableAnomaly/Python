# Dependent vs. independent nesting

# Dependent
fav_color = "cerulean"
fav_movie = "Lord of the Rings"
fav_food = "pasta"

if fav_color == "cerulean":
    print("Cerulean is my favorite color too!")
    if fav_movie == "Lord of the Rings":
        print("Lord of the Rings is my favorite movie too!")
        if fav_food == "pasta":
            print("Pasta is my favorite food too!")

# Independent
fav_color = "cerulean"
fav_movie = "Lord of the Rings"
fav_food = "pasta"

if fav_color == "cerulean":
    print("Cerulean is my favorite color too!")
if fav_movie == "Lord of the Rings":
    print("Lord of the Rings is my favorite movie too!")
if fav_food == "pasta":
    print("Pasta is my favorite food too!")
