def solution(X, Y):
    answer = ""
    for i in range(9, -1, -1):
        for _ in range(min(X.count(str(i)), Y.count(str(i)))):
            answer += str(i)
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer