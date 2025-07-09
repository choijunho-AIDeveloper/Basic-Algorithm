n = int(input())

possibleMap = [1e9] * (n + 1)
possibleMap[0], possibleMap[1] = 0, 1
for i in range(2, n + 1):
    possibleMap[i] = possibleMap[i - 1] + possibleMap[i - 2]

print(possibleMap[-1])