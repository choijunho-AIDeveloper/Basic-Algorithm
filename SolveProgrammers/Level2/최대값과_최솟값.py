def solution(s):
    s = list(map(int, s.split()))
    s_list = [str(min(s)), str(max(s))]
    return " ".join(s_list)