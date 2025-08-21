def solution(survey, choices):
    result = ""
    check = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    surDict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    choiceDict = {1 : 3, 2 : 2, 3 : 1, 4 : 0, 5 : -1, 6 : -2, 7 : -3}
    for i in range(len(survey)):
        surDict[survey[i][0]] += choiceDict[choices[i]]
    for che in check:
        if surDict[che[0]] > surDict[che[1]]:
            result += che[0]
        elif surDict[che[0]] < surDict[che[1]]:
            result += che[1]
        else:
            so = list(sorted([che[0], che[1]]))
            result += so[0]
    return result