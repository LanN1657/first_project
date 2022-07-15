from random import randint
a = []
b = []
def unique_nums(function):

    def wrapper():
        function()
        a = b
        a = set(a)   
        a = list(a)
        print(a)
    return wrapper

@unique_nums
def rand_nums():
    for i in range(100):
        c = randint(10, 50)
        b.append(c)
rand_nums()
