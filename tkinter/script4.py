import tkinter as tk
import cv2
from pyzbar import pyzbar
import keyboard
import os

#def handle_key_press(event):
#    print("Space was pressed!")

notepadpath = "notepad"

def hotkeya_callback():
    print("a was pressed!")
def hotkeyb_callback():
#    print("b was pressed!")
    os.system(f"open {notepadpath}")
def hotkeyc_callback():
#    print("c was pressed!")
   os.startfile('notepad')





keyboard.add_hotkey('a', hotkeya_callback)
keyboard.add_hotkey('b', hotkeyb_callback)
keyboard.add_hotkey('c', hotkeyc_callback)



# Create the main window
root = tk.Tk()
width_var = root.winfo_screenwidth()
height_var = root.winfo_screenheight()

root.geometry(f"{width_var}x{height_var}")  # Set window size
#root.title("Welcome to My App")  # Set window title
#Full Screen Window
root.attributes('-fullscreen', True)
def quit_win():
   root.destroy()


# Create a StringVar to associate with the label
text_var = tk.StringVar()
text_var.set("INSERT GAME CARD")

# Create the label widget with all options
label = tk.Label(root, 
                 textvariable=text_var, 
                 anchor=tk.CENTER,       
                 bg="Black",                    
                 bd=3,           
                 #height=3,
                 height=height_var,              
                 #width=30,
                 width=width_var,        
                 font=("Courier New", 80, "bold"), 
                 cursor="hand2",   
                 fg="white",             
                 padx=0,               
                 pady=0,                
                 justify=tk.CENTER,    
                 highlightthickness=0     
                )

# Pack the label into the window
label.pack()  # Add some padding to the top

#root.bind("<Key>", handle_key_press)


# Run the main event loop
root.mainloop()

