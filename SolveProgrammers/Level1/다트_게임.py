def solution(dartResult):
    answer = []
    cur = []
    for i in range(len(dartResult)):
        if dartResult[i] == "*":
            if len(answer) == 1:
                answer[-1] = 2 * answer[-1]
            else:
                answer[-1], answer[-2] = 2 * answer[-1], 2 * answer[-2]
        elif dartResult[i] == "#":
            answer[-1] = -answer[-1]
        else:
            if dartResult[i].isalpha():
                if dartResult[i] == "S":
                    answer.append(int("".join(cur)))
                    cur = []
                elif dartResult[i] == "D":
                    answer.append(int("".join(cur)) ** 2)
                    cur = []
                elif dartResult[i] == "T":
                    answer.append(int("".join(cur)) ** 3)
                    cur = []
            else:
                cur.append(dartResult[i])            
            
    return sum(answer)