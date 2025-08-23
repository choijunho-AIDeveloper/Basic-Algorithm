def solution(numbers, target):
    def dfs(idx, node):
        if len(node) == len(numbers):
            if sum(node) == target:
                return 1
            return 0
        node.append(numbers[idx])
        plus = dfs(idx + 1, node)
        node.pop()
        node.append(-numbers[idx])
        minus = dfs(idx + 1, node)
        node.pop()
        return plus + minus
        
    return dfs(0, [])