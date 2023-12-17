import time
import tkinter as tk
import main


class CountDown:
    def __init__(self, root):
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Funtions Call
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.LabelFrame(self.root, text='Compte à rebours', font=('cambria', 14, 'bold'), bg="white",
                                         fg="black")
        try:
            main.widgets["countdown"] = {"name": "Compte à rebours", "widget": self.title_label,
                                         "x": main.widgets_placement["countdown"]["x"],
                                         "y": main.widgets_placement["countdown"]["y"]}
        except Exception as e:
            main.widgets["countdown"] = {"name": "Compte à rebours", "widget": self.title_label,
                                         "x": 3 * self.screen_width / 10 + 120, "y": 7.3 * self.screen_height / 9}
        self.title_label.place(x=main.widgets["countdown"]["x"], y=main.widgets["countdown"]["y"])

        # ----------------------------------------

        tk.Button(self.title_label, text="5 Secondes", command=lambda: self.submit(5),
                  font=("book antiqua", 13, "bold"), bg="aquamarine").grid(row=0, column=0, padx=0)
        tk.Button(self.title_label, text="10 Secondes", command=lambda: self.submit(10),
                  font=("book antiqua", 13, "bold"), bg="aquamarine").grid(row=0, column=1, padx=5)
        tk.Button(self.title_label, text="15 Secondes", command=lambda: self.submit(15),
                  font=("book antiqua", 13, "bold"), bg="aquamarine").grid(row=0, column=2, padx=5)
        tk.Button(self.title_label, text="30 Secondes", command=lambda: self.submit(30),
                  font=("book antiqua", 13, "bold"), bg="aquamarine").grid(row=0, column=3, padx=0)

    def submit(self, temps):
        self.decompte = tk.Tk()
        self.temps = temps

        self.decompte.deiconify()
        self.decompte.title("Compte à Rebours")
        self.decompte.geometry(str(self.screen_width) + "x" + str(self.screen_height))
        self.decompte.resizable(width=False, height=False)
        self.decompte_label = tk.Label(self.decompte, text='', font=('book antiqua', 500, 'bold'))
        self.decompte_label.pack(expand=True)

        while self.temps > -1:

            self.decompte_label.configure(text=str(self.temps))

            # Mis à jour de la fenêtre principale
            self.decompte.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if self.temps == 0:
                self.decompte.destroy()

            elif self.temps <= 6:
                self.decompte_label["fg"] = "red"

            self.temps -= 1
        self.decompte.mainloop()
