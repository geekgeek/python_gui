#CREATE GUI WITH PYTHON

from Tkinter import *
#blank window
root = Tk()

#label
#TheLabel = Label(root, text='this is easy')
#TheLabel.pack()

Topframe = Frame(root)
Topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(Topframe, text="text", fg="red")
button1.pack()



#loop / show window
root.mainloop()
