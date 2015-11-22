from helper_functions import *
from popups import *
from Tkinter import *

listaipod = 'iPod.txt'


def iPod(iPod):
    # Entry
    e = Entry(iPod)
    e.pack()

    # 'Add Album' Button
    addbtn = Button(iPod, text='Add Album',
                            command=lambda: addAlbumDeleteInput(e, listaipod, listbox))
    addbtn.pack()

    # List of albums
    scrollbar = Scrollbar(iPod, orient='vertical')
    listbox = Listbox(iPod, width=50, yscrollcommand=scrollbar.set, selectmode='extended')
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side='right', fill='y')
    listbox.pack(side='left', fill='both', expand=1)
    addStuff(listaipod, listbox)

    # Add 'Delete' Button
    delbtn = Button(iPod, text='Delete', command=lambda: deleteAlbums(listaipod, listbox))
    delbtn.pack()

    # Add 'Edit' Button
    editbtn = Button(iPod, text='Edit', command=lambda: Edit(listaipod, listbox))
    editbtn.pack()

