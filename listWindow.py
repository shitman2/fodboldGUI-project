from tkinter import *
import tkinter as tk

class listWindowClass:
    def __init__(self, master):
        self.master = master
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger").pack()

        listbox = tk.Listbox(self.listWindow, width=40, height=10)
        for name, amount in self.master.fodboldtur.items():
            listbox.insert(tk.END, f"{name}: {amount} kr")
        listbox.pack()

        def printliste():
            for name, amount in self.master.fodboldtur.items():
                print(f"{name}: {amount} kr")
            print("Er beløbet betalt?")

        printliste()

        # Back Button
        self.backButton = Button(self.listWindow, text="Tilbage", command=self.goBack)
        self.backButton.pack(pady=10)

    def goBack(self):
        self.listWindow.destroy()
