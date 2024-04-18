import tkinter as tk
from tkinter import messagebox
import random

global stop_game
global pause_game
current_player = 1

# enforce player turns
def switch_player():
    global current_player
    current_player = (current_player + 1) % 2

# visualize the state of the game for the player 
# stop the game when over
def button_click(row, col, player=1):
    # player turn logic
    global pause_game
    player_val =  ""
    button = buttons[row][col]

    if player == 1: # human player
        button.config(text="X", bg='green', state='disabled')
        player_val = "X"
        switch_player()
        pause_game = False

    else: # bot player
        button.config(text="O", bg='red', state='disabled')
        player_val = "O"
        pause_game = True
    find_win(player_val)
    make_move()

# create board game with buttons
def create_buttons():
    buttons = []
    for r in range(3):
        button_row = []
        for c in range(3):
            button = tk.Button(root, text="  ", width=20, height=10, command=lambda r=r, c=c : button_click(r, c), borderwidth=2, relief="solid", activebackground='yellow')
            button.grid(row=r, column=c)
            button_row.append(button)
        buttons.append(button_row)
    return buttons


# dummy bot, player #2
def make_move(bot=0):
    global current_player
    global pause_game

    if current_player == bot and pause_game == False:
        for r in range(3):
            for c in range(3):
                currButton = buttons[r][c]
                state = str(currButton['state'])
                if state != 'disabled':
                    button_click(r,c,player=0)
                    switch_player()
                    return
                    
# find the winner/tie
def find_win(player):
    for i in range(3):

        # horizonal wins
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] == player:
            messagebox.showinfo("Game Over", f"The game has ended! Congrats player {player}!")
            stop()
        
        # vertical wins
        elif buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] == player:
            messagebox.showinfo("Game Over", f"The game has ended! Congrats player {player}!")
            stop()

    # diagonal wins
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == player:
        messagebox.showinfo("Game Over", f"The game has ended! Congrats player {player}!")
        stop()

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == player:
        messagebox.showinfo("Game Over", f"The game has ended! Congrats player {player}!")
        stop()

    # check for tie
    elif all(button['state'] == 'disabled' for row in buttons for button in row):
        messagebox.showinfo("Game Over", "The game has ended! It's a tie!")
        stop()
    
# stop game
def stop():
    global stop_game
    stop_game = True
         
# start game
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.geometry("800x600")

    buttons = create_buttons()

    root.mainloop()
