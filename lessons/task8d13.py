dict_1 = {'a': 1, 'b': 2, 'c': 3}
def func():
    tuple_1 = []
    tuple_2 = []
    tuple_1.append(dict_1.keys())
    tuple_2.append(dict_1.values())
    tuple_1 = tuple(tuple_1)
    tuple_2 = tuple(tuple_2)
    print(tuple_1, end=' ')
    print(tuple_2, end=' ')
func()