#CREATE GUI WITH PYTHON
#https://www.youtube.com/watch?v=Ko4EPJ8DDjg

from Tkinter import *
#blank window
root = Tk()

#fill

#label
TheLabel = Label(root, text='GUI TEXT', bg='red', fg="white")
TheLabel.pack()

thelabel2 = Label(root, text='GUI TEXT2', bg='green', fg="black")
thelabel2.pack(fill=X)

thelabel3 = Label(root, text='GUI TEXT3', bg='blue', fg="white")
thelabel3.pack(side=LEFT, fill=Y)

root.mainloop()
