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
                print("Заметка добавлена")
                Menu()
        except:
            with open('data.json', 'w') as json_file:
                json.dump([obj.GetDict()], json_file, indent=2, ensure_ascii=False)
                print("Заметка добавлена")
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
                    print("Заметка удалена")
                    Menu()
                
        except:
                print('File does not exsist')
                print('Try again')
                Menu()
    
    if (a == 3):
        try: 
            with open ('data.json', 'r') as json_file:
                data = json.load(json_file)
                print(type(data))
                new_data = sorted(data, key= itemgetter("date"))
                for i in new_data:
                    print(i)
                Menu()
                
        except:
                print('File does not exsist')
                print('Try again')
                Menu()
        

    if (a == 0):
        return print("The end")

Menu()        