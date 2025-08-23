def solution(s):
    answer = True
    curList = []
    for i in range(len(s)):
        if not curList and s[i] == ")":
            return False
        elif s[i] == ")" and curList[-1] == "(":
            curList.pop()
        else:
            curList.append(s[i])
            
    if not curList:
        return True
    else:
        return False