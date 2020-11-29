import itertools

lst = [1, 2, 3]
all_combs = []

for r in range(len(lst) + 1):
    combs_object = itertools.combinations(lst, r)
    combs_lst = list(combs_object)
    all_combs += combs_lst
# print(all_combs)
