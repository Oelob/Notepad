from operator import itemgetter
from models import *

from View import *
import json

def Menu():
    a = int(input("Введите действие:\
                  \n 1. Добавление новой заметки \
                  \n 2. Удаление заметки \
                  \n 3. показать все заметки\
                  \n 0. Выход\n "))
    if (a == 1):
        list = CreateNotepad.GetInfo()
        obj = Notepad(list[0],list[1],list[2])
        try: 
           with open ('data.json', 'r') as json_file:
                data = json.load(json_file)
                data.append(obj.GetDict())
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    f.truncate()
                message = ShowToUser('Заметка создана\n')
                message.PrintInfo()
                Menu()
        except:
            with open('data.json', 'w') as json_file:
                json.dump([obj.GetDict()], json_file, indent=2, ensure_ascii=False)
                message = ShowToUser('Заметка создана\n')
                message.PrintInfo()
                Menu()


    if (a == 2):
        num_note = DelNotepad.GetInfo()
        try: 
            with open ('data.json', 'r') as json_file:
                data = json.load(json_file)
                for i in data:
                    if i['id'] == num_note:
                        data.remove(i)
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    f.truncate()
                    message = ShowToUser('Заметка удалена\n')
                    message.PrintInfo()
                    Menu()
                
        except:
                ShowToUser.PrintError()
                Menu()
    
    if (a == 3):
        try: 
            with open ('data.json', 'r') as json_file:
                data = json.load(json_file)
                new_data = sorted(data, key= itemgetter("date"))
                for i in new_data:
                    obj = ShowToUser(i)
                    obj.PrintInfo()
                    print()
                    # print(i)
                Menu()
                
        except:
               ShowToUser.PrintError()
               Menu()
        

    if (a == 0):
        obj = ShowToUser("The end")
        obj.PrintInfo()
         
Menu()        