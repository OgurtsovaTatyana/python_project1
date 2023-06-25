import json
import note
from datetime import datetime,date

class NoteBook:
    def __init__(self,path:str):
        self.path=path
        self.note_list=[]
        self.open()
    def __str__(self): #печать при использовании print(книга)
        result=''
        i=1
        for note  in self.note_list:
            result+=(f'{i:<10} | {note} \n')
            i+=1
        return result   
    def show_title(self)->str:
        return f'{"{:10}".format("№")} | {"{:10}".format("id")} | {"{:30}".format("Заголовок")} | {"{:30}".format("дата")} | {"{:20}".format("тело заметки")}'  

    def open(self):
        self.note_list=[]
        with open(self.path, "r") as file_json: # открытие файла note_list.json для чтения
            data_line = json.load(file_json)# преобразование данных JSON в объекты Python (список)         
        index_id=1000
        for item in data_line:
            new_note=item.split(';')
            self.note_list.append(note.Note( index_id, new_note[1], datetime.strptime(new_note[2], '%Y-%m-%d %H:%M:%S.%f'), new_note[3]))
            index_id+=1
        note.Note.count_id=index_id
        
    def search_note(self,search_date:datetime):
        search=True
        print(f'Записи от :{search_date.date()}')
        i=1
        for item in self.note_list: 
            if item.date.date()==search_date.date():
                if i<2:
                    self.show_title()
                print(f'{i:<10} | {item}') 
                i+=1
                search=False         
        if search:
            print("не найдены")  
                         
    def add_note(self,new_note: note.Note):
        self.note_list.append(new_note) 
        note.Note.count_id+=1
        print("Запись успешно добавлена") 
        
    def change_note(self,index_id:int,new_name:str,new_date,new_comment:str):  
        if index_id>=1000 & index_id < note.Note.count_id:
            for item_note in self.note_list:
                if item_note.id==index_id:
                    if new_name:                        
                        item_note.name=new_name
                    if new_comment:                        
                        item_note.comment=new_comment
                    item_note.date=new_date
                    break
        else: print('записи с таким ID не найдено')  
        
         
            
    def del_note(self,index_id:int):
        if index_id>=1000 & index_id < note.Note.count_id:
            i=0
            for item in self.note_list:                
                if item.id==index_id:
                    self.note_list.pop(i)
                    break 
                i+=1
            return True
        else:
            return False
          
             
    def save(self):
        data=[]
        with open(self.path, 'w') as file_json:
            for note in self.note_list:
                line=f'{note.id};{note.name};{note.date};{note.comment}'
                data.append(line)                   
            json.dump(data,file_json)
        print("записная книга сохранена")
        
            
    def full_note(self,index_id:int):
        if index_id>=1000 & index_id < note.Note.count_id:
            for item_note in self.note_list:
                if item_note.id==index_id:            
                    print(note.Note.full_print(item_note))
        else: print('записи с таким ID не найдено')
        
   
        

   
  