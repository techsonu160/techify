from tkinter import *


from time import strftime


techno=tkinter.Tk()
techno.title("Clock by pythonhub")

def time():
    string=strftime('"%H:%M:%S %p')
    lb1.config(text=string)
    lb1.after(1000,time)

lb1=Label(techno,font=('lucida',40,'bold'),
                    background='red',
                    foreground='white')
lb1.pack(anchor='center')
time()
techno.mainloop()