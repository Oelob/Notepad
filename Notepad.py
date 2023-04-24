
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
    
   