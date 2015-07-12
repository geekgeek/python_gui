#https://www.youtube.com/watch?v=D24Vx3_IM8U
#https://www.youtube.com/watch?v=FqIKEW-S8W0

from Tkinter import *

root = Tk()

def doNothing():
    print "message to print"

#---MAIN MENU-----------
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

#-----Toolbar--------------

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="insert image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#-----Status Bar------

status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
