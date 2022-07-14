def profile_salary(name, salary=5000):
    print(name, '-', salary)

name = input('Введите своё имя: ')
salary = input('Введите свою зарплату: ')

if salary:
    salary = int(salary)
    profile_salary(name, salary)
else:
    profile_salary(name)