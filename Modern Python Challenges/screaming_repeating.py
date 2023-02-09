# My attempt
# scream = input("How many times do I have to tell you?")

# for x in scream:
#     command = "CLEAN YOUR ROOM!!!\n"
#     command[x] += command
#     if int(scream) < 100:
#         print(command)

# The solution
times = input("How many times do I have to tell you? ")
times = int(times)

for time in range(times):
    print("CLEAN UP YOUR ROOM!!!")

# to show each incrememnt of scream
# for time in range(times):
#     print(f"time {time + 1}:CLEAN UP YOUR ROOM!!!")
