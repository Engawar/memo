import tkinter as tk
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text_content = text_widget.get("1.0", tk.END)
        file.write(text_content)
        file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', defaultextension=".txt")
    if file:
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", file.read())
        file.close()

root = tk.Tk()
root.title("simple memo")

text_widget = tk.Text(root)
text_widget.pack()

# saveボタンの実装
save_button = tk.Button(root, text="名前を付けて保存", command=save_file)
save_button.pack(side=tk.LEFT)

# openボタンの実装
open_button = tk.Button(root, text="開く", command=open_file)
open_button.pack(side=tk.LEFT)

root.mainloop()