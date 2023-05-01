from operator import itemgetter
from models import *

from View import *
import json

def Menu():
    while True:
        a = int(input("Введите действие:\
                    \n 1. Добавление новой заметки \
                    \n 2. Удаление заметки \
                    \n 3. Показать все заметки\
                    \n 4. Внести изменения в заметку\
                    \n 0. Выход\n "))
        # блок создания заметки
        if (a == 1):
            new_list = CreateNotepad.GetInfo()
            obj = Notepad(new_list[0],new_list[1],new_list[2])
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
        
        # блок удаления заметки
        if (a == 2):
            num_note = DelNotepad.GetInfo()
            try: 
                with open ('data.json', 'r') as json_file:
                    data = json.load(json_file)
                    len_first = len(data)
                    for i in data:
                        if i['id'] == num_note:
                            data.remove(i)
                    with open('data.json', 'w') as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                        f.truncate()
                        if (len_first>len(data)):
                            message = ShowToUser('Заметка удалена\n')
                            message.PrintInfo()
                            Menu()
                        else:
                            ShowToUser.PrintError()
                            Menu()        
            except:
                    ShowToUser.PrintError()
                    Menu()
        
        # блок вывода списка всех заметок
        if (a == 3):
            try: 
                with open ('data.json', 'r') as json_file:
                    data = json.load(json_file)
                    new_data = sorted(data, key= itemgetter("date_edit"))
                    for i in new_data:
                        obj = ShowToUser(i)
                        obj.PrintInfo()
                    print()
                    Menu()
            except:
                ShowToUser.PrintError()
                Menu()
        
        # блок изменения заметки
        if (a==4):
            try: 
                with open ('data.json', 'r') as json_file:
                    note_id = GetEdit.GetId()
                    data = json.load(json_file)
                    data_id = []
                    for i in data:
                        data_id.append(i['id'])
                    if note_id not in data_id:
                        ShowToUser.PrintError()
                        Menu()
                    else:
                        new_list = GetEdit.GetInfo()
                        for i in data:
                            if i['id'] == note_id:
                                i[new_list[0]] = new_list[1]
                                i['date_edit'] = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
                        with open('data.json', 'w') as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                            f.truncate()
                            Menu()        
            except:
                    ShowToUser.PrintError()
                    Menu()


        # блок выхода из меню и прекращения работы программы
        if (a == 0):
            obj = ShowToUser("The end")
            obj.PrintInfo()
            break
        
         
         
Menu()      