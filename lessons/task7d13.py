def main_func():
    def func():
        print('Я вложенная функция.')
    print('Я главная функция.')
    func()
main_func()