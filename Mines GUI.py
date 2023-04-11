from tkinter import *
from tkinter import messagebox
from random import sample


#to restart the game
def restart():
    global root
    root.destroy()
    main()


#close window function
def close(b):
    global difficulty,minenumber,level,mines,grids
    difficulty=b["text"]
    if difficulty=="MEDIUM":
        minenumber=5
    elif difficulty=="HARD":
        minenumber=8
    level.destroy()


#show mines when game is over
def show_all_mines():
    global grids,level,mines
    #mine_img=PhotoImage(file=r"C:\Users\sanke\Downloads\mine_icon_138375 (1).png")
    for i in mines:
        grids[i].config(text="💣")


#disable all buttons
def disable_all_buttons():
    global grids,level,mines
    for i in range(25):
        grids[i].config(state=DISABLED)


#task to perform when button is clicked
def b_click(i):
    global mines,minenumber,level,grids,count,win_number

    if i in mines:
        show_all_mines()
        disable_all_buttons()
        messagebox.showinfo("Game Ended", "You lost!")
    elif count==win_number-1:
        grids[i].config(state=DISABLED, bg="Silver")
        disable_all_buttons()
        messagebox.showinfo("Game Ended", "You Win!")
    else:
        count+=1
        #count mines around clicked button
        m=0
        if i==0:
            if 1 in mines:
                m+=1
            if 6 in mines:
                m+=1
            if 5 in mines:
                m+=1
        elif i==4:
            if 3 in mines:
                m+=1
            if 8 in mines:
                m+=1
            if 9 in mines:
                m+=1
        elif i==24:
            if 19 in mines:
                m+=1
            if 18 in mines:
                m+=1
            if 23 in mines:
                m+=1
        elif i==20:
            if 15 in mines:
                m+=1
            if 16 in mines:
                m+=1
            if 21 in mines:
                m+=1
        elif i in [5,10,15]:
            if i-5 in mines:
                m+=1
            if i-4 in mines:
                m+=1
            if i+1 in mines:
                m+=1
            if i+5 in mines:
                m+=1
            if i+6 in mines:
                m+=1
        elif i in [9,14,19]:
            if i-5 in mines:
                m+=1
            if i-6 in mines:
                m+=1
            if i-1 in mines:
                m+=1
            if i+5 in mines:
                m+=1
            if i+4 in mines:
                m+=1
        elif i in [1,2,3]:
            if i-1 in mines:
                m+=1
            if i+4 in mines:
                m+=1
            if i+5 in mines:
                m+=1
            if i+6 in mines:
                m+=1
            if i+1 in mines:
                m+=1
        elif i in [21,22,23]:
            if i-1 in mines:
                m+=1
            if i-6 in mines:
                m+=1
            if i-5 in mines:
                m+=1
            if i-4 in mines:
                m+=1
            if i+1 in mines:
                m+=1
        else:
            if i-6 in mines:
                m+=1
            if i-5 in mines:
                m+=1
            if i-4 in mines:
                m+=1
            if i-1 in mines:
                m+=1
            if i+1 in mines:
                m+=1
            if i+4 in mines:
                m+=1
            if i+5 in mines:
                m+=1
            if i+6 in mines:
                m+=1


        grids[i].config(state=DISABLED, text=m if m!=0 else "", bg="Silver")


def main():
    global minenumber,count,win_number
    #setting default difficulty
    minenumber=3


    #creating difficulty level window
    global level,mines,grids,root
    level=Tk()
    level.title("Choose Difficulty Level")
    level.iconbitmap(r"C:\Users\sanke\Downloads\mine_icon_138375.ico")
    Easy=Button(level, text="EASY",bg="SystemButtonFace", fg="Green", command=lambda: close(Easy))
    Medium=Button(level, text="MEDIUM",bg="SystemButtonFace", fg="Yellow", command=lambda: close(Medium))
    Hard=Button(level, text="HARD",bg="SystemButtonFace", fg="Red", command=lambda: close(Hard))
    Easy.place(x=50, y=50)
    Medium.place(x=100, y=50)
    Hard.place(x=170, y=50)
    level.geometry("250x140")
    level.mainloop()

    #creating game window
    root=Tk()
    root.title("MineSweeper")
    root.iconbitmap(r"C:\Users\sanke\Downloads\mine_icon_138375.ico")
    root.geometry("401x530")

    #create mines list
    mines=sample(range(25),minenumber)

    #constraints to check for win
    win_number=25-minenumber
    count=0

    #creating buttons
    grids=[]
    for i in range(25):
        grids.append(Button(root, text="", height=5, width=10, bg="SystemButtonFace", command=lambda i=i: b_click(i)))
        grids[i].grid(row=i//5, column=i%5)  #creating the grid of buttons

    brestart=Button(root, text="Restart Game", font=("Times New Roman",15), height=2, width=25, bg="SystemButtonFace", command=lambda: restart())

    brestart.place(x=55, y=450)


    root.mainloop()

#to start/restart the game
main()