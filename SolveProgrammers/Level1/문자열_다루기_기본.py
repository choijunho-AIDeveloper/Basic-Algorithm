def solution(s):
    answer = True
    if not len(s) == 4 and not len(s) == 6:
        return False
    for ele in s:
        if not ele.isdigit():
            answer = False
            break
    return answer