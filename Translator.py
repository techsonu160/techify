from tkinter import *
from translate import translators

def translate():
    translator=Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translator=translator.translate(var.get())
    var1.set(translation)

window=Tk()
window.title("Translatror")
#  creating a frame and grid to hide the content
mainframe=Frame(window)
mainframe._grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.pack(pady=100,padx=100)


window.mainloop()



