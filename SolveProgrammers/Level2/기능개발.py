def solution(progresses, speeds):
    answer = []
    result = []
    import math
    for i in range(len(progresses)):
        ele = math.ceil((100 - progresses[i])/speeds[i])
        result.append(ele)
    stack = 1
    if len(result) == 1:
        return [stack]
    curMax = result[0]
    for i in range(1, len(result)):
        if result[i] > curMax:
            answer.append(stack)
            curMax = result[i]
            stack = 1
        else:
            stack += 1
    answer.append(stack)
    return answer
                     