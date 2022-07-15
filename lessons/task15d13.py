file_name = input('Введите имя файла: ')
def create_file():
    with open(file_name, 'w') as f:
        f.write('Файл успешно создан!')
create_file()