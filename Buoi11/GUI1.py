import tkinter
from tkinter import messagebox

# Khai báo form chính
root = tkinter.Tk()

#Thêm control (widget) vô form
tkinter.Label(root,
    text="HELLO NIIE PYTHON",
    font="Arial 18",
    bg="yellow green",    # bg: Màu nền
    fg = "red",           # fg: màu chữ
).pack()
tkinter.Label(root, text="PHẦN MỀM QUẢN LÝ").pack()
tkinter.Button(root,
    text="Click me",
    command=lambda: messagebox.showinfo("Thông báo", "Vừa click")
).pack()

# Hiện form lên
root.mainloop()