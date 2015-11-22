from Tkinter import *
from ttk import *
from content import *

root = Tk()
root.title('CamposMusic')
root.wm_iconbitmap('favicon.ico')

n = Notebook(root)

waitingList = Frame(n)
ipod = Frame(n)

n.add(waitingList, text='WaitingList')
n.add(ipod, text='iPod')
n.pack()

content(ipod, waitingList)

root.mainloop()
