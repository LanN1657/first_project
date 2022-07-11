def choice_to_number(choice):
    if choice == 'Usain':
        return 1
    elif choice == 'Me':
        return 2
    elif choice == 'Aybek':
        return 3
def number_to_choice(number):
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Aybek') == 3
    if number == 1:
        return 'Usain'
    elif number == 2:
        return 'Me'
    elif number == 3:
        return 'Aybek'
def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Aybek'
    print('YOUR CODE IS CORRECT!')
test_number_to_choice()