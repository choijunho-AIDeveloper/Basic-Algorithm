from collections import defaultdict

com_num = int(input())
con_num = int(input())
con_dict = defaultdict(list)
vir = [0] * (com_num + 1)

for _ in range(con_num):
  fir, sec = map(int,input().split())
  con_dict[fir].append(sec)
  con_dict[sec].append(fir)


def dfs(node):
  for con_num in con_dict[node]:
    if vir[con_num] != 1 and con_num != 1:
      vir[con_num] = 1
      dfs(con_num)


dfs(1)
print(sum(vir))