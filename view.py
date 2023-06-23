import main_menu_text
import submenu_text

def main_menu() ->int:
    print(main_menu_text.main_menu)
    length_menu=len(main_menu_text.main_menu.split('\n'))
    while True:
        choice=input('Выберите пункт меню:')
        if choice.isdigit() and 0<int(choice)<length_menu:
            return int(choice)
        else:
            print(f'Введите Число от 1 до {length_menu-2}')
def submenu_menu() ->int:
    print(submenu_text.submenu)
    length_menu=len(submenu_text.submenu.split('\n'))
    while True:
        
        submenu_choice=input('Выберите действие:')
        if submenu_choice.isdigit() and 0<int(submenu_choice)<length_menu:
            return int(submenu_choice)
        else:
            print(f'Введите Число от 1 до  {length_menu-2}')

def show_message_line(message:str):
    print('-'*len(message))
    print(message)
    print('-'*len(message))