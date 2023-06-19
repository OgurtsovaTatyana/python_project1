import note_book
import view
import datetime
my_book=note_book.NoteBook('note_list.txt') #создаю экземпляр записной книжки
print(my_book.note_list)
my_book.open()

def start():
    while True:
        
        choice=view.main_menu()
        if choice ==1: #     1. Добавить запись
            
            new_id=input('Введите id ')
            new_name=input('Введите заголовок ')
            new_comment=input('Введите тело заметки ')
            new_date=datetime.datetime.now()
            my_book.add_note(new_id,new_name,new_date,new_comment)
            
        elif choice ==2: # показать все записи
            print('\n Записная книжка: ')
            mess="{:20}".format("id") + " | " + "{:20}".format("Заголовок") + " | " + "{:30}".format("дата") + " | " + "{:20}".format("тело заметки")  
            view.show_message(mess)
            print(my_book)
            
        # elif choice ==3:  #     . Найти запись
       
        # elif choice ==4: #     4. Изменить запись
        #     index=int(input('Введите номер записи, которую хотите изменить'))
        #     
        # elif choice ==5: #     5. Удалить запись
        #     index=int(input('Введите номер записи, которую хотите удалить '))
        #       
                  
        elif choice ==6: #     6. Сохранить файл
            my_book.save()
            print('Файл сохранен') 

        elif choice ==7: #     7.  Выход
            return  