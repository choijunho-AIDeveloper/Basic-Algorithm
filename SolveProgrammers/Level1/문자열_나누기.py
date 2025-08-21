def solution(s):
    from collections import deque
    s = deque(list(s))
    answer = 0
    left, right = 0, 0
    while s:
        comp = s.popleft()
        left += 1
        while s and left > right:
            temp = s.popleft()
            if comp == temp:
                left += 1
            else:
                right += 1
        answer += 1
    return answer