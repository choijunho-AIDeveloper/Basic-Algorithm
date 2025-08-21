def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    for ele in babbling:
        for sp in speak:
            if sp * 2 in ele:
                break
            if sp in ele:
                ele = ele.replace(sp, " ")
        if not ele.replace(" ", ""):
            answer += 1
                
                
    return answer