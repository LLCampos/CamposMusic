import Tkinter
from helper_functions import *
from popups import *


listamusica = 'Lista Musica.txt'

window = Tkinter.Tk()
window.title('CamposMusic')
window.wm_iconbitmap('favicon.ico')

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
listbox.pack(side='left', fill='both', expand=1)
addStuff(listamusica, listbox)

# Add 'Delete' Button
delbtn = Tkinter.Button(window, text='Delete', command=lambda: deleteAlbums(listamusica, listbox))
delbtn.pack()

# Add 'Edit' Button
editbtn = Tkinter.Button(window, text='Edit', command=lambda: Edit(listamusica, listbox))
editbtn.pack()

# Add 'Downloaded' Button
downedbtn = Tkinter.Button(window, text='Downloaded', command=lambda: changeColor(listbox, 'green'))
downedbtn.pack()


window.mainloop()
