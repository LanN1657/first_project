num = int(input('number: '))

if num % 2 == 1:
    print('odd number')
else:
    print('number is even')
if num % 3 == 0:
    print('number is divisible by 3')
else:
    print('number is not divisible by 3')
if num ** 2 > 1000:
    print(num, 'is bigger than 1000')
else:
    print(num, 'is smaller than 1000')
