import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

graph = {i: [] for i in range(n)}

for i in range(len(parent)):
	if parent[i] != -1:
		graph[parent[i]].append(i)

def dfs(rem_node, graph, is_first, parent):
	if graph[rem_node] == []:
		graph[rem_node].append(-1)
		if is_first and len(graph[parent[rem_node]]) == 1:
			graph[parent[rem_node]] = []
	else:
		is_first = False
		for node in graph[rem_node]:
			dfs(node, graph, is_first, parent)
		
if parent[remove_node] == -1:
	print(0)
else:
	is_first = True
	dfs(remove_node, graph, is_first, parent)
	
	count = 0
	for i in range(len(graph)):
		if graph[i] == []:
			count += 1
			
	print(count)