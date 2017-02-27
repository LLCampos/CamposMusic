from Tkinter import *
from helper_functions import *


def Edit(filename, listbox):
    edit = Tk()
    edit.title('CamposMusic - Edit')
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
    download.geometry('200x50')

    options = ['PirateBay', 'Kickass', 'RUTracker', 'Google', 'New Album Release']
    v = StringVar(download)
    v.set(options[0])

    optionmenu = OptionMenu(download, v, *options)
    optionmenu.pack()

    def downloadPopup(listbox, site):
        goToSites(listbox, site)
        download.destroy()

    btn = Button(download, text='Go!', command=lambda: downloadPopup(listbox, v.get()))
    btn.pack()
