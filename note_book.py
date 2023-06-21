import json
import note
import datetime


class NoteBook:
    def __init__(self,path:str):
        self.path=path
        self.note_list=[]
        self.open()
    def __str__(self): #печать при использовании print(книга)
        result=''
        for note  in self.note_list:
            result+=(f'{note} \n')
        return result   
    
    
    def open(self):
        self.note_list=[]
        with open(self.path, "r") as file_json: # открытие файла note_list.json для чтения
            data_line = json.load(file_json)# преобразование данных JSON в объекты Python (список)         
        index_id=1
        for item in data_line:
            new_note=item.split(';')
            self.note_list.append(note.Note( index_id, new_note[1], datetime.datetime.strptime(new_note[2], '%Y-%m-%d %H:%M:%S.%f'), new_note[3]))
            index_id+=1
        note.Note.count_id=index_id
        
    def search_note(self,search_date:datetime):
        for note in self.note_list:
            if note.date==search_date:
                print(note)  
            else:
                print("Такой записи нет в книге") 
                
                 
                         
    def add_note(self,new_note):
        self.note_list.append(new_note) 
        note.Note.count_id+=1
        print("Запись успешно добавлена") 
        
    def change_note(self,idnex_id:int,new_name:str,new_date,new_comment:str):    
        if new_name:
            note =self.note_list[idnex_id]
            note.name=new_name
        if new_comment:
            note =self.note_list[idnex_id]
            note.comment=new_comment
        print("Запись отредактирована") 
            
    def del_note(self,index_id:int):
        if index_id < len(self.note_list):
            self.note_list.pop(index_id)
            for index in range(index_id,len(self.note_list)):
                self.note_list[index].id=index+1
            note.Note.count_id=len(self.note_list)
            print("Запись успешно удалена")
        else:
            print("такого элемента нет в списке")  
             
    def save(self):
        data=[]
        with open(self.path, 'w') as file_json:
            for note in self.note_list:
                line=f'{note.id};{note.name};{note.date};{note.comment}'
                data.append(line)                   
            json.dump(data,file_json)
        print("записная книга сохранена")      
            
        

   
  