def string():
    a = input('Введите слово: ')
    b = 0
    for i in a:
        b += 1
    print(f'Количество букв {b}')
string()
