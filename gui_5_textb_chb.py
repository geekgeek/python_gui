#https://www.youtube.com/watch?v=-nmzq3xiZ6I
#https://www.youtube.com/watch?v=wNBqM28MMjs

from Tkinter import *


#blank window
root = Tk()

#create label,textboxes and checkbox
label1 = Label(root, text="lb1")
label2 = Label(root, text="label2")

textbox1 = Entry(root)
textbox2 = Entry(root)

checkbox1 = Checkbutton(root, text="checbox1")


#Create alignments / sticky e = align to east
label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)

checkbox1.grid(columnspan=2)



root.mainloop()
