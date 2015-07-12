#https://www.youtube.com/watch?v=PSm-tq5M-Dc

from Tkinter import *

root = Tk()

def doNothing():
    print "message to print"

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="new project", command=doNothing)
subMenu.add_command(label="new ...", command=doNothing)

subMenu.add_separator()

subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
