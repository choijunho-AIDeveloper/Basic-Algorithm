def solution(nums):
    import math
    from itertools import combinations
    
    answer = 0
    
    def isPrime(num):
        if num == 2:return True
        if num == 3:return True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    numList = combinations(nums, 3)
    for ele in numList:
        answer += isPrime(sum(ele))
    
    return answer