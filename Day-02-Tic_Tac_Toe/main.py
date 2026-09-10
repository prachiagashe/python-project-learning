import tkinter as tk
from tkinter import messagebox


def check_winner():
    global winner

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        if (buttons[combo[0]]["text"] ==
            buttons[combo[1]]["text"] ==
            buttons[combo[2]]["text"] != ""):

            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")

            messagebox.showinfo(
                "Game Over",
                f"Player {buttons[combo[0]]['text']} wins!"
            )

            winner = True
            return


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player

        check_winner()

        if not winner:
            toggle_player()


def toggle_player():
    global current_player

    current_player = "X" if current_player == "O" else "O"

    label.config(
        text=f"Player {current_player}'s turn"
    )


# Create window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons
buttons = [
    tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )
    for i in range(9)
]

# Arrange buttons
for i, button in enumerate(buttons):
    button.grid(
        row=i // 3,
        column=i % 3
    )

# Starting player
current_player = "X"
winner = False

# Player turn label
label = tk.Label(
    root,
    text=f"Player {current_player}'s turn",
    font=("Arial", 14)
)

label.grid(
    row=3,
    column=0,
    columnspan=3
)

# Start game
root.mainloop()