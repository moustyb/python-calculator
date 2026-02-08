import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
                font=("Segoe UI", 16),
                padding=10,
                relief="flat",
                background="#2d2d2d",
                foreground="white")

style.map("TButton",
          background=[("active", "#3a3a3a")])

style.configure("Operator.TButton",
                background="#ff9500",
                foreground="white")

style.map("Operator.TButton",
          background=[("active", "#e08900")])

entry = tk.Entry(root, font=("Segoe UI", 28), justify="right",
                 bg="#3a3a3a", fg="white", bd=0, relief="flat")
entry.pack(fill="x", padx=20, pady=20, ipady=15)

def click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

buttons = [
    ["AC", "%", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "" , ""]
]

for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(fill="x", padx=20, pady=5)
    for btn in row:
        if btn == "":
            tk.Label(frame, bg="#1e1e1e").pack(side="left", expand=True)
            continue

        style_name = "TButton"
        if btn in ["+", "-", "×", "÷", "="]:
            style_name = "Operator.TButton"

        b = ttk.Button(frame, text=btn, style=style_name,
                       command=lambda v=btn: click(v))
        b.pack(side="left", expand=True, fill="x", padx=5)

root.mainloop()
