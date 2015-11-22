import Tkinter
from helper_functions import *


listamusica = 'Lista Musica.txt'

window = Tkinter.Tk()

e = Tkinter.Entry(window)
e.pack()

# 'Add Album' Button
addbtn = Tkinter.Button(window, text='Add Album',
                                command=lambda: addAlbumDeleteInput(e, listamusica, listbox))
addbtn.pack()

# List of albums
scrollbar = Tkinter.Scrollbar(window, orient='vertical')
listbox = Tkinter.Listbox(window, width=50, yscrollcommand=scrollbar.set, selectmode='extended')
scrollbar.config(command=listbox.yview)
scrollbar.pack(side='right', fill='y')
listbox.pack()
addStuff(listamusica, listbox)

# Add 'Delete' Button
delbtn = Tkinter.Button(window, text='Delete', command=lambda: deleteAlbums(listamusica, listbox))
delbtn.pack()


window.mainloop()
