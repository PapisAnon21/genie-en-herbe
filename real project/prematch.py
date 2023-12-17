import tkinter as tk
from players import Players
from teams import Teams
from lancement import Debut

EQUIPE_A = ""
EQUIPE_B = ""
NOMS_JOUEUR_A = ""
NOMS_JOUEUR_B = ""


class Prematch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x700+400+50")
        self.players = Players(self.root)
        self.teams = Teams(self.root)
        self.game_logo()
        self.create_widgets()
        self.root.bind("<Return>", self.lancer_le_match)
        self.root.mainloop()

    def create_widgets(self):
        # Equipes et Joueurs
        self.players.nom_joueurs.grid(row=1, column=0, pady=4, sticky=tk.W, padx=100)
        # Equipes
        self.teams.equipeA.grid(row=2, column=0, sticky=tk.W, pady=40, padx=0)
        self.teams.champA.place(x=190, y=340)
        self.teams.equipeB.grid(row=3, column=0, sticky=tk.W, pady=40, padx=0)
        self.teams.champB.place(x=190, y=475)

        # Joueurs
        self.players.joueurA_type_label.grid(row=2, sticky=tk.W, pady=40, padx=300)
        self.players.champ_joueurs_A.grid(row=2, padx=450, sticky=tk.W)
        self.players.joueurB_type_label.grid(row=3, sticky=tk.W, pady=40, padx=300)
        self.players.champ_joueurs_B.grid(row=3, padx=450, sticky=tk.W)

        # Valider les donnees
        valider = tk.Button(self.root, text='Valider les Entrees', command=lambda: self.lancer_le_match(None),
                            font=('calibri', '18', 'italic'), bg='green', fg='white')
        valider.grid(sticky=tk.W, padx=300)

        # Champs de messages
        self.message_alerte = tk.Label(self.root, text='', font=('Cambria', 12, 'bold'))
        self.message_alerte.grid(row=4)

    def lancer_le_match(self, event):
        global EQUIPE_A, EQUIPE_B, NOMS_JOUEUR_A, NOMS_JOUEUR_B
        # avant que cette fenetre ne se charge on doit verifier si les donne ont ete bien entre
        # donc verifions par la methode
        if self.players.verifier_champs_joueurs():
            # on recuperer ce qui est entre dans les champs

            EQUIPE_A = self.teams.champA.get()
            EQUIPE_B = self.teams.champB.get()
            NOMS_JOUEUR_A = self.players.champ_joueurs_A.get()
            NOMS_JOUEUR_B = self.players.champ_joueurs_B.get()
            self.root.destroy()
            Debut()

        else:
            self.message_alerte['text'] = 'Entrez toutes les donnees valide du match'

    def game_logo(self):
        logo = tk.PhotoImage(file='logos/logo.png')
        label_logo = tk.Label(image=logo)
        label_logo.image = logo
        label_logo.grid(row=0, padx=275, pady=50, sticky=tk.W)
