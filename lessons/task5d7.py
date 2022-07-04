set1 = set()
a = 0 
while a != 10:
    b = int(input('Введите число: '))
    set1.add(b)
    a += 1
set2 = frozenset(set1)
print(set2)
