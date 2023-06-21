#Заметка должна содержать:
# идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. 
import datetime
class Note:
    count_id=0
    def __init__(self,id:int, name:str,date:datetime, comment:str):
        self.id=id # идентификатор
        self.name=name #заголовок
        self.date=date # дата создания
        self.comment=comment #тело заметки
        
    def __str__(self): #печать при использовании print(заметка)
        return f'{self.id:<20} | {self.name:<20} | {self.date.strftime("%c"):<30} | {self.comment:<20}'    