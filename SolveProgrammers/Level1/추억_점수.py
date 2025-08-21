def solution(name, yearning, photo):
    from collections import defaultdict
    personDict = defaultdict(int)
    for i in range(len(name)):
        personDict[name[i]] = yearning[i]
    answer = []
    for ele in photo:
        temp = 0
        for eleEle in ele:
            temp += personDict[eleEle]
        answer.append(temp)
    return answer