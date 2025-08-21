def solution(id_list, report, k):
    declare = {id: 0 for id in id_list}
    declared = {id: set() for id in id_list}
    for r in report:
        f, s = r.split()
        declared[s].add(f)
    for key, value in declared.items():
        if len(value) >= k:
            for v in value:
                declare[v] += 1
    return list(declare.values())