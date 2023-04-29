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
        result = int(input("id заметки для удаления "))
        return result

#class CreateNotepadIter():  