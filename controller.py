import note_book
import note
import view
from datetime import datetime, date
my_book=note_book.NoteBook('note_list.json') #создаю экземпляр записной книжки

my_book.open()

def start():
    while True:          
        choice=view.main_menu()
        # Добавить запись
        if choice==1:              
            new_id=note.Note.count_id
            new_name=input('Введите заголовок ')
            new_comment=input('Введите тело заметки ')
            new_date=datetime.now()
            my_book.add_note(note.Note(new_id,new_name,new_date,new_comment))
        # показать все записи    
        elif choice==2: 
            print('\n Записная книжка: ')            
            view.show_message_line(my_book.show_title())
            print(my_book) 
            while True: 
                submenu_choice=view.submenu_menu()
                #  показать запись
                if submenu_choice==1: 
                    index_id=int(input('Введите ID записи, которую хотите открыть: '))
                    my_book.full_note(index_id)
                # Найти запись по дате    
                elif submenu_choice==2: 
                    date_string=input(f'Введите дату, для поиска в формате: [ year-month-day] ')           
                    search_date = datetime.strptime(date_string,'%Y-%m-%d')
                    my_book.search_note(search_date)
                    
                # Изменить запись    
                elif submenu_choice==3: 
                    index_id=int(input('Введите номер записи, которую хотите изменить: '))
                    print(f' Запись № {index_id} открыта для редактирования ')
                    my_book.full_note(index_id)
                    new_name=input('Измените заголовк или пропустите пункт, чтоб оставить без изменений ')
                    new_comment=input('Измените содержимое заметки или пропустите пункт, чтоб оставить без изменений ')
                    new_date=datetime.now()
                    my_book.change_note(index_id,new_name,new_date,new_comment) 
                    print("Запись успешно отредактирована")  
                    
                # удалить запись    
                elif submenu_choice==4:  
                    index_id=int(input('Введите номер записи, которую хотите удалить: '))
                    if my_book.del_note(index_id):
                        print("Запись успешно удалена")
                    else:
                        print("Такого элемента нет в списке") 
                 #     Выход         
                elif submenu_choice==5:   
                    break 
        #Сохранить файл           
        elif choice==3: 
            my_book.save()
            print('Файл сохранен') 
        #Выход    
        elif choice==4: 
            return  