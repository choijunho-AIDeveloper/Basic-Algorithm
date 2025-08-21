def solution(k, m, score):
    idx = 0
    score.sort(reverse = True)
    answer = 0
    temp = []
    for i in range(len(score)):
        if i % m == m - 1:
            temp.append(score[i])
            answer += temp[-1] * len(temp)
            temp = []
        else:
            temp.append(score[i])
    return answer