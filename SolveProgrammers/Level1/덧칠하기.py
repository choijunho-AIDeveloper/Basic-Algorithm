def solution(n, m, section):
    li = [0] * n
    for s in section:
        li[s-1] = 1
    
    result = 0
    for i in range(len(li)):
        if li[i] == 1:
            result += 1
            for j in range(m):
                if i + j < len(li):
                    if li[i+j] == 1:
                        li[i+j] = 0
    return result