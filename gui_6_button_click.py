#https://www.youtube.com/watch?v=qWnE-yp6wzU

from Tkinter import *
root = Tk()

def printName():
    print "hello this is function"
    
button1 = Button(root, text="call function", command=printName)
button1.pack()
    


root.mainloop()
