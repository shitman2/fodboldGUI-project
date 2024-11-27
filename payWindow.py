from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master  # reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("300x250")

        Label(self.payWindow, text="Beløb").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.text = Label(self.payWindow, text="Navn")
        self.text.pack()

        self.name = Entry(self.payWindow)
        self.name.pack()

        self.transaction_type = StringVar(value="pay")
        self.pay_radio = Radiobutton(self.payWindow, text="Betal", variable=self.transaction_type, value="pay")
        self.pay_radio.pack()
        self.withdraw_radio = Radiobutton(self.payWindow, text="Træk penge", variable=self.transaction_type, value="withdraw")
        self.withdraw_radio.pack()

        self.button = Button(self.payWindow, text="Bekræft", command=self.processMoney)
        self.button.pack(pady=10)

        self.backButton = Button(self.payWindow, text="Tilbage", command=self.goBack)
        self.backButton.pack(pady=10)

    def processMoney(self):
        try:
            amount = abs(int(self.money.get()))
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        name = self.name.get().strip()
        if not name:
            messagebox.showerror(parent=self.payWindow, title="Navn fejl!", message="Navn må ikke være tomt.")
            return

        if name not in self.master.fodboldtur:
            self.master.fodboldtur[name] = 0  # Initialize if the name doesn't exist

        if self.transaction_type.get() == "pay":
            self.master.fodboldtur[name] += amount
        else:
            self.master.fodboldtur[name] -= amount

        self.master.total = sum(self.master.fodboldtur.values())
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        self.master.progress['value'] = self.master.total / self.master.target * 100

        self.master.gemFilen()  # Save the updated data
        print(f"Opdateret: {self.master.fodboldtur}")
        messagebox.showinfo(parent=self.payWindow, title="Success", message=f"Beløb opdateret for {name}.")
        self.goBack()

    def goBack(self):
        self.payWindow.destroy()