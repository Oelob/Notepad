class CreateNotepad():
    
    def GetInfo():
        
        result = []
        id = input("Введите ID")
        title = input("Введите заголовок заметки")
        msg = input("Введите текст заметки")
        result.append(id)
        result.append(title)
        result.append(msg)
        return result

class DelNotepad():

    def GetInfo():
        result = 0
        id = input("Введите ID заметки которую нужно удалить")
        return result

#class CreateNotepadIter():  