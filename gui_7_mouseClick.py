#https://www.youtube.com/watch?v=XkCbinbgbdw
#Catches when mouse button is clicked
from Tkinter import *
root = Tk()

def leftclick(event):
    print "left"

def rightclick(event):
    print "right"
    
def middleclick(event):
    print "middle"

frame1 = Frame(root, width=300, height=400)

frame1.bind("<Button-1>", leftclick)
frame1.bind("<Button-2>", middleclick)
frame1.bind("<Button-3>", rightclick)
frame1.pack()

root.mainloop()
