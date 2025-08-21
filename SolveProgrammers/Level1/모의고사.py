def solution(answers):
    answer = [0] * 3
    db = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    firstAnswer = db[0] * (len(answers)//5) + db[0][:len(answers)%5]
    secondAnswer = db[1] * (len(answers)//8) + db[1][:len(answers)%8]
    thirdAnswer = db[2] * (len(answers)//10) + db[2][:len(answers)%10]
    for i in range(len(firstAnswer)):
        if answers[i] == firstAnswer[i]:
            answer[0] += 1
    for i in range(len(secondAnswer)):
        if answers[i] == secondAnswer[i]:
            answer[1] += 1
    for i in range(len(thirdAnswer)):
        if answers[i] == thirdAnswer[i]:
            answer[2] += 1
    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i + 1)
    return result