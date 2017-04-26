from Tkinter import *
from ttk import *
from content import *

root = Tk()
root.title('CamposMusic')

n = Notebook(root)

waitingList = Frame(n)
ipod = Frame(n)
phone = Frame(n)

n.add(waitingList, text='WaitingList')
n.add(ipod, text='iPod')
n.add(phone, text='Phone')
n.pack()

content(ipod, waitingList, phone)

root.mainloop()
