


class CreateNotepad():
    def GetInfo():
        
        result = []
        id = int(input("Введите ID "))
        title = input("Введите заголовок заметки ")
        msg = input("Введите текст заметки ")
        result.append(id)
        result.append(title)
        result.append(msg)
        return result

class DelNotepad():

    def GetInfo():
        result = 0
        result = int(input("Введите id заметки для удаления "))
        return result

class ShowToUser():
    message = ''
    def __init__(self, message):
        self.message = message

    def PrintInfo(self):
        print(self.message)
    
    def PrintError():
        message = 'File does not exsist\nTry again'
        print(message)

class GetEdit():
    def GetId():
        res = int(input('Введите id заметки, которую хотите изменить: '))
        return res

    def GetInfo():
        result = []
        # id = int(input('Введите id заметки, которую хотите изменить: '))
        # result.append(id)
        elemet = int(input('Выберите элемент заметки, которую хотите изменить:\
                           \n 1. id\
                           \n 2. title\
                           \n 3. msg '))
        if elemet == 1: 
            result.append('id') 
            result.append(int(input('Введите новое значение: ')))
        if elemet == 2: 
            result.append('title')
            result.append(input('Введите новое значение: '))
        if elemet == 3: 
            result.append('msg')
            result.append(input('Введите новое значение: '))
        return result
        