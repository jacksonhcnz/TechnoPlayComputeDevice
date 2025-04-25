import tkinter as tk

root = tk.Tk()
canvas_width = 1920
canvas_height = 1200

#Full Screen Window
root.attributes('-fullscreen', True)
def quit_win():
   root.destroy()

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black", highlightthickness=0)
canvas.pack()

text = "Centered Text"
x = canvas_width / 2  # X-coordinate for the center
y = canvas_height / 2  # Y-coordinate for the center

canvas.create_text(x, y, text="INSERT GAME CARD", anchor="center", fill="White", font=('"Courier New" 80 bold'))

root.mainloop()