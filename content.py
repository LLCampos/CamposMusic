from helper_functions import *
from popups import *
from Tkinter import *
from constants import *


def content(iPod, waitingList, phone):

    ##### Phone #####

    entry_phone_list = Entry(phone, width=80)
    entry_phone_list.pack()

    # 'Add Album' Button
    addbtn_phone_list = Button(
        phone,
        text='Add Album',
        command=lambda: addAlbumDeleteInput(entry_phone_list, listaphone, listbox_phone_list)
    )
    addbtn_phone_list.pack()

    # List of albums
    scrollbar_phone_list = Scrollbar(phone, orient='vertical')
    listbox_phone_list = Listbox(phone, width=50, yscrollcommand=scrollbar_phone_list.set, selectmode='extended')
    scrollbar_phone_list.config(command=listbox_phone_list.yview)
    scrollbar_phone_list.pack(side='right', fill='y')
    listbox_phone_list.pack(side='left', fill='both', expand=1)
    addStuff(listaphone, listbox_phone_list)

    # Add 'Delete' Button
    delbtn_phone_list = Button(phone, text='Delete', command=lambda: deleteAlbums(listaphone, listbox_phone_list))
    delbtn_phone_list.pack()

    # Add 'Edit' Button
    editbtn_phone_list = Button(phone, text='Edit', command=lambda: Edit(listaphone, listbox_phone_list))
    editbtn_phone_list.pack()

    ##### IPOD #####
    # Entry
    e = Entry(iPod, width=80)
    e.pack()

    # 'Add Album' Button
    addbtn = Button(
        iPod,
        text='Add Album',
        command=lambda: addAlbumDeleteInput(e, listaipod, listbox)
    )
    addbtn.pack()

    # List of albums
    scrollbar = Scrollbar(iPod, orient='vertical')
    listbox = Listbox(iPod, width=50, yscrollcommand=scrollbar.set, selectmode='extended')
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side='right', fill='y')
    listbox.pack(side='left', fill='both', expand=1)
    addStuff(listaipod, listbox)

    # Add 'Delete' Button
    delbtn = Button(iPod, text='Delete', command=lambda: deleteAlbums(listaipod, listbox, listaphone, listbox_phone_list))
    delbtn.pack()

    # Add 'Edit' Button
    editbtn = Button(iPod, text='Edit', command=lambda: Edit(listaipod, listbox))
    editbtn.pack()

    ##### Waiting_List #####

    ew = Entry(waitingList, width=80)
    ew.pack()

    # 'Add Album' Button
    addbtnw = Button(
        waitingList,
        text='Add Album',
        command=lambda: addAlbumDeleteInput(ew, listamusica, listboxw)
    )
    addbtnw.pack()

    # List of albums
    scrollbarw = Scrollbar(waitingList, orient='vertical')
    listboxw = Listbox(waitingList, width=50, yscrollcommand=scrollbarw.set, selectmode='extended')
    scrollbarw.config(command=listboxw.yview)
    scrollbarw.pack(side='right', fill='y')
    listboxw.pack(side='left', fill='both', expand=1)
    addStuff(listamusica, listboxw)

    # Add 'Delete' Button
    delbtnw = Button(waitingList, text='Delete', command=lambda: deleteAlbums(listamusica, listboxw, listaipod, listbox))
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

    # Add 'Listened' Button
    liste = Button(waitingList, text='Listened', command=lambda: changeColor(listamusica, listboxw, 'plum3'))
    liste.pack()

    # Add 'Buy' Button
    liste = Button(waitingList, text='Buy', command=lambda: changeColor(listamusica, listboxw, 'yellow'))
    liste.pack()

    # Add 'Extra' Button
    extra = Button(waitingList, text='Extra', command=lambda: changeColor(listamusica, listboxw, 'orange'))
    extra.pack()
