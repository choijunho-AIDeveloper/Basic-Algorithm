class combinators:
    def __init__(self, strList, returnLength):
        self.strList = strList
        self.returnLength = returnLength
        self.results = []
    def combination(self):
        self.results = []

        def dfs(result, visited):
            if len(result) == self.returnLength:
                self.results.append(result[:])
                return
            for i in range(len(self.strList)):
                if not visited[i]:
                    result.append(self.strList[i])
                    visited[i] = True
                    dfs(result, visited)
                    result.pop()
                    visited[i] = False

        visited = [False] * len(self.strList)
        dfs([], visited)

        return self.results
    def permutation(self):
        self.results = []

        def dfs(idx, result):
            if len(result) == self.returnLength:
                self.results.append(result[:])
                return
            for i in range(idx, len(self.strList)):
                result.append(self.strList[i])
                dfs(i + 1, result)
                result.pop()

        dfs(0, [])

        return self.results
    def combinationWithRepetition(self):
        self.results = []

        def dfs(result):
            if len(result) == self.returnLength:
                self.results.append(result[:])
                return
            for i in range(len(self.strList)):
                result.append(self.strList[i])
                dfs(result)
                result.pop()

        dfs([])
        
        return self.results
    def permutationWithRepetition(self):
        self.results = []

        def dfs(idx, result):
            if len(result) == self.returnLength:
                self.results.append(result[:])
                return
            for i in range(idx, len(self.strList)):
                result.append(self.strList[i])
                dfs(i, result)
                result.pop()

        dfs(0, [])
        return self.results


if __name__ == "__main__":
    combinator = combinators(["a", "b", "c"], 2)
    print(combinator.combination())
    print(combinator.combinationWithRepetition())
    print(combinator.permutation())
    print(combinator.permutationWithRepetition())