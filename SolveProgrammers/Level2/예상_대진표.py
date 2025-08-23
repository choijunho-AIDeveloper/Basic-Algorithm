def solution(n,a,b):
    n_list = [[i, i + 1] for i in range(1, n + 1, 2)]
    idx = 1
    while [a, b] not in n_list and [b, a] not in n_list:
        temp = []
        idx += 1
        for ele in n_list:
            if ele[0] == a:
                temp.append(ele[0])
            elif ele[1] == a:
                temp.append(ele[1])
            elif ele[0] == b:
                temp.append(ele[0])
            elif ele[1] == b:
                temp.append(ele[1])
            else:
                temp.append(ele[0])
        n_list = [[temp[i], temp[i + 1]] for i in range(0, len(temp), 2)]
    return idx