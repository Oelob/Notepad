from models import *

from View import *
import json

def Menu():
    a = int(input("Введите действие: "))
    if (a == 1):
        list = CreateNotepad.GetInfo()
        obj = Notepad(list[0],list[1],list[2])
        print(obj)
        try: 
           with open ('data.json', 'r') as json_file:
                data = json.load(json_file)
                print(data)
                data.append(obj.GetDict())
                print(data)
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
                    f.truncate()
        except:
            with open('data.json', 'w') as json_file:
                json.dump([obj.GetDict()], json_file, indent=2, ensure_ascii=False)
           


    if (a == 2):
        try: 
            with open ('data.json', 'r') as json_file:
                data = json.load(json_file)
                print(data)
                data.append(obj.GetDict())
                print(data)
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
                f.truncate()
        except:
                print('File does not exsist')
                print('Try again')
                Menu()
        # num_note = DelNotepad.GetInfo()
        # for item in obj.items():
        #     if  == num_note:
        #         obj[num_note]

Menu()        

# list = CreateNotepad.GetInfo()
# obj = Notepad(list[0],list[1],list[2])
# print(obj.GetDict())
# print(json.dumps(obj.__dict__))
# with open('data.json', 'w') as f:
    
#     json.dump([obj.__dict__], f, indent=2, ensure_ascii=False)
   
    

# with open('data.json', 'r') as file:
#     data = json.load(file)
# print(data)
