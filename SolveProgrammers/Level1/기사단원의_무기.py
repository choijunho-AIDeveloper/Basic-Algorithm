def solution(number, limit, power):
    import math
    def isPrime(num):
        if num == 1:
            return 1
        count = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if i == math.sqrt(num):
                    count += 1
                else:
                    count += 2  
        return count
    result = 0
    for i in range(1, number + 1):
        result += isPrime(i) if isPrime(i) <= limit else power
    return result