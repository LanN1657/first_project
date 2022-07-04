a =float(input('Первый номер: '))
b = float(input('Второй номер: '))
c = float(input('Третий номер: '))

if a > b and b < a and b > c: #a > b > c
    print(a, b, c)
elif a < b and a > c and b > c: #b > a > c
    print(b, a, c)
elif a > b and c > b and a > c: #a > c > b
    print(a, c, b)
elif a < b and b > c and a < c: #b > c > a
    print(b, c, a)
elif a > b and c > b and a < c: #c > a > b
    print(c, a, b)
elif c > b and b > a and c > a: #c > b > a
    print(c, b, a)
elif a == b and a < c:
    print(c, 'больше,', 'номера', a, 'и', b, 'равны')
elif a == b and a > c:
    print('Номера', a, 'и', b, 'равны', c, 'меньшее')
elif a == c and a < b:
    print(b, 'больше,', 'номера', a, 'и', c, 'равны')
elif a == c and a > b:
    print('номера', a, 'и', c, 'равны',  b, 'меньшее')
elif b == c and b < a:
    print('номера', b, 'и', c, 'равны', a, 'меньшее')
elif b == c and b > a:
    print(a, 'больше', 'номера', b, 'и', c, 'равны')
else:
    print('Все номера равны')
