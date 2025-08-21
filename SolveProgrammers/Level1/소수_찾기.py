def solution(n):
    answer = 0
    import math
    def isPrime(num):
        if num == 2: return True
        if num == 3: return True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    for i in range(2, n + 1):
        answer += isPrime(i)
    return answer