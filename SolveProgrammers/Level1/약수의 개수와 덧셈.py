def solution(left, right):
    import math
    answer = 0
    for i in range(left, right + 1):
        if i / int(math.sqrt(i)) == math.sqrt(i):
            answer -= i
        else:
            answer += i
    return answer