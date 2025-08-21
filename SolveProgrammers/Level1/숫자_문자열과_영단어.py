def solution(s):
    from collections import deque
    answer = ""
    eleDict = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    s = deque(s)
    curEle = ""
    while s:
        if s[0].isdigit():
            answer += s.popleft()
        else:
            curEle += s.popleft()
            if curEle in eleDict:
                answer += str(eleDict[curEle])
                curEle = ""
    return int(answer)