
import datetime


class Notepad():
    id = 0
    title = ""
    msg = ""
    date = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
  
    
    def __init__(self, id, title, msg, date = date):
        self.id = id
        self.title = title
        self.msg = msg
        self.date = date

    def __str__(self):
        return f" {self.id}, {self.title}, {self.msg}, {self.date} "
        
    def __repr__(self):
        return f" {self.id}, {self.title}, {self.msg}, {self.date} "
    
    def GetDict(self):
        return {
            'id':self.id,
            'title':self.title,
            'msg':self.msg,
            'date':self.date
        }
    

   