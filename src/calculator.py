import tkinter as tk

root = tk.Tk()
root.title("Python Calculator")
root.geometry("320x450")
root.configure(bg="#121212")

display = tk.Entry(root,
                   font=("Segoe UI", 28),
                   justify="right",
                   bg="#1f1f1f",
                   fg="white",
                   bd=0,
                   relief="flat")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15, sticky="nsew")

for i in range(1, 6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

def on_click(text):
    if text == "AC":
        display.delete(0, tk.END)
    elif text == "=":
        try:
            result = eval(display.get().replace("×", "*").replace("÷", "/"))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, text)

btn_cfg_num = {
    "font": ("Segoe UI", 16),
    "bg": "#2b2b2b",
    "fg": "white",
    "activebackground": "#3a3a3a",
    "activeforeground": "white",
    "bd": 0,
    "relief": "flat"
}

btn_cfg_op = {
    "font": ("Segoe UI", 16),
    "bg": "#ff9500",
    "fg": "white",
    "activebackground": "#e08900",
    "activeforeground": "white",
    "bd": 0,
    "relief": "flat"
}

btn_cfg_func = {
    "font": ("Segoe UI", 16),
    "bg": "#3a3a3a",
    "fg": "white",
    "activebackground": "#4a4a4a",
    "activeforeground": "white",
    "bd": 0,
    "relief": "flat"
}

layout = [
    ["AC", "%", "-", ""],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "=", ".", ""]
]

for r, row in enumerate(layout, start=1):
    for c, text in enumerate(row):
        if text == "":
            continue

        if text in ["+", "-", "×", "÷", "="]:
            cfg = btn_cfg_op
        elif text in ["AC", "%"]:
            cfg = btn_cfg_func
        else:
            cfg = btn_cfg_num

        btn = tk.Button(root,
                        text=text,
                        command=lambda t=text: on_click(t),
                        **cfg)
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

root.mainloop()
