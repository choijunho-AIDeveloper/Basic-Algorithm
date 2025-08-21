def solution(mats, park):
    mats.sort()
    def check(mats, cur, park):
        maxNum = -1
        for mat in mats:
            isCheck = False
            if cur[0] + mat <= len(park) and cur[1] + mat <= len(park[0]):
                for i in range(mat):
                    for j in range(mat):
                        if park[cur[0] + i][cur[1] + j] != "-1":
                            isCheck = True
                            break
                if not isCheck:
                    maxNum = max(mat, maxNum)
        return maxNum
    maximum = -1
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                maximum = max(maximum, check(mats, [i, j], park))
    return maximum