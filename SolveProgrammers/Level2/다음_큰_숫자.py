def solution(n):
    answer = 0
    def toTwo(num):
        result = 0
        while num > 1:
            if num % 2 == 1:
                result += 1
            num //= 2
        return result + 1
    prev = toTwo(n)
    while True:
        n += 1
        cur = toTwo(n)
        if cur == prev:
            return n