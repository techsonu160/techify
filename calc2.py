from tkinter import *
import tkinter.messagebox as tsmg
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
                tsmg.showerror("Error",e)



        scvalue.set(value)
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() +text)
        screen.update()

anu_root=Tk()
anu_root.geometry("1000x1200")

anu_root.title("code by sonu")
anu_root.wm_iconbitmap("calc3.png")
scvalue=StringVar()
scvalue.set("")
screen=Entry(anu_root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=10,ipady=10,padx=12)
f1=Frame(anu_root,bg="grey")
f1.pack()
b=Button(f1,text="9",padx=28,pady=12,font="lucida 35 bold",bg="skyblue")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="8",padx=28,pady=12,font="lucida 35 bold",bg="skyblue")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="7",padx=28,pady=12,font="lucida 35 bold",bg="skyblue")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f1=Frame(anu_root,bg="grey")
f1.pack()
b=Button(f1,text="6",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="5",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="4",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f1=Frame(anu_root,bg="grey")
f1.pack()
b=Button(f1,text="3",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="2",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="1",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=3,pady=3)

f1=Frame(anu_root,bg="grey")
f1.pack()
b=Button(f1,text="0",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="*",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="+",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
f1=Frame(anu_root,bg="grey")
f1.pack()
b=Button(f1,text="-",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="C",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="=",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
f1=Frame(anu_root,bg="grey")
f1.pack()
f1=Frame(anu_root,bg="grey")
f1.pack()
b=Button(f1,text="/",padx=30,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b=Button(f1,text="%",padx=28,pady=12,font="lucida 35 bold",bg="skyblue",activebackground="yellow")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)






anu_root.mainloop()