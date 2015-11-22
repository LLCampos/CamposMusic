import Tkinter
from helper_functions import *


listamusica = 'Lista Musica.txt'

window = Tkinter.Tk()

e = Tkinter.Entry(window)
e.pack()

# 'Add Album' Button
btn = Tkinter.Button(window, text='Add Album',
                     command=lambda: addAlbumDeleteInput(e, listamusica, listbox))
btn.pack()

# List of albums
scrollbar = Tkinter.Scrollbar(window, orient='vertical')
listbox = Tkinter.Listbox(window, width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side='right', fill='y')
listbox.pack()
addStuff(listamusica, listbox)





window.mainloop()
