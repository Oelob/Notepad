
import datetime



class Notepad():
    id = 0
    title = ""
    msg = ""
    date_create = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    date_edit = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    
    def __init__(self, id, title, msg, date_create = date_create, date_edit = date_edit):
        self.id = id
        self.title = title
        self.msg = msg
        self.date_create = date_create
        self.date_edit = date_edit

    def __str__(self):
        return f" {self.id}, {self.title}, {self.msg}, {self.date_create}, {self.date_edit} "
        
    def __repr__(self):
        return f" {self.id}, {self.title}, {self.msg}, {self.date_create}, {self.date_edit} "
    
    def GetDict(self):
        return {
            'id':self.id,
            'title':self.title,
            'msg':self.msg,
            'date_create':self.date_create,
            'date_edit':self.date_edit
        }

   