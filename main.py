from Notepad import *
from View import *


# a = Notepad(1, "new", "k;lk;l")
# print(a.__dict__)

a = input("Введите действие: ")

if (a == 1):
    list = View.CreatedNotepad()

for i in list:
    print(i)
