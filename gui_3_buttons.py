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

button1 = Button(Topframe, text="text1", fg="red")
button2 = Button(Topframe, text="text2", fg="red")
button3 = Button(Topframe, text="text3", fg="red")
button4 = Button(bottomframe, text="text4")

button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")
button4.pack(side="bottom")



#loop / show window
root.mainloop()
