def solution(n, words):
    answer = []
    word = []
    idx = 0
    l = 1
    prev = ""
    for w in words:
        idx += 1
        if w in word:
            print(w, word)
            return [idx, l]
        if prev and prev[-1] != w[0]:
            print(prev, word)
            return [idx, l]
        if idx == n:
            idx = 0
            l += 1
        word.append(w)
        prev = w
    return [0, 0]