def solution(s):
    s = s.lower()
    pNum = 0
    yNum = 0
    for ele in s:
        if ele == "p":
            pNum += 1
        if ele == "y":
            yNum += 1
    return True if pNum == yNum else False