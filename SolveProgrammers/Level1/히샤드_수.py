def solution(x):
    return True if x % sum([int(ele) for ele in list(str(x))]) == 0 else False