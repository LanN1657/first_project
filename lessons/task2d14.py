dict1 = {}
login1 = []

def shadow(function):
    
    def wrapper():
        function()
        for i in dict1.keys():
            for j in i:
                login1.append(ord(j))
        for k in dict1.values():
            password = k
        print('''
        
Имя пользователя:''')
        for i in login1:
            print(i, end='')
        print('''

Пароль:''')
        print(chr(password))
        


    return wrapper



@shadow
def login_pass():
    login = input('Введите свой логин: ')
    password = int(input('Введите пароль (пароль нужно вводить числами!): '))
    dict1[login] = password
    
login_pass()
