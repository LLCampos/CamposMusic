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
    f.write(inputuser + '\n')
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


def deleteAlbums(filename, listbox):
    """Delete album(s) from file and listbox"""
    indexes = reversed(listbox.curselection())
    for i in indexes:
        listbox.delete(i)
        deleteAlbumFromFile(i, filename)
