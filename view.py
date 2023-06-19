import main_menu_text

def main_menu() ->int:
    print(main_menu_text.main_menu)
    length_menu=len(main_menu_text.main_menu.split('\n'))
    while True:
        choice=input('Выберите пункт меню:')
        if choice.isdigit() and 0<int(choice)<=length_menu:
            return int(choice)
        else:
            print(f'Введите Число от 1 до {length_menu}')

def show_message(message:str):
    print('-'*len(message))
    print(message)
    print('-'*len(message))