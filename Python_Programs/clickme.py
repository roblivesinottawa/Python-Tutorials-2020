import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


def sayHi():
    print('Hello World')


button = tk.Button(frame,
                    text="Click me",
                    fg='red',
                    command=print('Hello World'))


button.pack(side=tk.LEFT)
root.mainloop()