from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master  # reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("300x250")  # Increased size to fit new elements

        Label(self.payWindow, text="Beløb").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.text = Label(self.payWindow, text="Navn")
        self.text.pack()

        self.name = Entry(self.payWindow)
        self.name.pack()

        # Radio buttons for selecting payment or withdrawal
        self.transaction_type = StringVar(value="pay")  # Default to "pay"
        self.pay_radio = Radiobutton(self.payWindow, text="Betal", variable=self.transaction_type, value="pay")
        self.pay_radio.pack()
        self.withdraw_radio = Radiobutton(self.payWindow, text="Træk penge", variable=self.transaction_type, value="withdraw")
        self.withdraw_radio.pack()

        self.button = Button(self.payWindow, text="Bekræft", command=self.processMoney)
        self.button.pack(pady=10)

        # Back button
        self.backButton = Button(self.payWindow, text="Tilbage", command=self.goBack)
        self.backButton.pack(pady=10)

    def processMoney(self):
        try:
            amount = abs(int(self.money.get()))  # Validate input for positive integers only
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        name = self.name.get().strip()
        if not name:
            messagebox.showerror(parent=self.payWindow, title="Navn fejl!", message="Navn må ikke være tomt.")
            return

        if self.transaction_type.get() == "pay":
            self.master.total += amount
            print(f"{amount} kr. betalt af {name}.")
        else:  # withdraw
            self.master.total -= amount
            print(f"{amount} kr. trukket fra {name}.")

        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        self.master.gemFilen()

    def goBack(self):
        self.payWindow.destroy()
