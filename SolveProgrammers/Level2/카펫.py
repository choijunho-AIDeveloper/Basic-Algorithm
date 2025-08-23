def solution(brown, yellow):
    import math
    answer = []
    def check(n):
        result = []
        for i in range(1, int(math.sqrt(yellow)) + 1):
            if n % i == 0:
                result.append([n//i, i])
        print(result)
        return result
    result = check(yellow)
    for res in result:
        if (res[0] + 2) * (res[1] + 2) == yellow + brown:
            return [res[0] + 2, res[1] + 2]
    return answer