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
        return f'{self.id:<10} | {self.name[:30]:<30} | {self.date.strftime("%d-%b-%Y"):<30} | {self.comment[:10]:<10}...'   
    
    def full_print(self): 
        return f''' 
            Запись #{self.id} 
            Заголовок: {self.name:}
            Дата создания/редактирования:{self.date.strftime("%c"):<30}
            Тело заметки:
            {self.comment}
            '''  