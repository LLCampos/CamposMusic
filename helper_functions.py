import tkMessageBox
import webbrowser
from constants import *


def addStuff(filename, listbox):
    """Updates all albums listbox"""
    listbox.delete(0, 'end')
    f = open(filename, 'r')
    albums = f.readlines()
    albums = [album.strip().split(',') for album in albums]
    for album in albums:
        listbox.insert('end', album[0])
        if album[1] == '$g':
            listbox.itemconfig('end', bg='green')
        elif album[1] == '$r':
            listbox.itemconfig('end', bg='indian red')
        elif album[1] == '$p':
            listbox.itemconfig('end', bg='plum3')
        else:
            listbox.itemconfig('end', bg='white smoke')
    f.close()


def addAlbum(inputuser, filename, listbox):
    """Adds inputuser to listbox and file filename"""
    f = open(filename, 'a')
    f.write(inputuser.encode('utf-8') + ',\n')
    f.close()
    addStuff(filename, listbox)


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
    sign = albums[index].strip().split(',')[1]
    albums[index] = new_text + ',' + sign + '\n'
    f = open(filename, 'w')
    for album in albums:
        f.write(album)
    f.close()


def editAlbum(filename, listbox, inp, index):
    """Edits album from file and listbox
    inp is the input of the user"""
    editAlbumFromFile(index, filename, inp)
    addStuff(filename, listbox)


def addSign(filename, listbox, sign, i):
    """Adds sign to album in file filename"""
    f = open(filename, 'r')
    albums = f.readlines()
    f.close()
    name_album = albums[i].strip().split(',')[0]
    albums[i] = name_album + ',' + sign + '\n'
    f = open(filename, 'w')
    for album in albums:
        f.write(album)
    f.close()


def changeColor(filename, listbox, color):
    """Change the color of the selected listbox items"""
    for i in listbox.curselection():
        if listbox.itemcget(i, 'bg') != color:
            if color == 'green':
                addSign(filename, listbox, '$g', i)
            elif color == 'indian red':
                addSign(filename, listbox, '$r', i)
            elif color == 'plum3':
                addSign(filename, listbox, '$p', i)
        else:
            addSign(filename, listbox, '', i)
    addStuff(filename, listbox)


def goToSite(album, site):
    """Does search in site of album"""
    album = album.replace(' ', '%20')
    if site == 'PirateBay':
        url = 'https://arrr.xyz/search/' + album + '/0/99/0'
    elif site == 'Kickass':
        url = 'http://katproxy.is/usearch/' + album
    elif site == 'Google':
        url = 'https://www.google.pt/webhp?hl=pt-PT#hl=pt-PT&q=' + album + '+(rar+|+zip)'
    elif site == 'New Album Release':
        url = 'http://newalbumreleases.net/?s=' + album
    webbrowser.open(url)


def goToSites(listbox, site):
    """Does search in site of all items selected is listbox"""
    indexes = listbox.curselection()
    for index in indexes:
        goToSite(listbox.get(index), site)
