from collections import defaultdict

n = int(input())
m = int(input())
n_dict = defaultdict(list)
member = [False] * (n + 1)

for _ in range(m):
  fir, sec = map(int, input().split())
  n_dict[fir].append(sec)
  n_dict[sec].append(fir)

member[1] = True

for n_num in n_dict[1]:
  if not member[n_num]:
    member[n_num] = True
  for sub_num in n_dict[n_num]:
    if not member[sub_num]:  
      member[sub_num] = True

print(sum(member) - 1)