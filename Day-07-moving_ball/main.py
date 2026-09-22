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


