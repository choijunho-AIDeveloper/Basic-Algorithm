def solution(n, lost, reserve):
    n_list = [1] * n
    for ele in lost:
        n_list[ele-1] = 0
    for ele in reserve:
        if n_list[ele-1] == 0:
            n_list[ele-1] = 1
        else:
            n_list[ele-1] = 2
    for i in range(n):
        if n_list[i] == 0:
            if i > 0 and n_list[i-1] == 2:
                n_list[i-1] = 1
                n_list[i] = 1
            elif i < len(n_list)-1 and n_list[i+1] == 2:
                n_list[i+1] = 1
                n_list[i] = 1
    return n_list.count(1) + n_list.count(2)