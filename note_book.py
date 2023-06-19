#Заметка должна содержать:
# идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. 
import datetime
class Note:
    id=0
    def __init__(self,id:int,name:str,date:datetime, comment:str):
        #self.id=id
        self.name=name #заголовок
        self.date=date # дата создания
        self.comment=comment #тело заметки
    def __str__(self): #печать при использовании print(заметка)
        return f'{self.id:<20} | {self.name:<20} | {self.date.strftime("%c"):<30} | {self.comment:<20}'    


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
                                             
    def save(self):
        data=[]
        with open(self.path,'w',encoding='UTF-8') as file:   
            for note in self.note_list:
                    line=f'{note.id};{note.name};{note.date};{note.comment}'
                    data.append(line)
                    text='\n'.join(data)
            file.write(text)

    def add_note(self,new_id:int,new_name:str,new_date,new_comment:str):
        Note.id+=Note.id
        self.note_list.append(Note(new_id,new_name,new_date,new_comment)) 
   