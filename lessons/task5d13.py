a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def add():
    c = a + b
    print(f'Сумма чисел {a} и {b} равна {c}')
add()

def substract():
    d = a - b
    print(f'Разность чисел {a} и {b} равна {d}')
substract()

def multiply():
    e = a * b
    print(f'Произведение чисел {a} и {b} равна {e}')
multiply()

def divide():
    try:
        f = a / b
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
    else:
        print(f'Деление чисел {a} и {b} равна {f}')
divide()