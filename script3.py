import tkinter as tk

root = tk.Tk()

# specify size of window.
root.geometry("250x170")
root.attributes('-fullscreen', True)
def quit_win():
   root.destroy()

# Create text widget and specify size.
T = Text(root, height = 5, width = 52)


# Create label
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))



tk.mainloop()