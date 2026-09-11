import tkinter as tk
from tkinter import messagebox
import os


# -----------------------------
# Functions
# -----------------------------

def add_task():
    """Add a new task to the list."""

    task = task_entry.get().strip()

    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a task."
        )


def delete_task():
    """Delete the selected task."""

    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        save_tasks()

    except IndexError:
        messagebox.showwarning(
            "Warning",
            "Please select a task to delete."
        )


def mark_completed():
    """Mark the selected task as completed."""

    try:
        selected_task = task_listbox.curselection()[0]

        task = task_listbox.get(selected_task)

        if not task.startswith("✓ "):
            task_listbox.delete(selected_task)
            task_listbox.insert(
                selected_task,
                "✓ " + task
            )

        save_tasks()

    except IndexError:
        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )


def clear_tasks():
    """Delete all tasks after confirmation."""

    if task_listbox.size() == 0:
        messagebox.showinfo(
            "Information",
            "There are no tasks to clear."
        )
        return

    answer = messagebox.askyesno(
        "Clear Tasks",
        "Are you sure you want to delete all tasks?"
    )

    if answer:
        task_listbox.delete(0, tk.END)
        save_tasks()


def save_tasks():
    """Save all tasks to a text file."""

    with open("tasks.txt", "w", encoding="utf-8") as file:

        tasks = task_listbox.get(0, tk.END)

        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    """Load previously saved tasks."""

    if os.path.exists("tasks.txt"):

        with open("tasks.txt", "r", encoding="utf-8") as file:

            for task in file:
                task = task.strip()

                if task:
                    task_listbox.insert(
                        tk.END,
                        task
                    )


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("To-Do List")

root.geometry("500x550")

root.resizable(False, False)


# -----------------------------
# Heading
# -----------------------------

heading = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 24, "bold")
)

heading.pack(pady=20)


# -----------------------------
# Task Input
# -----------------------------

task_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=30
)

task_entry.pack(pady=10)

task_entry.focus()


# -----------------------------
# Add Task Button
# -----------------------------

add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    width=20,
    command=add_task
)

add_button.pack(pady=5)


# -----------------------------
# Task List
# -----------------------------

task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=12,
    selectmode=tk.SINGLE
)

task_listbox.pack(pady=15)


# -----------------------------
# Complete Button
# -----------------------------

complete_button = tk.Button(
    root,
    text="Mark Completed",
    font=("Arial", 12),
    width=20,
    command=mark_completed
)

complete_button.pack(pady=5)


# -----------------------------
# Delete Button
# -----------------------------

delete_button = tk.Button(
    root,
    text="Delete Task",
    font=("Arial", 12),
    width=20,
    command=delete_task
)

delete_button.pack(pady=5)


# -----------------------------
# Clear Button
# -----------------------------

clear_button = tk.Button(
    root,
    text="Clear All Tasks",
    font=("Arial", 12),
    width=20,
    command=clear_tasks
)

clear_button.pack(pady=5)


# -----------------------------
# Keyboard Shortcut
# -----------------------------

root.bind(
    "<Return>",
    lambda event: add_task()
)


# -----------------------------
# Load Saved Tasks
# -----------------------------

load_tasks()


# -----------------------------
# Start Application
# -----------------------------

root.mainloop()