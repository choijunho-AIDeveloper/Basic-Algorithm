all_num = 9
nanjang_num = 7

nanjangs = []
for i in range(9):
    nanjang = int(input())
    nanjangs.append(nanjang)

non_nanjang_sum = sum(nanjangs) - 100

change = False

for i in range(len(nanjangs)):
    for j in range(len(nanjangs)):
        if i != j:
            if nanjangs[i] + nanjangs[j] == non_nanjang_sum:
                remove_element = [nanjangs[i], nanjangs[j]]
                nanjangs.remove(remove_element[0])
                nanjangs.remove(remove_element[1])
                change = True
                break
    if change == True:
        break

nanjangs.sort()

for i in range(len(nanjangs)):
    print(nanjangs[i])
