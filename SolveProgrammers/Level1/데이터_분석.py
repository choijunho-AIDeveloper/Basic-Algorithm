def solution(data, ext, val_ext, sort_by):
    check_dict = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    data = [ele for ele in data if ele[check_dict[ext]] < val_ext]
    return sorted(data, key = lambda x: x[check_dict[sort_by]])