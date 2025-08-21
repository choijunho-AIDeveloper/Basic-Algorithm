def solution(keymap, targets):
    answer = []
    for target in targets:
        ans = 0
        for tar in target:
            isCheck = False
            curMin = 1e9
            for key in keymap:
                if tar in key:
                    curMin = min(curMin, key.index(tar) + 1)
                    isCheck = True
            if not isCheck:
                break
            ans += curMin
        if not isCheck:
            answer.append(-1)
        else:
            answer.append(ans)
            
    return answer