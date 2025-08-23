def solution(dirs):
    count = 0
    # 0 : L, 1 : U, 3 : D, 4 : R
    possibleMap = [[[False] * 4 for _ in range(11)] for _ in range(11)]
    cur = [5, 5]
    for dir in dirs:
        if dir == "L" and cur[1] > 0:
            if not possibleMap[cur[0]][cur[1]][0]:
                count += 1
                possibleMap[cur[0]][cur[1]][0] = True
                possibleMap[cur[0]][cur[1] - 1][3] = True
            cur[1] -= 1
        if dir == "U" and cur[0] > 0:
            if not possibleMap[cur[0]][cur[1]][1]:
                count += 1
                possibleMap[cur[0]][cur[1]][1] = True
                possibleMap[cur[0] - 1][cur[1]][2] = True
            cur[0] -= 1
        if dir == "D" and cur[0] < len(possibleMap) - 1:
            if not possibleMap[cur[0]][cur[1]][2]:
                count += 1
                possibleMap[cur[0]][cur[1]][2] = True
                possibleMap[cur[0] + 1][cur[1]][1] = True
            cur[0] += 1
        if dir == "R" and cur[1] < len(possibleMap) - 1:
            if not possibleMap[cur[0]][cur[1]][3]:
                count += 1
                possibleMap[cur[0]][cur[1]][3] = True
                possibleMap[cur[0]][cur[1] + 1][0] = True
            cur[1] += 1
    return count