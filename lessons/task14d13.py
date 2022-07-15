order_food = input('''Что хотите покушать?
''')
order_drink = input('''Чего желаете выпить?
''')

def order():
    with open('menu.txt', 'w') as f:
        f.write(order_food)
    with open('menu.txt', 'a') as f:
        f.write( order_drink)
order()