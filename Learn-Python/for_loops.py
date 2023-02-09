for num in range(1, 10):
    print(num)
    print(num*num)

for char in "tea leaf":
    print(char)

for num in range(1, 10, 2):
    print(num)

for even in range(10, 20, 2):
    print(even)

x = 0
for n in range(10, 21):  # remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n

n = 0
for y in range(11, 21, 2):
    x += y
