def solution(s):
    from collections import deque
    answer = ''
    jumpList = deque()
    for i in range(1, len(s)):
        if s[i - 1].isalpha() and s[i] == " ":
            jumpList.append(1)
        elif not s[i - 1].isalpha() and s[i] == " ":
            jumpList[-1] += 1
    for st in s.split():
        answer += st[0].upper() + st[1:].lower()
        if jumpList:
            answer += " " * jumpList[0]
            jumpList.popleft()
    return answer