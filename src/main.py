from tkinter import Tk, Label
from connect4 import Connect4Party

screen = Tk()

screen.title('wesh')
screen.minsize(width=500, height=500)

Label(screen, text='Wesh les mecs').pack()

screen.config()
screen.mainloop()

# party = Connect4Party([{'id': 'fdp', 'case': 'red'}, {'id': 'fdp', 'case': 'yellow'}])
