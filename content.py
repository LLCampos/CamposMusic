from helper_functions import *
from popups import *
from Tkinter import *
from constants import *


def content(iPod, waitingList):
    ##### IPOD #####
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

    ##### Waiting_List #####

    ew = Entry(waitingList)
    ew.pack()

    # 'Add Album' Button
    addbtnw = Button(waitingList, text='Add Album',
                            command=lambda: addAlbumDeleteInput(ew, listamusica, listboxw))
    addbtnw.pack()

    # List of albums
    scrollbarw = Scrollbar(waitingList, orient='vertical')
    listboxw = Listbox(waitingList, width=50, yscrollcommand=scrollbarw.set, selectmode='extended')
    scrollbarw.config(command=listboxw.yview)
    scrollbarw.pack(side='right', fill='y')
    listboxw.pack(side='left', fill='both', expand=1)
    addStuff(listamusica, listboxw)

    # Add 'Delete' Button
    delbtnw = Button(waitingList, text='Delete', command=lambda: deleteAlbums(listamusica, listboxw, listbox))
    delbtnw.pack()

    # Add 'Edit' Button
    editbtnw = Button(waitingList, text='Edit', command=lambda: Edit(listamusica, listboxw))
    editbtnw.pack()

    # Add 'Downloaded' Button
    downedbtn = Button(waitingList, text='Downloaded', command=lambda: changeColor(listamusica, listboxw, 'green'))
    downedbtn.pack()

    # Add 'Download' Button
    downbtn = Button(waitingList, text='Download', command=lambda: Download(listboxw))
    downbtn.pack()

    # Add 'Problems' Button
    prob = Button(waitingList, text='Problems', command=lambda: changeColor(listamusica, listboxw, 'indian red'))
    prob.pack()
