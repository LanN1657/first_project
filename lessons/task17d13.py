from random import randint
def unique_nums():
    a = []
    for i in range(100):
        b = randint(10, 50)
        a.append(b)
    c = set(a)
    a = list(c)
    print(a)
unique_nums()
