# my attempt
# for emoji in range(1, 11):
#     print("\U0001f600"[emoji])

# the solution (for)
for num in range(1, 11):
    print("\U0001f600" * num)

# solution 2 (while)
times = 1
while times <= 10:
    print("\U0001f600" * times)
    times += 1

# solution 3 (UGLY QUADRATIC STYLE)
# for num in range(1, 11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "\U0001f600"
#         count += 1
#     print(smileys)
