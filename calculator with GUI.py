import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

def evaluate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def press_key(char):
    if char == "=":
        evaluate()
    elif char == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + char)

def on_key(event):
    key = event.keysym
    char = event.char
    if key == "Return":
        evaluate()
    elif key == "BackSpace":
        entry_var.set(entry_var.get()[:-1])
    elif key == "Escape":
        entry_var.set("")
    elif char in "0123456789+-*/().":
        entry_var.set(entry_var.get())
    return "break"

# Setup app
app = ttk.Window(themename="darkly")
app.title("Calculator")
app.geometry("360x540")
app.resizable(False, False)

entry_var = StringVar()
entry = ttk.Entry(app, textvariable=entry_var, font=("Segoe UI", 26), justify="right")
entry.pack(pady=20, padx=15, fill=X)
entry.focus()
app.bind("<Key>", on_key)

# Custom styles
style = ttk.Style()
style.configure("Dark.TButton", font=("Sans-serif", 18), padding=10, borderwidth=0, relief="flat")
style.configure("Orange.TButton", font=("Sans-serif", 18), padding=10, borderwidth=0, relief="flat", background="#ff9500", foreground="white")

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['(', ')', '=', '']
]

for row_vals in buttons:
    row = ttk.Frame(app)
    row.pack(expand=True, fill="both", padx=10, pady=5)
    for val in row_vals:
        if val:
            is_op = val in ['+', '-', '*', '/', '=']
            style_name = "Orange.TButton" if is_op else "Dark.TButton"
            btn = ttk.Button(
                row,
                text=val,
                style=style_name,
                command=lambda v=val: press_key(v)
            )
            btn.pack(side="left", expand=True, fill="both", padx=6, pady=6)

app.mainloop()
