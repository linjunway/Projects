import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from ctypes import windll

"""====================================================================================================="""
""" Helper Functions                                                                                    """
"""====================================================================================================="""

def display_move(row, column):
    global players
    global curr_player
    global board
    global turn_message
    global gameover
    global r1, r2, r3, c1, c2, c3, d1, d2

    if board[row][column]["text"] != "" or gameover == True:
        return
    
    board[row][column]["text"] = curr_player
    track_move_weight(row, column)

    check_winner(r1, r2, r3, c1, c2, c3, d1, d2)

    if curr_player == players[0]:
        curr_player = players[1]

    elif curr_player == players[1]:
        curr_player = players[0]

    if not gameover:
        turn_message["text"] = curr_player+"'s turn"

def track_move_weight(row, col):
    global curr_player
    global players
    global r1, r2, r3, c1, c2, c3, d1, d2

    if curr_player == players[0]:
        if row == 0 and col == 0:
            r1 += 1
            c1 += 1
            d1 += 1
        elif row == 0 and col == 1:
            r1 += 1
            c2 += 1
        elif row == 0 and col == 2:
            r1 += 1
            c3 += 1
            d2 += 1
        elif row == 1 and col == 0:
            r2 += 1
            c1 += 1
        elif row == 1 and col == 1:
            r2 += 1
            c2 += 1
            d1 += 1
            d2 += 1
        elif row == 1 and col == 2:
            r2 += 1
            c3 += 1
        elif row == 2 and col == 0:
            r3 += 1
            c1 += 1
            d2 += 1
        elif row == 2 and col == 1:
            r3 += 1
            c2 += 1
        elif row == 2 and col == 2:
            r3 += 1
            c3 += 1
            d1 += 1
    elif curr_player == players[1]:
        if row == 0 and col == 0:
            r1 -= 1
            c1 -= 1
            d1 -= 1
        elif row == 0 and col == 1:
            r1 -= 1
            c2 -= 1
        elif row == 0 and col == 2:
            r1 -= 1
            c3 -= 1
            d2 -= 1
        elif row == 1 and col == 0:
            r2 -= 1
            c1 -= 1
        elif row == 1 and col == 1:
            r2 -= 1
            c2 -= 1
            d1 -= 1
            d2 -= 1
        elif row == 1 and col == 2:
            r2 -= 1
            c3 -= 1
        elif row == 2 and col == 0:
            r3 -= 1
            c1 -= 1
            d2 -= 1
        elif row == 2 and col == 1:
            r3 -= 1
            c2 -= 1
        elif row == 2 and col == 2:
            r3 -= 1
            c3 -= 1
            d1 -= 1

    return r1, r2, r3, c1, c2, c3, d1, d2

def check_winner(r1, r2, r3, c1, c2, c3, d1, d2):
    global gameover, turn_message, turn_ctr
    
    turn_ctr+=1

    if (turn_ctr != 9 and (r1 == 3 or r2 == 3 or r3 == 3 or c1 == 3 or c2 == 3 or c3 == 3 or d1 == 3 or d2 == 3)):
        highlight_box(r1, r2, r3, c1, c2, c3, d1, d2)
        gameover = True
        turn_message["text"] = "Player X has won!"
    elif (turn_ctr != 9 and (r1 == -3 or r2 == -3 or r3 == -3 or c1 == -3 or c2 == -3 or c3 == -3 or d1 == -3 or d2 == -3)):
        highlight_box(r1, r2, r3, c1, c2, c3, d1, d2)
        gameover = True
        turn_message["text"] = "Player O has won!"
    elif turn_ctr == 9:
        gameover = True
        turn_message["text"] = "Draw!"

def highlight_box(r1, r2, r3, c1, c2, c3, d1, d2):
    global board

    if r1 == 3 or r1 == -3:
        for col in range(3):
            board[0][col]["background"]="gold"
    elif r2 == 3 or r2 == -3:
        for col in range(3):
            board[1][col]["background"]="gold"
    elif r3 == 3 or r3 == -3:
        for col in range(3):
            board[2][col]["background"]="gold"

    # Highlight the winning column
    if c1 == 3 or c1 == -3:
        for row in range(3):
            board[row][0]["background"]="gold"
    elif c2 == 3 or c2 == -3:
        for row in range(3):
            board[row][1]["background"]="gold"
    elif c3 == 3 or c3 == -3:
        for row in range(3):
            board[row][2]["background"]="gold"

    # Highlight the winning diagonal
    if d1 == 3 or d1 == -3:
        for i in range(3):
            board[i][i]["background"]="gold"
    elif d2 == 3 or d2 == -3:
        for i in range(3):
            board[i][2 - i]["background"]="gold"

def reset_board():
    global board
    global players
    global curr_player
    global turn_message
    global gameover
    global r1, r2, r3, c1, c2, c3, d1, d2
    global turn_ctr

    turn_ctr = 0
    gameover = False
    r1, r2, r3, c1, c2, c3, d1, d2 = 0, 0, 0, 0, 0, 0, 0, 0

    for i in range(3):
        for j in range(3):
            board[i][j]["text"] = ""
            board[i][j]["background"] = dark_gray

    curr_player = players[0]
    turn_message["text"] = curr_player+"'s turn"

"""====================================================================================================="""
""" Main Program                                                                                        """
"""====================================================================================================="""

board = [[0,0,0], 
         [0,0,0], 
         [0,0,0]]

gameover = False
turn_ctr = 0
r1, r2, r3, c1, c2, c3, d1, d2 = 0, 0, 0, 0, 0, 0, 0, 0

players = ["X", "O"]
curr_player = players[0]

purple = "#703BFF"
dark_gray = "#595959"
gold = "#FFDF3C"
cyan = "#3CFFF3"

"""=================================================================================================="""
""" GUI Setup                                                                                        """
"""=================================================================================================="""

windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title('Tic Tac Toe')
root.geometry('400x500')
root.resizable(0,0)

root.grid_rowconfigure(0, weight=1)

for i in range(1,4):  
    root.grid_rowconfigure(i, weight=3)
for j in range(3):  
    root.grid_columnconfigure(j, weight=3)

root.grid_rowconfigure(4, weight=1)

messages = tk.Frame(root, background=dark_gray)
messages.grid(row=0, column=0, columnspan=3, sticky="nsew")

messages.grid_rowconfigure(0, weight=1)
messages.grid_columnconfigure(0, weight=1)

turn_message = tk.Label(messages, text=curr_player+"'s turn", background=dark_gray, font=("Arial", 20, "bold"))
turn_message.grid(row=0, column=0, columnspan=3, sticky='nsew')

game_frame = tk.Frame(root, background=dark_gray)
game_frame.grid(row=1, column=0, rowspan=3, columnspan=3, sticky="nsew")

for i in range(3): 
    game_frame.grid_rowconfigure(i, weight=3) 
    game_frame.grid_columnconfigure(i, weight=3)

for i in range(3):
    for j in range(3):
        btn = tk.Button(game_frame, text="", font=("Arial", 20, "bold"), background=dark_gray, foreground=cyan, command=lambda i=i, j=j: display_move(i,j), width=4, height=1)
        btn.grid(row=i, column=j, sticky="nsew")
        board[i][j] = btn

restart_frame = tk.Frame(root, background=dark_gray)
restart_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")

restart_frame.grid_rowconfigure(0, weight=1)
restart_frame.grid_columnconfigure(0, weight=1)

reset = ctk.CTkButton(restart_frame, fg_color=purple, text="Restart", command=reset_board, anchor="center").grid(row=4, column=0, padx=100, pady=(0,20))
    
if __name__ == '__main__':
    root.mainloop()