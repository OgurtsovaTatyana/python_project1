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
        # print(data_line)
        for item in data_line:
            new_note=item.split(';')
            self.note_list.append(note.Note( new_note[0], new_note[1], datetime.datetime.strptime(new_note[2], '%Y-%m-%d %H:%M:%S.%f'), new_note[3]))
        # print(self.note_list)   
                         
    def save(self):
        data=[]
        with open(self.path, 'w') as file_json:
            for note in self.note_list:
                line=f'{note.id};{note.name};{note.date};{note.comment}'
                data.append(line)
                # text='\n'.join(data)        
            json.dump(data,file_json)
                  
            
        

    # def add_note(self,new_id:int,new_name:str,new_date,new_comment:str):
    #     self.note_list.append(Note(new_id,new_name,new_date,new_comment)) 
    def add_note(self,new_note):
        self.note_list.append(new_note) 