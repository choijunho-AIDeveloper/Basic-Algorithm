def solution(arr, divisor):
    answer = [ele for ele in arr if ele % divisor == 0]
    answer.sort()
    if not answer:
        return [-1]
    return answer