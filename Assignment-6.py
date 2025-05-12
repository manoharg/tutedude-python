import tkinter as tk

def click(event):
    """Handles button clicks and updates the display."""
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        try:
            value = eval(screen.get())
        except Exception as e:
            value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")

scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(root, textvar=scvalue, font="lucida 20 bold", bd=5, relief=tk.SUNKEN)
screen.pack(fill=tk.X, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 0
col_val = 0

for button_text in button_texts:
    button = tk.Button(button_frame, text=button_text, padx=20, pady=20, font="lucida 15 bold")
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
