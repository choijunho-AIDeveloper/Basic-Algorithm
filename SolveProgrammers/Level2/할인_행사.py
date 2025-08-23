def solution(want, number, discount):
    answer = 0
    wantDict = {want[i]: number[i] for i in range(len(want))}
    for i in range(len(discount) - sum(number) + 1):
        temp = discount[i:i + sum(number)]
        productSet = set(temp)
        isCheck = True
        for product in productSet:
            if product in wantDict and temp.count(product) == wantDict[product]:
                pass
            else:
                isCheck = False
                break
        if isCheck:
            answer += 1
    return answer