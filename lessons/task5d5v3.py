a = 0
for i in range(1, 20):
    if i <= 10:
        print(i, end = ' ') 
    else:
        a += 2
        i -= a
        print(i, end = ' ')