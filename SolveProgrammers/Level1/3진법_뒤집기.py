def solution(n):
    answer = []
    
    num = 1
    while n >= num:
        num *= 3
        
    while True:
        num /= 3
        if num < 1:
            break
        answer.append(n // num)
        n %= num
    result = 0
    for i in range(len(answer)):
        result += (3 ** i) * answer[i]
    return result