import tkinter as tk
player = []

class Remplacement:
    def __init__(self, JOUEURS_X, LABS_JOUEURS_X):
        self.noms_joueurs = JOUEURS_X
        self.labs_joueurs = LABS_JOUEURS_X
        self.root = tk.Tk()
        self.root.title("Remplacement")

        # grand label pour remplacant
        # equipeA
        remplacant_label = tk.LabelFrame(self.root, text="Remplacement", font=('cambria', 12, 'bold'))
        remplacant_label.pack()
        tk.Label(remplacant_label, text='Joueur à remplacer', font=('verdana', 8, 'italic')).grid(row=2, column=1)
        self.joueur_a_remplacer = tk.Entry(remplacant_label, font=('verdana', 8, 'italic'))
        self.joueur_a_remplacer.grid(row=2, column=2)
        tk.Label(remplacant_label, text='Remplaçant'.upper(), font=('verdana', 8, 'italic')).grid(row=3, column=1)
        self.le_remplacant = tk.Entry(remplacant_label, font=('verdana', 8, 'italic'))
        self.le_remplacant.grid(row=3, column=2)
        tk.Button(remplacant_label, text='Valider', font=('verdana', 10, 'bold'), bg='green', fg='white',
                  command=lambda: self.effectuer_remplacement(self.noms_joueurs, self.labs_joueurs)).grid(row=5,
                                                                                                          column=2,
                                                                                                          sticky=tk.E,
                                                                                                          padx=3)

        self.root.mainloop()

    def effectuer_remplacement(self, noms_joueurs, labs_joueurs):
        # on verifie si les champs correspondants ont ete bien saisi
        if len(self.joueur_a_remplacer.get()) and len(self.le_remplacant.get()) != 0:
            # dans ce cas on recupere ce qui a ete saisi dans ces champs:
            a_remplacer = self.joueur_a_remplacer.get().upper()
            remplacant = self.le_remplacant.get().upper()
            # on verifie si le joueur a remplacer se trouve bel et bien sur la liste des joueurs
            if a_remplacer in noms_joueurs:
                # alors on recupere l'index
                index = noms_joueurs.index(a_remplacer)
                # on le supprime de la liste des joueurs
                noms_joueurs.remove(noms_joueurs[index])
                noms_joueurs.insert(index, remplacant)

            # maintenant il faut mettre a jour la liste des joueurs
            for i, joueur in enumerate(noms_joueurs):
                labs_joueurs[i]['text'] = joueur.upper()
                player.append(joueur)
