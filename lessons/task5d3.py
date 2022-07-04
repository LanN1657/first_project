num = int(input('number: '))

if num % 2 == 1:
    print('Число нечётное')
else:
    print('Число чётное')
if num % 3 == 0:
    print('Число делится на 3')
else:
    print('Число не делится на 3')
if num ** 2 > 1000:
    print(num, 'больше чем 1000')
else:
    print(num, 'меньше чем 1000')
