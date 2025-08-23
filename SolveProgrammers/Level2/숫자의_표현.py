def solution(n):
    answer = 0
    for i in range(n):
        sumNum = 0
        s = i
        while sumNum < n:
            sumNum += 1 + s
            s += 1
        if sumNum == n:
            answer += 1
    return answer