# 11726
n = int(input())

possibleMap = [0] * (n + 1)
possibleMap[0] = 1
possibleMap[1] = 1

for i in range(2, len(possibleMap)):
    possibleMap[i] = possibleMap[i - 1] + possibleMap[i - 2]

print(possibleMap[-1] % 10007)