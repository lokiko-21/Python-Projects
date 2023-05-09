import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        #self.master IS THE MAIN(MASTER) WINDOW DISPLAY
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgray')

        #MAKING STRING VARIABLES
        self.varFName = StringVar()
        self.varLName = StringVar()

        #FIRST NAME LABELS
        self.lblFName = Label(self.master, text='First Name', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        #LAST NAME LABELS
        self.lblLName = Label(self.master, text='Last Name', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))

        #SUBMIT BUTTON TEXT PLACEHOLDER
        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))

        #FIRST NAME TEXT BOX
        self.txtFName = Entry(self.master, text=self.varFName, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))

        #LAST NAME TEXT BOX
        self.txtLName = Entry(self.master, text=self.varLName, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))

        #SUBMIT BUTTON
        self.btnSubmit = Button(self.master, text = 'Submit', width = 10, height = 2, command = self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE)

        #CANCEL BUTTON
        self.btnCancel = Button(self.master, text = 'Cancel', width = 10, height = 2, command = self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0, 90), pady=(30, 0), sticky=NE)

    #SUBMIT BUTTON FUNCTIONALITY
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        #DISPLAYS THIS MESSAGE AFTER HITTING SUBMIT
        self.lblDisplay.config(text='Hello {} {}!'.format(fn, ln))

    #CANCEL BUTTON FUNCTIONALITY
    def cancel(self):
        #EXITS OUT OF THE PROGRAM
        self.master.destroy()










        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
