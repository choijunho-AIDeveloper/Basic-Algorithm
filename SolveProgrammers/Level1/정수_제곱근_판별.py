def solution(n):
    import math
    return (math.sqrt(n) + 1) ** 2 if n / int(math.sqrt(n)) == math.sqrt(n) else -1