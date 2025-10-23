# import turtle as t
# import random
# colors = ["red", "yellow", "cyan", "green", "blue", "purple"]

# t.speed(0)
# t.bgcolor('black')
# # t.pencolor('orange')

# def square(x, y):
#     for j in range(4):
#         t.forward(x)
#         t.right(y)

# for i in range(80):
#     t.pencolor(random.choice(colors))
#     square(170, 90)
#     t.right(5) 
#     t.circle(50)
#     t.right(50)
 
# t.hideturtle()
# t.done()


import tkinter as tk
from tkinter import messagebox 

root = tk.Tk()
root.title("Tic-Tac-Toe")

winner = False
current_player = "X"


def player_win():  
    global winner 
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        if (button[combo[0]]["text"] == button[combo[1]]["text"] == button[combo[2]]) and button[combo[0]]["text"] != "":
            button[combo[0]].config(bg= "green")
            button[combo[1]].config(bg= "green")
            button[combo[2]].config(bg= "green")
            messagebox.showinfo("Tic-Tac-Toe", f"Players {button[combo[0]]['text']} Wins!")
            winner = True
            return
       
def button_chick(index):
    if button[index]["text"] == "" and not winner:
        button[index]["text"] = current_player
        player_win()
        if not winner:
            toggle_player()


def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"player {current_player}'s turn")


button = [tk.Button(root, text= "", font=("normal", 25), width= 6, height= 2, command= lambda i=i: button_chick(i)) for i in range(9)]

for i, btn in enumerate(button):
    btn.grid(row=i //3, column=i % 3)

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()