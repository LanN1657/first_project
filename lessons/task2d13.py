list_1 = set()
for i in range(5):
    a = int(input('Введите число: '))
    list_1.add(a)
list_2 = list(list_1)
print(f'Самое минимальное число введённое вами {list_2[0]}')