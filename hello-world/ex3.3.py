# score = input("Enter Score: ")
# scoreInt = float(score)

# if scoreInt < 0 and scoreInt > 1:
#     print("Please input a score that is between 1 and 0")
# elif scoreInt < 1 and scoreInt >= 0.9:
#     print("A")
# elif scoreInt >= 0.8:
#     print("B")
# elif scoreInt >= .7:
#     print("C")
# elif scoreInt >= .6:
#     print("D")
# else:
#     print("F")

# x = 1
# x = x + 1
# print(x)
# n = 10
# while False:
#     print(n, end=' ')
#     n = n - 1
# print('Done!')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')