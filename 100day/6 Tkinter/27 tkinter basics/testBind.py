import tkinter as tk

def on_click(event):
    print("Button clicked at position", event.x, event.y)

root = tk.Tk()
button = tk.Button(root, text="Click Me")
button.pack()

button.bind("<Button-1>", on_click)

root.mainloop()
