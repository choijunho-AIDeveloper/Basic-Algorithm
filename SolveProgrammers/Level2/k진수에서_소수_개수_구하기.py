def solution(n, k):
    answer = 0
    import math
    from collections import deque
    
    def isDecimal(num):
        isTrue = True
        if num == 1:
            return False
        if num == 2 or num == 3:
            return True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    def trans(num, k):
        n_list = deque()
        while num // k > 0:
            n_list.appendleft(str(num % k))
            num //= k
        n_list.appendleft(str(num))
        return "".join(n_list)
    
    n = trans(n, k)
    comp = []
    prev = 0
    comp = [ele for ele in n.split("0") if ele]
    for ele in comp:
        if isDecimal(int(ele)):
            answer += 1
    return answer