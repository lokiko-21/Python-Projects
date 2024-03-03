import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #title for tkinter page
        self.master.title("Web Page Generator")

        #this button activates the html webpage
        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=2, padx=(2, 2), pady=(10, 10), sticky=E)

        #this button will add the custom text to the web page
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=3, padx=(2, 2), pady=(10, 10), sticky=E)

        #label for entry box
        self.lbl_text = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lbl_text.grid(row=0, column=0, columnspan=4)

        #this entry box will be text that the user will input into the web page
        self.txt_entry = Entry(self.master, text='', width=120)
        self.txt_entry.grid(row=1, column=0, columnspan=4, padx=(5, 5), pady=(1, 1))


    #this function is our default html web page
    def defaultHTML(self):
        #my h1 text
        htmlText = "Stay tuned for our amazing summer sale!"
        #setting index.html to htmlFile
        htmlFile = open("index.html", "w")
        #html code
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #inserting my html code inside of index.html
        htmlFile.write(htmlContent)
        htmlFile.close()
        #opens index.html on a new tab in the web browser
        webbrowser.open_new_tab("index.html")


    #this function is custom text that a user can add to the web page
    def customHTML(self):
        #custom <p> text from user
        customText = self.txt_entry.get()
        htmlText = "Stay tuned for our amazing summer sale!"
        #setting index.html to htmlFile
        htmlFile = open("index.html", "w")
        #html code
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n<p>" + customText + "</p>\n</body>\n</html>"
        #inserting my html code inside of index.html
        htmlFile.write(htmlContent)
        htmlFile.close()
        #opens index.html on a new tab in the web browser
        webbrowser.open_new_tab("index.html")
        



























if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
