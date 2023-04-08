from tkinter import *
from tkinter import messagebox
#from tkinter import Button

#create the main window
root=Tk()
root.title("Tic-Tac-Toe")
root.iconbitmap(r'C:\Users\sanke\Downloads\tic-tac-toe_39453.ico')
root.geometry("481x625")

count=0 #to count the number of turns

#to restart the game
def restart():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, count
    for i in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        i.config(state=NORMAL, bg="SystemButtonFace", text="")
        count=0

#to disable the buttons
def disable_all_buttons():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#to command the button
def b_click(b):
    global count
    if b["text"] == "" and count%2 ==0:
        b["text"] = "X"
        count+=1
        check_win()
    elif b["text"] == "" and count%2 == 1:
        b["text"] = "O"
        count+=1
        check_win()
    else:
        messagebox.showerror("UH-OH!", "Button has already been clicked on!\n\nPlease choose another button")

#To check the win or draw
def check_win():
    global count,b1,b2,b3,b4,b5,b6,b7,b8,b9
    checklist=[[b1,b2,b3],[b4,b5,b6],[b7,b8,b9],[b1,b4,b7],[b2,b5,b8],[b3,b6,b9],[b1,b5,b9],[b3,b5,b7]]   #All the ways to win
    draw=True
    for check in checklist:
        if check[0]["text"]+check[1]["text"]+check[2]["text"]=="XXX":
            check[0].config(bg="red")
            check[1].config(bg="red")
            check[2].config(bg="red")
            disable_all_buttons()
            messagebox.showinfo("We have a winner!","Player X has won!")
            draw=False
        elif check[0]["text"]+check[1]["text"]+check[2]["text"]=="OOO":
            check[0].config(bg="red")
            check[1].config(bg="red")
            check[2].config(bg="red")
            disable_all_buttons()
            messagebox.showinfo("We have a winner!","Player O has won!")
            draw=False
    if count==9 and draw:
        disable_all_buttons()
        messagebox.showinfo("Game ends without a winner","It is a draw!")

#create buttons

b1=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b1))
b2=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b2))
b3=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b3))

b4=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b4))
b5=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b5))
b6=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b6))

b7=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b7))
b8=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b8))
b9=Button(root, text="", font=("Times New Roman",20), height=5, width=10, bg="SystemButtonFace", command=lambda: b_click(b9))

#create restart button
brestart=Button(root, text="Restart Game", font=("Times New Roman",15), height=2, width=25, bg="SystemButtonFace", command=lambda: restart())

#create buttons grid

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

#place restart button
brestart.place(x=100, y=550)
root.mainloop()