def solution(k, dungeons):
    from itertools import permutations
    maxNum = 0
    can = list(permutations(list(range(len(dungeons))), len(dungeons)))
    for ele in can:
        rest = k
        res = 0
        for e in list(ele):
            if dungeons[e][0] > rest:
                continue
            res += 1
            rest -= dungeons[e][1]
        maxNum = max(res, maxNum)
            
    return maxNum
