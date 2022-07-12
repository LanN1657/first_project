list_1 = ['name', 'age', '1', '19']
print('Оригинальный лист: ', list_1)
def list_():
    list_1 = ['name', 'age', '1', '19']
    list_2 = list_1[:2]
    list_3 = list_1[2:]
    list_1 = list(reversed(list_2)) + list(reversed(list_3))
    print('Изменённый лист: ', list_1)
list_() 