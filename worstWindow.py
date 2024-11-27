# importing tkinter module
from tkinter import *
import tkinter as tk

def findThreeLowestValues(d):
    # Sorter dictionaryens elementer baseret på deres værdier
    sorted_items = sorted(d.items(), key=lambda item: item[1])
    # Vælg de første tre elementer (nøglerne til de tre laveste værdier)
    lowest_keys = [item[0] for item in sorted_items[:3]]
    # Convert List to Dict
    lowest_keys = [(index, item) for index, item in enumerate(lowest_keys)]
    lowest_keys = dict(lowest_keys)
    return lowest_keys

class worstWindowClass:
    def __init__(self, master):
        self.master = master  # reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("300x300")  # Increased size for better layout

        Label(self.worstWindow, text="De værste betalere").pack(pady=10)

        listbox = tk.Listbox(self.worstWindow, width=40, height=10)
        for item in findThreeLowestValues(self.master.fodboldtur).items():
            listbox.insert(tk.END, item)
        listbox.pack(pady=10)

        # ADD BACK BUTTON BELOW LISTBOX
        self.backButton = Button(self.worstWindow, text="Tilbage", command=self.goBack)
        self.backButton.pack(pady=10)

    def goBack(self):
        self.worstWindow.destroy()
