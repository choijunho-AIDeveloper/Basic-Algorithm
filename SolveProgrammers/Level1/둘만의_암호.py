def solution(s, skip, index):
    def change(ele, skip, index):
        skip = [ord(i) for i in list(skip)]
        curEle = ord(ele)
        for _ in range(index):
            curEle += 1
            if curEle > 122:
                curEle -= 26
            while curEle in skip:
                curEle += 1
                if curEle > 122:
                    curEle -= 26
        return chr(curEle)
    s = list(s)
    for i in range(len(s)):
        s[i] = change(s[i], skip, index)
    return "".join(s)