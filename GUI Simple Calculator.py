from tkinter import *
root = Tk()
root.title("Simple Calculator")

e=Entry(root, width = 35 , borderwidth = 7)
e.grid(row = 0,columnspan=3,padx=20,pady=20)

def button_click(number):
    now = e.get()
    e.delete(0,END)
    e.insert(0,str(now) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    fan = e.get()
    global first
    global math
    math = "addition"
    first = int(fan)
    e.delete(0,END)

def button_sub():
    fan = e.get()
    global first
    global math
    math = "subtraction"
    first = int(fan)
    e.delete(0, END)

def button_mul():
    fan = e.get()
    global first
    global math
    math = "multiplication"
    first = int(fan)
    e.delete(0, END)

def button_div():
    fan = e.get()
    global first
    global math
    math = "division"
    first = int(fan)
    e.delete(0, END)

def button_equal():
    second = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,int(first) + int(second))
    elif math == "subtraction":
        e.insert(0,int(first) - int(second))
    elif math == "multiplication":
        e.insert(0, int(first) * int(second))
    elif math == "division":
        e.insert(0, int(first) / int(second))

button_1 = Button(root,text="1",padx=30,pady=30,command=lambda:button_click(1),bg="yellow")
button_2 = Button(root,text="2",padx=30,pady=30,command=lambda:button_click(2),bg="yellow")
button_3 = Button(root,text="3",padx=30,pady=30,command=lambda:button_click(3),bg="yellow")
button_4 = Button(root,text="4",padx=30,pady=30,command=lambda:button_click(4),bg="yellow")
button_5 = Button(root,text="5",padx=30,pady=30,command=lambda:button_click(5),bg="yellow")
button_6 = Button(root,text="6",padx=30,pady=30,command=lambda:button_click(6),bg="yellow")
button_7 = Button(root,text="7",padx=30,pady=30,command=lambda:button_click(7),bg="yellow")
button_8 = Button(root,text="8",padx=30,pady=30,command=lambda:button_click(8),bg="yellow")
button_9 = Button(root,text="9",padx=30,pady=30,command=lambda:button_click(9),bg="yellow")
button_0 = Button(root,text="0",padx=30,pady=30,command=lambda:button_click(0),bg="yellow")
button_cls = Button(root,text="clear",padx=30,pady=30,command=button_click,bg="yellow")
button_equal = Button(root,text="=",padx=30,pady=30,command=button_equal,bg="yellow")
button_add = Button(root,text="+",padx=30,pady=30,command=button_add,bg="yellow")
button_sub = Button(root,text="-",padx=30,pady=30,command=button_sub,bg="yellow")
button_mul = Button(root,text="x",padx=30,pady=30,command=button_mul,bg="yellow")
button_div = Button(root,text="/",padx=30,pady=30,command=button_div,bg="yellow")

button_1.grid(row=3,column=0,padx=10)
button_2.grid(row=3,column=1,padx=10)
button_3.grid(row=3,column=2,padx=10)

button_4.grid(row=2,column=0,padx=10)
button_5.grid(row=2,column=1,padx=10)
button_6.grid(row=2,column=2,padx=10)

button_7.grid(row=1,column=0,padx=10)
button_8.grid(row=1,column=1,padx=10)
button_9.grid(row=1,column=2,padx=10)
button_0.grid(row=4,column=0,padx=10)

button_cls.grid(row=6,)
button_equal.grid(row=4,column=1,padx=10)

button_add.grid(row=5,column=0)
button_sub.grid(row=5,column=1)
button_mul.grid(row=5,column=2)
button_div.grid(row=4,column=2,padx=10)

root.mainloop()
