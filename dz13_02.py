# Створи код де при натисканні на кнопку рамка навколо твоєї кнопки
# буде міняти свій колір на рандомний зі списку кольорів.
from tkinter import *
import random

window = Tk()
window.title("Веселкова кнопка")
window.geometry("250x100")

def randomcolor():
    a=[]
    a = [hex(random.randint(0,255)).strip("0x").zfill(2),hex(random.randint(0,255)).strip("0x").zfill(2),hex(random.randint(0,255)).strip("0x").zfill(2)]
    st="".join(a)
    return st
#.zfill() - додає нулі на початок доки стріенга не буде довжиною вказаною в дужках

frame = Frame(bg=f'#{randomcolor()}', bd=10)
frame.pack()

def change():
    frame.config(bg=f'#{randomcolor()}')
    frame.pack()

button = Button(frame,text="Змінити колір", command=change)
button.pack()

window.mainloop()