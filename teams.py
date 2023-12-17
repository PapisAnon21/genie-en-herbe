import tkinter as tk
from tkinter import ttk


class Teams:
    def __init__(self, root):
        self.root = root
        self.list_equipe = ('TC1', 'TC2', 'DIC1', 'DIC2', 'DIC3', "ANCIENS")
        self.donnees()

    def donnees(self):
        # Equipes

        # Equipe A
        self.equipeA = tk.Label(self.root, text='Equipe A:', font=('cambria', 30, 'bold'))
        self.champA = ttk.Combobox(self.root, width=8, font=('Cambria', 13))
        self.champA['values'] = self.list_equipe
        self.champA.insert(0, 'TC1')
        self.champA['state'] = 'readonly'

        # Equipe A
        self.equipeB = tk.Label(self.root, text='Equipe B:', font=('cambria', 30, 'bold'))
        self.champB = ttk.Combobox(self.root, width=8, font=('Cambria', 13))
        self.champB['values'] = self.list_equipe
        self.champB.insert(0, 'TC2')
        self.champB['state'] = 'readonly'
