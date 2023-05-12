import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        #sets title of my GUI window
        self.master.title("File Transfer")
        
        #creates button to select files from the source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #positions source button in GUI using tkinter's grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkinter's grid() padx/y are the same
        #as the button to ensure they line up correct
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creating button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #positions destination button in GUI using tkinter's grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
        
        #creating entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #positions entry in GUI using tkinter's grid(). padx/y are the same
        #as button to ensure they will line up together
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #creates button to transfer files
        self.transfer_btn = Button(text='Transfer Files', width=20, command=self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


    #function that selects source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory(title="selectFile")
        
        #the .delete(0, END) will clear content that's inserted in the Entry widget,
        #this allows path to be inserted into Entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)


    #function that selects destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()

        #the .delete(0, END) will clear content that's inserted in the Entry widget,
        #this allows path to be inserted into Entry widget properly
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.destination_dir.insert(0, selectDestDir)
        

    #function that transfers files from one directory to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of all the files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')
            #CONTINUE HERE LOKIKO!!!!


    #function that exits program
    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method tells
        #python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
