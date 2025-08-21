def solution(participant, completion):
    from collections import defaultdict
    answer = ""
    participantDict = defaultdict(int)
    for ele in participant:
        participantDict[ele] += 1
    for ele in completion:
        participantDict[ele] -= 1
    for ele in participantDict:
        if participantDict[ele] == 1:
            answer = ele[:]
    
    return answer