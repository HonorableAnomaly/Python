# my attempt

print("Enter your tweet:")
tweet = input()
length = len(tweet)
remainder = int(length) - 140

if length <= 140:
    print(f"Your {length} character tweet will work!")
else:
    print(
        f"Your {length} character tweet is {remainder} characters too long! Tweet not posted.")

# the solution
# max_chars = 140
# print("*" * 50)
# tweet = input("Enter your tweet: ")
# char_count = len(tweet)

# if char_count < max_chars:
#     print(f"Your {char_count} character tweet will work!")
# else:
#     print(f"Your {char_count} character tweet is {char_count - max_chars} characters too long! Tweet not posted.")
