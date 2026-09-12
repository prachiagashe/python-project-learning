import tkinter as tk


# -----------------------------
# Functions
# -----------------------------

def button_click(value):
    current_value = display.get()

    display.delete(0, tk.END)
    display.insert(0, current_value + str(value))


def clear_display():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def delete_last():
    current_value = display.get()

    display.delete(0, tk.END)
    display.insert(0, current_value[:-1])


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("Python Calculator")
root.geometry("350x500")
root.resizable(False, False)


# -----------------------------
# Display
# -----------------------------

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)

display.pack(
    padx=10,
    pady=20,
    fill="x"
)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(root)

button_frame.pack()


buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("+", 3, 2),
    ("=", 3, 3),
]


for text, row, column in buttons:

    if text == "=":
        command = calculate
    else:
        command = lambda value=text: button_click(value)

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# -----------------------------
# Clear Button
# -----------------------------

clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 15, "bold"),
    width=15,
    height=2,
    command=clear_display
)

clear_button.pack(pady=10)


# -----------------------------
# Delete Button
# -----------------------------

delete_button = tk.Button(
    root,
    text="DELETE",
    font=("Arial", 15, "bold"),
    width=15,
    height=2,
    command=delete_last
)

delete_button.pack()


# -----------------------------
# Start Application
# -----------------------------

root.mainloop()