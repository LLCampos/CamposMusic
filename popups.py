from Tkinter import *
from helper_functions import *


def Edit(filename, listbox):
    edit = Tk()
    edit.title('CamposMusic - Edit')
    edit.wm_iconbitmap('favicon.ico')
    n = listbox.curselection()[0]
    v = listbox.get(n)
    editentry = Entry(edit, width=55)
    editentry.insert(0, v)
    editentry.pack()

    def pressOkEdit():
        editAlbum(filename, listbox, editentry.get().encode('utf-8'), n)
        edit.destroy()

    okbtn = Button(edit, text='OK', command=pressOkEdit)
    okbtn.pack()

    edit.mainloop()


def Download(listbox):
    download = Tk()
    download.title('CamposMusic - Download')
    download.wm_iconbitmap('favicon.ico')
    download.geometry('200x50')

    options = ['PirateBay', 'Kickass', 'Google', 'New Album Release']
    v = StringVar(download)
    v.set(options[0])

    optionmenu = OptionMenu(download, v, *options)
    optionmenu.pack()

    btn = Button(download, text='Go!', command=lambda: goToSites(listbox, v.get()))
    btn.pack()
