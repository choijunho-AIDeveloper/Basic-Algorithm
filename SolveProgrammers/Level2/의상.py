def solution(clothes):
    from collections import defaultdict
    clothesDict = defaultdict(list)
    for name, t in clothes:
        clothesDict[t].append(name)
    result = []
    for clothesEle in clothesDict:
        result.append(len(clothesDict[clothesEle]))
    answer = 1
    for ele in result:
        answer *= ele + 1
    return answer - 1