n = int(input())

possibleMap = [0] * (n + 1)
stairs = [0]

for _ in range(n):
    stair = int(input())
    stairs.append(stair)

if n >= 1:
    possibleMap[1] = stairs[1]
if n >= 2:
    possibleMap[2] = stairs[1] + stairs[2]
if n >= 3:
    for i in range(3, n + 1):
            possibleMap[i] = max(possibleMap[i - 3] + stairs[i - 1], possibleMap[i - 2]) + stairs[i]

print(possibleMap[n])