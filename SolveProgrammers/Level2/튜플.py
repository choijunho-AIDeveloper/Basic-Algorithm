def solution(s):
    s = list(s.split("}"))
    s_list = []
    for ele in s:
        temp = []
        tempStr = ""
        for i in ele:
            if i.isdigit():
                tempStr += i
            if i == ",":
                if tempStr:temp.append(int(tempStr))
                tempStr = ""
        if tempStr:temp.append(int(tempStr))
        s_list.append(temp)
    s_list = [ele for ele in s_list if ele]
    s_list = sorted(s_list, key = lambda x: len(x))
    prev = s_list[0]
    result = s_list[0]
    for i in range(1, len(s_list)):
        temp = list(set(s_list[i]) - set(prev))
        result.append(temp[0])
        prev = s_list[i]
    return result