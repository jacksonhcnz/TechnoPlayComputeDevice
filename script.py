#Import the required Libraries
from tkinter import *
#Create an instance of Tkinter frame
win= Tk()
canvas_width = 400
canvas_height = 200

#Set the Geometry
win.geometry("1920x1200")
#Full Screen Window
win.attributes('-fullscreen', True)
def quit_win():
   win.destroy()
#Create a Quit Button
#button=Button(win,text="Quit", font=('Comic Sans', 13, 'bold'), command= quit_win)
#button.pack(pady=0) 


#Create a canvas object
canvas= Canvas(win, width=1920, height=1200, highlightthickness=0, bg="black")

x = canvas_width / 2  # X-coordinate for the center
y = canvas_height / 2  # Y-coordinate for the center

#Add a text in Canvas
canvas.create_text(960, 600, text="Insert Game Card", anchor="center", fill="White", font=('"Courier New" 80 bold'))
canvas.pack(pady=0)



win.mainloop()
