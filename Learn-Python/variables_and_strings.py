pokemon = 3

friends = pokemon

_pokemon = 9

pokemon3 = 3

Pokemon = pokemon

# Python naming conventions
#   snake_case not camelCase
#   SNAKE_CASE refers to constants like PI
#   upper CamelCase refers to class
#   dunder means __no_touchy__
#   booleans are UpperCamelCased


### Data Types
# Booleans
is_active = True

game_over = True
game_over = False

# Strings

some_string = "8"
string = "Hello, I am a string!"

# List (ordered/sequenced)
[1,2,3]
["a","b","c"]

# Dict (unordered collection)
{"first_name":"Ricky", "last_name":"Argenbright"}

# Python is dynamically typed and variables can be reassigned as any data type

# None is a Python keyword like null in JS
first_name = "Daisy"
age = 30
child = None

# help(keywords) to search for Python keywords

# Can use quotes inside of other quotes
my_other_str = "a cat"
my_str = 'a hat'
msg = "He said, 'Hello there!'"
msg2 = 'He said, "Hello there!"'

# Escape characters start with backslashes
new_line = "Hello \n World!"

backslash_str = "This is a backslash: \\"
double_quotes = "She said \"Ha ha\""

# Concatenation
str_one = "Your"
str_two = "face"
str_three = str_one + " " + str_two
str_four = "Jimmy"

print("Hello there and welcome to the game, " + str_four)

name = "Bond"
name += (", James" + name)

# F-strings
#   If you want to use curly braces you need an f
guess = 9
print(f"Your guess of {guess} was incorrect!")
print(f"Your guess of {guess + 1} was incorrect!")

second_guess = f"Nice try, {name}, but your guess of {guess} was incorrect!"

# Bad old 3.5 format!
# print("Nice try, {}, but your guess of {} was incorrect!".format(name, guess))

# Indices
laugh = "lol"
print(laugh[0])

# Converting data types
#   Use the data type as a precursor
#   Don't use keywords as variable names!!!
decimal = 13.325463
integer = int(decimal)