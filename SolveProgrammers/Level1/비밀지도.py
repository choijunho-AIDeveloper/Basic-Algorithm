def solution(n, arr1, arr2):
    answer = []
    def isChange(number):
        i = 2 ** (n - 1)
        returnArr = []
        while i >= 1:
            returnArr.append(int(number // i))
            number %= i
            i /= 2
        return returnArr
    for i in range(len(arr1)):
        temp = ""
        arr1Ele = isChange(arr1[i])
        arr2Ele = isChange(arr2[i])
        for j in range(len(arr1Ele)):
            if not arr1Ele[j] and not arr2Ele[j]:
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
    return answer