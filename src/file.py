# code by audiotore (github)


# This is our filemanager.
# It may look limited at first
# but it actually does a surprising amount of stuff.
# If you ever need to open up a windows application
# you can do so by using the filemanager and opening
# the windows executable :)

from tkinter import *
from tkinter import filedialog
import os

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    os.startfile(filepath)

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()