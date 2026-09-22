import tkinter as tk

root = tk.Tk()
root.title("Moving Ball")
root.geometry("500x300")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

ball = canvas.create_oval(
    20, 130,
    70, 180,
    fill="green"
)

x = 5


def move_ball():
    global x

    canvas.move(ball, x, 0)

    position = canvas.coords(ball)

    if position[2] >= 500 or position[0] <= 0:
        x = -x

    root.after(30, move_ball)


move_ball()

root.mainloop()