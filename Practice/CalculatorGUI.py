#Pyhhon GUI calculator using tkinter
#By MJK618
from tkinter import *

def click(event):
    global str_var
    text = event.widget.cget("text")
    if text == "=":
        if str_var.get().isdigit():
            value = int(str_var.get())
        else:
            value = eval(str_var.get())

        str_var.set(value)
        field.update()
    elif text == "C":
        str_var.set("")
        field.update()
    else:
        str_var.set(str_var.get() + text)
        field.update()
        
#Creating the main screen
root = Tk()
root.geometry("600x600")
root.title("Calculator by MJK618")

#Making the entry widget whose textvalue would be a string variable
str_var = StringVar()
str_var.set("")

#The screen where caculations wil be shown
field = Entry(root, textvar = str_var, font="Courier 40 bold")
field.pack(fill = X, ipadx=10, padx=10,pady=10)

#Creating Frames
frame5 = Frame(root,bg='cyan')
frame5.pack()
#Bind the buttons with a function
b_div = Button(frame5, text="/",padx='10', pady='10',font="Courier 35 bold")
b_div.pack(side=LEFT,padx=10,pady=10)
b_div.bind("<Button-1>",click)

b_mul = Button(frame5, text="*",padx='10', pady='10',font="Courier 35 bold")
b_mul.pack(side=LEFT,padx=10,pady=10)
b_mul.bind("<Button-1>",click)

b_sub = Button(frame5, text="-",padx='10', pady='10',font="Courier 35 bold")
b_sub.pack(side=LEFT,padx=10,pady=10)
b_sub.bind("<Button-1>",click)

b_plus = Button(frame5, text="+",padx='10', pady='10',font="Courier 35 bold")
b_plus.pack(side=LEFT,padx=10,pady=10)
b_plus.bind("<Button-1>",click)

#Creating Frames
frame1 = Frame(root,bg='cyan')
frame1.pack()
#Bind the buttons with a function
b9 = Button(frame1, text="9",padx='10', pady='10',font="Courier 35 bold")
b9.pack(side=LEFT,padx=10,pady=10)
b9.bind("<Button-1>",click)

b8 = Button(frame1, text="8",padx='10', pady='10',font="Courier 35 bold")
b8.pack(side=LEFT,padx=10,pady=10)
b8.bind("<Button-1>",click)

b7 = Button(frame1, text="7",padx='10', pady='10',font="Courier 35 bold")
b7.pack(side=LEFT,padx=10,pady=10)
b7.bind("<Button-1>",click)

#Creating Frames
frame2 = Frame(root,bg='cyan')
frame2.pack()
#Bind the buttons with a function
b6 = Button(frame2, text="6",padx='10', pady='10',font="Courier 35 bold")
b6.pack(side=LEFT,padx=10,pady=10)
b6.bind("<Button-1>",click)

b5 = Button(frame2, text="5",padx='10', pady='10',font="Courier 35 bold")
b5.pack(side=LEFT,padx=10,pady=10)
b5.bind("<Button-1>",click)

b4 = Button(frame2, text="4",padx='10', pady='10',font="Courier 35 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)

#Creating Frames
frame3 = Frame(root,bg='cyan')
frame3.pack()
#Bind the buttons with a function
b3 = Button(frame3, text="3",padx='10', pady='10',font="Courier 35 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

b2 = Button(frame3, text="2",padx='10', pady='10',font="Courier 35 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)

b1 = Button(frame3, text="1",padx='10', pady='10',font="Courier 35 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)

#Creating Frames
frame4 = Frame(root,bg='cyan')
frame4.pack()
#Bind the buttons with a function
b_C = Button(frame4, text="C",padx='10', pady='10',font="Courier 35 bold")
b_C.pack(side=LEFT,padx=10,pady=10)
b_C.bind("<Button-1>",click)

b0 = Button(frame4, text="0",padx='10', pady='10',font="Courier 35 bold")
b0.pack(side=LEFT,padx=10,pady=10)
b0.bind("<Button-1>",click)

b_equal = Button(frame4, text="=",padx='10', pady='10',font="Courier 35 bold")
b_equal.pack(side=LEFT,padx=10,pady=10)
b_equal.bind("<Button-1>",click)


root.mainloop()

