from tkinter import *
from tkinter import ttk, messagebox
import webbrowser
import os
import sys

# Global variables
active_player = 1
player_moves = {1: [], 2: []}
winning_combinations = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9},  # Rows
    {1, 4, 7}, {2, 5, 8}, {3, 6, 9},  # Columns
    {1, 5, 9}, {3, 5, 7}              # Diagonals
]

# Initialize root window
root = Tk()
root.title("Tic Tac Toe")
root.configure(background="#0f5ddb")

style = ttk.Style()
style.theme_use('classic')
style.configure('TButton', background="#0f5ddb", font=("Arial", 14))

# Button storage
buttons = {}

# Functions
def reset_game():
    """Reset the game to its initial state."""
    global active_player, player_moves
    active_player = 1
    player_moves = {1: [], 2: []}
    for button in buttons.values():
        button.config(text=" ", state=NORMAL)
    root.title("Tic Tac Toe: Player 1's Turn")

def exit_game():
    """Exit the game."""
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def open_about():
    """Open the about link."""
    url = "https://www.facebook.com/boubli.programmer"
    webbrowser.open_new_tab(url)

def button_click(button_id):
    """Handle button clicks."""
    global active_player
    current_player_moves = player_moves[active_player]
    current_player_moves.append(button_id)
    set_button_layout(button_id, "X" if active_player == 1 else "O")
    if check_winner():
        messagebox.showinfo("Congratulations", f"Player {active_player} wins!")
        reset_game()
    elif len(player_moves[1]) + len(player_moves[2]) == 9:
        messagebox.showinfo("Draw", "It's a tie!")
        reset_game()
    else:
        active_player = 2 if active_player == 1 else 1
        root.title(f"Tic Tac Toe: Player {active_player}'s Turn")

def set_button_layout(button_id, text):
    """Update button layout for a move."""
    button = buttons[button_id]
    button.config(text=text, state=DISABLED)

def check_winner():
    """Check if the current player has won."""
    current_moves = set(player_moves[active_player])
    return any(combo.issubset(current_moves) for combo in winning_combinations)

# Create buttons
for row in range(3):
    for col in range(3):
        button_id = row * 3 + col + 1
        button = ttk.Button(root, text=" ", command=lambda id=button_id: button_click(id))
        button.grid(row=row, column=col, ipadx=40, ipady=40, sticky="nsew")
        buttons[button_id] = button

# Control buttons
ttk.Button(root, text="Restart", command=reset_game).grid(row=3, column=0, pady=10, sticky="nsew")
ttk.Button(root, text="Exit", command=exit_game).grid(row=3, column=1, pady=10, sticky="nsew")
ttk.Button(root, text="About Me", command=open_about).grid(row=3, column=2, pady=10, sticky="nsew")

# Adjust column and row weights for responsiveness
for i in range(3):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

root.mainloop()
