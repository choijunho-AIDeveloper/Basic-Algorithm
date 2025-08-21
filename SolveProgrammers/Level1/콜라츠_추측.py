def solution(num):
    lo = 0
    while num != 1:
        lo += 1
        if lo == 500:
            return -1
        
        if num % 2 == 0:
            num /= 2
        elif num %  2 == 1:
            num = num * 3 + 1

    return lo