def file():
    file1 = input('Введите название файла: ')
    with open(file1, 'w') as f:
        f.write('file.txt')
b = file()
b