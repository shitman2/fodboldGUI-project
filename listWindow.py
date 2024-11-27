from tkinter import *
import tkinter as tk

class listWindowClass:
    def __init__(self, master):
        self.master = master  # Reference to the main window object
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger").pack()

        #Liste
        self.listbox = tk.Listbox(self.listWindow, width=40, height=10)
        self.listbox.pack()

        # Update Listbox
        def updateList():
            self.listbox.delete(0, tk.END)  # Clear the Listbox
            for item in self.master.fodboldtur.items():  # Add all items
                self.listbox.insert(tk.END, f"{item[0]}: {item[1]}")

        # Function to update the dropdown menu
        def updateDropdown():
            menu = self.removeName["menu"]  # Access the OptionMenu's menu
            menu.delete(0, "end")  # Clear all options
            for key in self.master.fodboldtur:  # Add updated options
                menu.add_command(label=key, command=lambda value=key: self.clicked.set(value))

        # Add a new member
        def addMember():
            name = str(self.addName.get())
            if name:  # Ensure the name is not empty
                self.master.fodboldtur[name] = 0
                updateList()
                updateDropdown()
                self.addName.delete(0, tk.END)  # Clear the entry field

        # Remove a selected member
        def removeMember():
            key = self.clicked.get()
            if key in self.master.fodboldtur:
                del self.master.fodboldtur[key]
                updateList()
                updateDropdown()

        # Text and Entry for adding members
        Label(self.listWindow, text="Tilføj medlemmer").pack()
        self.addName = Entry(self.listWindow)
        self.addName.pack()

        addButton = Button(self.listWindow, text="Tilføj", command=addMember)
        addButton.pack(padx=20, pady=10)

        # Text and Dropdown for removing members
        Label(self.listWindow, text="Fjern medlemmer").pack()
        self.clicked = StringVar()
        self.clicked.set("Valg medlem")
        self.removeName = OptionMenu(self.listWindow, self.clicked, *self.master.fodboldtur)
        self.removeName.pack()

        removeButton = Button(self.listWindow, text="Fjern", command=removeMember)
        removeButton.pack(padx=20, pady=10)

        # Initialize the Listbox and Dropdown with current data
        updateList()
        updateDropdown()

        # Save the file (if implemented in master)
        self.master.gemFilen()

        # Print the current dictionary
        def printliste():
            for item in self.master.fodboldtur.items():
                print(item)

        printliste()
