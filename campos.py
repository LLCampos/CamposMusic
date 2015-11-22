import Tkinter
from helper_functions import *


listamusica = 'Lista Musica.txt'

window = Tkinter.Tk()

e = Tkinter.Entry(window)
e.pack()

btn = Tkinter.Button(window, text='Add Album',
                     command=lambda: addAlbumDeleteInput(e, listamusica, listbox))
btn.pack()

listbox = Tkinter.Listbox(window, width=50)
listbox.pack()
addStuff(listamusica, listbox)

window.mainloop()
