menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['besh_barmak'] = 130
print(menu)
menu_lagman = {'lagman': 135}
menu.update(menu_lagman)
print(menu)
menu.pop('borsh')
print(menu)