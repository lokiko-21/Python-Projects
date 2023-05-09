#Author:    Marco Breton
#
#Purpose:   Phonebook application project for The Tech Academy's
#           Python Course.

import tkinter as tk
from tkinter import *

#importing my other modules
import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that my class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define my master frame configuration
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        #this center_window will center the app on user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook App")
        self.master.configure(bg = "#F0F0F0")
        #this protocol method is a built-in tkinter method which catches if
        #user clicks on the upper corner, "X".
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))

        #loads in GUI methods from separate module,
        #keeping my code comparmentalized and clutter free.
        phonebook_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
