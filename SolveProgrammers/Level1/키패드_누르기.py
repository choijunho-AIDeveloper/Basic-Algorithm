def solution(numbers, hand):
    answer = ''
    leftCur = [3, 0]
    rightCur = [3, 2]
    def checkSame(number, leftCur, rightCur, hand):
        left = 0
        right = 0
        isCur = ""
        if abs(number[0] - leftCur[0]) + abs(number[1] - leftCur[1]) > abs(number[0] - rightCur[0]) + abs(number[1] - rightCur[1]):
            isCur = "R"
            rightCur = number[:]
        elif abs(number[0] - leftCur[0]) + abs(number[1] - leftCur[1]) < abs(number[0] - rightCur[0]) + abs(number[1] - rightCur[1]):
            isCur = "L"
            leftCur = number[:]
        else:
            if hand == "right":
                isCur = "R"
                rightCur = number[:]
            else:
                isCur = "L"
                leftCur = number[:]
        return isCur, leftCur, rightCur
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            if number == 1:
                leftCur = [0, 0]
            elif number == 4:
                leftCur = [1, 0]
            elif number == 7:
                leftCur = [2, 0]
        elif number in [3, 6, 9]:
            answer += "R"
            if number == 3:
                rightCur = [0, 2]
            elif number == 6:
                rightCur = [1, 2]
            elif number == 9:
                rightCur = [2, 2]
        else:
            if number == 2:
                isCur, leftCur, rightCur = checkSame([0, 1], leftCur, rightCur, hand)
                answer += isCur
            if number == 5:
                isCur, leftCur, rightCur = checkSame([1, 1], leftCur, rightCur, hand)
                answer += isCur
            if number == 8:
                isCur, leftCur, rightCur = checkSame([2, 1], leftCur, rightCur, hand)
                answer += isCur
            if number == 0:
                isCur, leftCur, rightCur = checkSame([3, 1], leftCur, rightCur, hand)
                answer += isCur
            
        
    return answer