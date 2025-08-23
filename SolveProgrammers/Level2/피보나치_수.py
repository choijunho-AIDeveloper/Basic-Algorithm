def solution(n):
    dpMap = [0] * (n + 1)
    dpMap[1] = 1
    for i in range(2, len(dpMap)):
        dpMap[i] = dpMap[i - 2] + dpMap[i - 1]
    return dpMap[n] % 1234567