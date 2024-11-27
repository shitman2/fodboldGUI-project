# importing tkinter module
import pickle
from tkinter import *
from tkinter.ttk import * #progressbar
from tkinter import messagebox


from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass

class mainWindow:
    def __init__(self):


        self.total = 0
        self.target = 4500

        # creating tkinter window
        self.root = Tk()

        #load filen:
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        try: #FILEN FINDES :)
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
        except: #FILEN FINDES IKKE.
            ##TODO: open file??
            ##TODONE: warn a brother
            messagebox.showerror(parent=self.root, title="GWAAAAAAA", message="FILEN ER IKKE FUNDET!!")
        print(self.fodboldtur)
        self.total = sum(self.fodboldtur.values())
        print(f"TOTAL: {self.total}")


        #TEXT:
        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
        self.progress.pack(padx= 20)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)


        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()
    def gemFilen(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()
        print("GEMT")

if __name__ == '__main__':
    main = mainWindow()