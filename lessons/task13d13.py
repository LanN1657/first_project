dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
def union_dict():
    dict1.update(dict2)
    print(dict1)
union_dict()