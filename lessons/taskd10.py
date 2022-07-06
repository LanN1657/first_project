list = []
for i in range(1, 256):
    if i == 15 or i == 24 or i == 81 or i == 132 or i == 196 or i == 214:
        continue
    else:
        list.append(i)
print(list)