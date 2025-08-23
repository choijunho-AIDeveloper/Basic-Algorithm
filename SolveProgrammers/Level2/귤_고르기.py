def solution(k, tangerine):
    from collections import defaultdict
    gulDict = defaultdict(int)
    for ele in tangerine:
        gulDict[ele] += 1
    gul = sorted(gulDict.items(), key = lambda x: x[1], reverse = True)
    answer = 0
    s = 0
    for g in gul:
        if s >= k:
            break
        else:
            answer += 1
            s += g[1]
    return answer