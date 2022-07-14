a = int(input('Введите сумму которую хотите занять: '))
proc = 3.47
while True:
    if a >= 50000:
        b = a * (proc / 100)
        c = b + a
        c = round(c, 2)
        print(f'Вам нужно будет вернуть {c} ')
        break
    else:
        print('Вы ввели недостаточную сумму!')
        a = int(input('Введите сумму которую хотите занять: '))