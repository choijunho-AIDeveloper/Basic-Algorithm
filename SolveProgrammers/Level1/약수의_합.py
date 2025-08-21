def solution(n):
    import math
    answer = set()
    if n == 1:
        return 1
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer.add(i)
            answer.add(int(n / i))
    return sum(answer)