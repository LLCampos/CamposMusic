from Tkinter import *
from ttk import *
from waiting_list import *
from iPod import *

root = Tk()
root.title('CamposMusic')
root.wm_iconbitmap('favicon.ico')

n = Notebook(root)

waitingList = Frame(n)
ipod = Frame(n)

n.add(waitingList, text='WaitingList')
n.add(ipod, text='iPod')
n.pack()

waiting_list(waitingList)
iPod(ipod)


root.mainloop()
