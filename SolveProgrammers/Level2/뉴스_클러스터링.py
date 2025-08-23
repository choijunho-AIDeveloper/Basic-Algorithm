def solution(str1, str2):
    from collections import Counter
    answer = 0
    union = 0
    inter = 0
    str1 = [(f"{str1[i]}{str1[i + 1]}").lower() for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()]
    str2 = [(f"{str2[i]}{str2[i + 1]}").lower() for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()]
    str1Dict = Counter(str1)
    str2Dict = Counter(str2)
    for ele in str1Dict:
        if ele in str2Dict:
            union += max(str1Dict[ele], str2Dict[ele])
            inter += min(str1Dict[ele], str2Dict[ele])
        else:
            union += str1Dict[ele]
    for ele in str2Dict:
        if ele not in str1Dict:
            union += str2Dict[ele]
    if union == 0:
        return 65536
    return int(inter/union * 65536)