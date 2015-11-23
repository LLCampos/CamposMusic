import tkMessageBox
from constants import *


def addStuff(filename, listbox):
    """Inserts all albums in filename in listbox"""
    f = open(filename, 'r')
    albums = f.readlines()
    for album in albums:
        listbox.insert('end', album)
    f.close()


def addAlbum(inputuser, filename, listbox):
    """Adds inputuser to listbox and file filename"""
    listbox.insert('end', inputuser)
    f = open(filename, 'a')
    f.write(inputuser.encode('utf-8') + '\n')
    f.close


def addAlbumDeleteInput(e, listamusica, listbox):
    """Adds inputuser to listbox and to file filename
       Deletes text in Entry e"""
    addAlbum(e.get(), listamusica, listbox)
    e.delete(0, 'end')


def deleteAlbumFromFile(index, filename):
    """Delete album from file filename"""
    f = open(filename, 'r')
    albums = f.readlines()
    f.close()
    albums.pop(index)
    f = open(filename, 'w')
    for album in albums:
        f.write(album)
    f.close()


def deleteAlbums(filename, listbox, listboxi=False):
    """Delete album(s) from file and listbox"""
    indexes = reversed(listbox.curselection())
    for i in indexes:
        name_album = listbox.get(i)
        if tkMessageBox.askyesno('Delete', 'Are you sure you want to delete ' + name_album + '?'):
            if listboxi:
                transferToiPod(name_album, listboxi)
            listbox.delete(i)
            deleteAlbumFromFile(i, filename)


def transferToiPod(album, listboxi):
    if tkMessageBox.askyesno('', 'Do you want to transfer ' + album + ' to iPod list?'):
        addAlbum(album, listaipod, listboxi)


def editAlbumFromFile(index, filename, new_text):
    """Edits album from file"""
    f = open(filename, 'r')
    albums = f.readlines()
    f.close()
    albums[index] = new_text
    f = open(filename, 'w')
    for album in albums:
        f.write(album)
    f.close()


def editAlbum(filename, listbox, inp, index):
    """Edits album from file and listbox
    inp is the input of the user"""
    listbox.delete(index)
    listbox.insert(index, inp)
    editAlbumFromFile(index, filename, inp)


def changeColor(listbox, color):
    """Change the color of the selected listbox items"""
    for i in listbox.curselection():
        listbox.itemconfig(i, bg=color)
