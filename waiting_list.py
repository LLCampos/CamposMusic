from helper_functions import *
from popups import *
from Tkinter import *

listamusica = 'Lista Musica.txt'

def waiting_list(waitingList):
    e = Entry(waitingList)
    e.pack()

    # 'Add Album' Button
    addbtn = Button(waitingList, text='Add Album',
                            command=lambda: addAlbumDeleteInput(e, listamusica, listbox))
    addbtn.pack()

    # List of albums
    scrollbar = Scrollbar(waitingList, orient='vertical')
    listbox = Listbox(waitingList, width=50, yscrollcommand=scrollbar.set, selectmode='extended')
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side='right', fill='y')
    listbox.pack(side='left', fill='both', expand=1)
    addStuff(listamusica, listbox)

    # Add 'Delete' Button
    delbtn = Button(waitingList, text='Delete', command=lambda: deleteAlbums(listamusica, listbox))
    delbtn.pack()

    # Add 'Edit' Button
    editbtn = Button(waitingList, text='Edit', command=lambda: Edit(listamusica, listbox))
    editbtn.pack()

    # Add 'Downloaded' Button
    downedbtn = Button(waitingList, text='Downloaded', command=lambda: changeColor(listbox, 'green'))
    downedbtn.pack()
