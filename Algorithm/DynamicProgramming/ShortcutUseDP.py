from collections import defaultdict
n, m = map(int, input().split())
possibleMap = [1e9] * (m + 1)

update = defaultdict(list)
for _ in range(n):
    start, end, dist = map(int, input().split())
    if end <= m:
        update[start].append([end, dist])
possibleMap[0] = 0
for i in range(len(possibleMap)):
    possibleMap[i] = min(possibleMap[i - 1] + 1, possibleMap[i])
    if update[i]:
        for j in range(len(update[i])):
            possibleMap[update[i][j][0]] = min(possibleMap[update[i][j][0]], possibleMap[i] + update[i][j][1])

print(possibleMap[-1])