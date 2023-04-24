
import datetime


class Notepad():
    id = 0
    title = ""
    msg = ""
    data = none
    
    def __init__(self, id, title, msg, data):
        self.id = id
        self.title = title
        self.msg = msg
        self.data = datetime.now()
    
    