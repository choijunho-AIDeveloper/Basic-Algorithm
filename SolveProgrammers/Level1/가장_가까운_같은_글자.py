def solution(s):
    from collections import defaultdict
    answer = []
    dictMap = defaultdict(list)
    s = list(s)
    for i in range(len(s)):
        if s[i] in dictMap:
            answer.append(i - dictMap[s[i]][-1])
            dictMap[s[i]].append(i)
        else:
            answer.append(-1)
            dictMap[s[i]].append(i)
    return answer