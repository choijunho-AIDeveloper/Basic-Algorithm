def solution(n, t, m, p):
    from collections import deque
    answer = ''
    transDict = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    def jinsu(n, num):
        n_list = deque()
        while num // n > 0:
            if num % n >= 10:
                n_list.appendleft(transDict[num % n])
            else:
                n_list.appendleft(num % n)
            num //= n
        if num >= 10:
            n_list.appendleft(transDict[num])
        else:
            n_list.appendleft(num)
        return n_list
    l = 0
    check = jinsu(n, l)
    for i in range(t):
        for j in range(m):
            temp = check.popleft()
            if not check:
                l += 1
                check = jinsu(n, l)
            if j + 1 == p:
                answer += str(temp)
    return answer