# controlled break with input

# while True:
#     command = input("type EXIT to exit: ")
#     if command == "EXIT":
#         break

# auto printing break

# for x in range(1, 10):
#     print(x)
#     if x == 3:
#         break

# auto stop mid loop

times = int(input("How many times do I have to tell you?"))

for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 4:
        print("Do you even listen anymore?")
        break
