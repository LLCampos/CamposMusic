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

    def downloadPopup(listbox, site):
        goToSites(listbox, site)
        download.destroy()

    btn = Button(download, text='Go!', command=lambda: downloadPopup(listbox, v.get()))
    btn.pack()


def Downloaded(listamusica, listbox, color):

    path = Tk()
    path.title('CamposMusic - Path')
    path.wm_iconbitmap('favicon.ico')

    pathlabel = Label(path, text='Where it is?')
    pathlabel.pack()

    pathentry = Entry(path, width=55)
    pathentry.pack()

    def wherePopup(listamusica, listbox, color):
        inp = pathentry.get().encode('utf-8')
        addInfo(listamusica, listbox, inp, listbox.curselection()[0], 2)
        changeColor(listamusica, listbox, color)
        path.destroy()

    pathbutton = Button(path, text='Ok!', command=lambda: wherePopup(listamusica, listbox, color))
    pathbutton.pack()
