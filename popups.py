import Tkinter
from helper_functions import *


def Edit(filename, listbox):
    edit = Tkinter.Tk()
    n = listbox.curselection()[0]
    v = listbox.get(n)
    editentry = Tkinter.Entry(edit)
    editentry.insert(0, v)
    editentry.pack()

    def pressOkEdit():
        editAlbum(filename, listbox, editentry.get(), n)
        edit.destroy()

    okbtn = Tkinter.Button(edit, text='OK', command=pressOkEdit)
    okbtn.pack()

    edit.mainloop()
