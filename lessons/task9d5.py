j = 0
b = 0
for i in range(-100, 100):
    if i % 13 == 0 and i % 2 == 0:
        j += 1
        i = i ** 2
        print(i)

for a in range(-100, 100, 7):
    if a % 2 == 1:
        b += 1
        print(a)
print(j, 'из первого условия, и', b, 'из второго условия')