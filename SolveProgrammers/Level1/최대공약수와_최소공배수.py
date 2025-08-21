def solution(n, m):
    answer = []
    result = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            result = i
    answer.append(result)
    answer.append(n * m / result)
    return answer