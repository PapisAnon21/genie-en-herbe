import tkinter as tk
from tkinter.font import BOLD


class Players:
    def __init__(self, root):
        self.root = root
        self.donnees()

    def donnees(self):
        # Donnees Joueurs et Equipes
        # noms des joueurs
        self.nom_joueurs = tk.Label(self.root, text='Saisissez le nom des Equipes ainsi que des Joueurs',
                                    font=('Cambria', 20, 'bold'), fg='#c59c1b')

        # noms des joueurs de l'équipe A
        self.joueurA_type_label = tk.Label(self.root, text='Joueurs:', font=('calibri', 20, 'bold'))
        self.champ_joueurs_A = tk.Entry(self.root, width=30, font=('Calibri', 15, 'bold'))
        self.champ_joueurs_A.insert(0, "")
        # noms des joueurs de l'équipe B
        self.joueurB_type_label = tk.Label(self.root, text='Joueurs:', font=('calibri', 20, 'bold'))
        self.champ_joueurs_B = tk.Entry(self.root, width=30, font=('Calibri', 15, 'bold'))
        self.champ_joueurs_B.insert(0, "")

    def verifier_champs_joueurs(self):
        cja = self.champ_joueurs_A.get()
        cjb = self.champ_joueurs_B.get()
        # print(ca , cb)
        verifier = len(cja) != 0 and len(cjb) != 0
        return verifier
