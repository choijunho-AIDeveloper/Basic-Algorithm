def solution(d, budget):
    answer = 0
    d.sort()
    for ele in d:
        if budget - ele < 0:
            break
        else:
            budget -= ele
            answer += 1
    return answer