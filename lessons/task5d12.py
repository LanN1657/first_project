from random import shuffle

def gen_number():
    a = ['1', '4', '5', '7', '9', '0']
    num = ['0444']
    for i in range(6):
        shuffle(a)
        num.append(a[0])
    print(''.join(num))
gen_number() 