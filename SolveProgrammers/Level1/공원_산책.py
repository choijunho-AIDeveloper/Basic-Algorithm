def solution(park, routes):
    answer = []
    park = [list(ele) for ele in park]
    start = [[i, j] for i in range(len(park)) for j in range(len(park[0])) if park[i][j] == "S"]
    start = start[0]
    print(start)
    for route in routes:
        di, n = route.split()
        n = int(n)
        isNo = False
        if di == "E":
            for i in range(n):
                if start[1] + i + 1 > len(park[0]) - 1 or park[start[0]][start[1] + i + 1] == "X":
                    isNo = True
                    break
            if not isNo:
                start[1] += n
        if di == "S":
            for i in range(n):
                if start[0] + i + 1 > len(park) - 1 or park[start[0] + i + 1][start[1]] == "X":
                    isNo = True
                    break
            print(isNo)
            if not isNo:
                start[0] += n
        if di == "W":
            for i in range(n):
                if start[1] - i - 1 < 0 or park[start[0]][start[1] - i - 1] == "X":
                    isNo = True
                    break
            if not isNo:
                start[1] -= n
        if di == "N":
            for i in range(n):
                if start[0] - i - 1 < 0 or park[start[0] - i - 1][start[1]] == "X":
                    isNo = True
                    break
            if not isNo:
                start[0] -= n
        print(start)
    return start