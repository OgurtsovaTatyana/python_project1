import note_book
import note
import view
import datetime
my_book=note_book.NoteBook('note_list.json') #создаю экземпляр записной книжки
# print(my_book.note_list)
my_book.open()

def start():
    while True:
        
        choice=view.main_menu()
        if choice==1: #     1. Добавить запись
             
            new_id=note.Note.count_id
            new_name=input('Введите заголовок ')
            new_comment=input('Введите тело заметки ')
            new_date=datetime.datetime.now()
            my_book.add_note(note.Note(new_id,new_name,new_date,new_comment))
            
        elif choice==2: # показать все записи
            print('\n Записная книжка: ')
            mess="{:20}".format("id") + " | " + "{:20}".format("Заголовок") + " | " + "{:30}".format("дата") + " | " + "{:20}".format("тело заметки")  
            view.show_message_line(mess)
            print(my_book)
            
        elif choice ==3:  #     . Найти запись по дате
            search_date=datetime(input('Введите дату, для поиска'))
            my_book.search_note(search_date)
       
        elif choice==4: #     4. Изменить запись
            index_id=int(input('Введите номер записи, которую хотите изменить'))
            print(f' запись № {index_id} открыта для редактирования:')
            print (my_book.note_list[index_id-1])
            new_name=input('Измените заголовк или пропустите пункт, чтоб оставить без изменений ')
            new_comment=input('Измените содержимое заметки или пропустите пункт, чтоб оставить без изменений ')
            new_date=datetime.datetime.now()
            my_book.change_note(index_id-1,new_name,new_date,new_comment)     
           
            
        elif choice ==5: #     5. Удалить запись
            index_id=int(input('Введите номер записи, которую хотите удалить '))
            my_book.del_note(index_id-1)  
                  
        elif choice==6: #     6. Сохранить файл
            my_book.save()
            print('Файл сохранен') 

        elif choice==7: #     7.  Выход
            return  