a = 17391
b = 546
c = 934

d = a % 17
e = b % 17
f = c % 17

if d < e and  d < f:
   print('Самое маленькое число', d)
elif e < d and  e < f:
   print('Самое маленькое число', e)
else:
   print('Самое маленькое число', f)