import sys

input = sys.stdin.readline
n = int(input())

possibleMap = [1e9] * (3 * n + 1)
possibleMap[1] = 1
for i in range(1, n + 1):
    possibleMap[i + 1] = min(possibleMap[i] + 1, possibleMap[i + 1])
    possibleMap[2 * i] = min(possibleMap[i] + 1, possibleMap[2 * i])
    possibleMap[3 * i] = min(possibleMap[i] + 1, possibleMap[3 * i])

print(possibleMap[n] - 1)