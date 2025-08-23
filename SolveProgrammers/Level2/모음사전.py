def solution(word):
    from itertools import product
    answer = 0
    words = ["A", "E", "I", "O", "U"]
    def dfs(results, result):
        if len(result) > 0:
            results.append("".join(result))
        if len(result) == 5:
            return
        for ele in words:
            result.append(ele)
            dfs(results, result)
            result.pop()
    results = []
    dfs(results, [])
    return results.index(word) + 1