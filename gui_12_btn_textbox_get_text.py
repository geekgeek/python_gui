from Tkinter import *
#blank window
root = Tk()

#create label,textboxes and checkbox
label1 = Label(root, text="lb1")
label2 = Label(root, text="label2")

textbox1 = Entry(root)
textbox2 = Entry(root)


def getTextbox1Text():
    print textbox1.get()

def getTextbox2Text():
    print textbox2.get()

checkbox1 = Checkbutton(root, text="checbox1")

button1 = Button(root, text="call function", command=getTextbox1Text)

#Create alignments / sticky e = align to east
label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
button1.grid(row=2,column=1)

root.mainloop()
