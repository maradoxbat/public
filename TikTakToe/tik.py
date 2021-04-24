from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("tik")

clicked = True
count = 0
win = False

def resetall():
    global win,clicked, count
    clicked = True
    count = 0
    win = False

    b1["text"]=" "
    b2["text"]=" "
    b3["text"]=" "

    b4["text"]=" "
    b5["text"]=" "
    b6["text"]=" "

    b7["text"]=" "
    b8["text"]=" "
    b9["text"]=" "

def checkwin():
    global win

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        messagebox.showinfo("X won", "X won")
        win=True
    if b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        messagebox.showinfo("X won", "X won")
        win=True
    if b1["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        messagebox.showinfo("X won", "X won")
        win=True

    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        messagebox.showinfo("O won", "O won")
        win=True
    if b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        messagebox.showinfo("O won", "O won")
        win=True
    if b1["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        messagebox.showinfo("O won", "O won")
        win=True
    if win == True:
        resetall()

def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1

    else:
        messagebox.showinfo("Error", "Invalid move")
    checkwin()


b1= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b1) )
b2= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b2) )
b3= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b3) )

b4= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b4) )
b5= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b5) )
b6= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b6) )

b7= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b7) )
b8= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b8) )
b9= Button(root, text=" ", height=3, width=6, command=lambda: b_click(b9) )

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
