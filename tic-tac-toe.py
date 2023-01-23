from tkinter import *
import random

# winner_exists() returns True if a winner exists in the current state of the game, "Tie" if it is a tie game, 
# and False if no winner exists and it is not a tie
def winner_exists():
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combination in winning_combinations:
        if all(buttons[x][y]['text'] != "" and buttons[x][y]['text'] == buttons[combination[0][0]][combination[0][1]]['text'] for x, y in combination):
            for x, y in combination:
                buttons[x][y].config(bg="#89b2f5")
            return True

    if empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#eaf589")
        return "Tie"
    else:
        return False

# whos_turn(row, column) sets the player to whoevers turn it is next, and changes the label to show who's turn it is.
def whos_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and winner_exists() is False:
        buttons[row][column]['text'] = player
        winner = winner_exists()
        if winner is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} turn")
        elif winner is True:
            label.config(text=f"{player} wins")
        elif winner == "Tie":
            label.config(text="Tie!")

# empty_spaces() returns True if there are empty spaces on the board, and False otherwise.
def empty_spaces():
    spaces = sum(1 for row in range(3) for column in range(3) if buttons[row][column]['text'] == "")
    return spaces != 0


# Game UI logic

window = Tk()
window.title("Tic-Tac-Toe")
players = ("X","O")
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=f"{player}'s turn", font=('arial',50))
label.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',50), width=5, height=2,
                                      command=lambda r=row, c=column: whos_turn(r,c))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()