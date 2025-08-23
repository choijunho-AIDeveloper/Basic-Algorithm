def solution(arr):
    import math
    if len(arr) == 1:
        return arr[0]
    g = 1
    answer = arr[0]
    for i in range(1, len(arr)):
        g = math.gcd(answer, arr[i])
        answer = (answer * arr[i]) // g
    return answer