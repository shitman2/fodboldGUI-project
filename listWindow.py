# importing tkinter module
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image #image stuff - install package: Pillow

#gwaa
class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger").pack()

        listbox = tk.Listbox(self.listWindow, width=40, height=10)
        for item in self.master.fodboldtur.items():
            listbox.insert(tk.END, item)
        listbox.pack()
        def printliste():
            for item in self.master.fodboldtur.items():
                print(item)
            print("Er beløbet betalt?")

        printliste()
