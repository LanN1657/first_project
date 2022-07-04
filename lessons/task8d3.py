a = int(input('Баллы: '))

if a >= 90:
    print('A')
else:
    if a <= 89 and a >= 70:
        print('B')
    else:
        if a <= 69 and a >= 50:
            print('C')
        else:
            print('Good luck next time!')
