def solution(s):
    from collections import deque
    from copy import deepcopy
    def isStack(s):
        copy_s = deepcopy(s)
        li = []
        for _ in range(len(s)):
            temp = copy_s.popleft()
            if li and li[-1] == "(" and temp == ")":
                li.pop()
            elif li and li[-1] == "[" and temp == "]":
                li.pop()
            elif li and li[-1] == "{" and temp == "}":
                li.pop()
            else:
                li.append(temp)
        if not li:
            return True
        else:
            return False
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        temp = s.popleft()
        s.append(temp)
        if isStack(s):
            answer += 1
    return answer