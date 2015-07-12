#https://www.youtube.com/watch?v=IYHJRnVOFlw

from Tkinter import *

class guiClass:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()

        self.button1 = Button(frame1, text="print message", command=self.printMessage)
        self.button1.pack(side=LEFT)

        self.button2 = Button(frame1, text="quit", command=frame1.quit)
        self.button2.pack(side=LEFT)

    def printMessage(self):
        print("worked")



root = Tk()

b = guiClass(root)
root.mainloop()
