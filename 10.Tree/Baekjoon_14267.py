from collections import defaultdict
import sys
input = sys.stdin.readline

sys.setrecursionlimit(200000)

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

graph = defaultdict(list)
for i in range(n):
    if n_list[i] != -1:
        graph[n_list[i]].append(i + 1)

m_list = defaultdict(int)
for _ in range(m):
	comp_person, comp = map(int, input().split())
	m_list[comp_person] += comp

comp_dict = [0] * (n + 1)

def dfs(node, graph, count):
	comp_dict[node] = count + m_list[node]
	for child in graph[node]:
		dfs(child, graph, comp_dict[node])

dfs(1, graph, 0)
for i in range(1, len(comp_dict)):
	print(comp_dict[i], end = " ")