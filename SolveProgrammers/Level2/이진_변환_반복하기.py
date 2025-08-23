def solution(s):
    from collections import deque
    answer = []
    def toTwo(num):
        ans = deque()
        num = len(num)
        while num > 1:
            ans.appendleft(str(num % 2))
            num //= 2
        ans.appendleft(str(num))
        return "".join(ans)
    while s != "1":
        answer.append(s.count("0"))
        s = s.replace("0", "")
        print(s)
        s = toTwo(s)
    return [len(answer), sum(answer)]