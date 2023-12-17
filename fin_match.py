import tkinter as tk
import scores
import prematch
import time
import sys


class FinMatch:
    def __init__(self, root):
        # tout d'abord on cherche si le match est null

        self.root = root
        self.equipeA_name = prematch.EQUIPE_A
        self.equipeB_name = prematch.EQUIPE_B
        gagnant = self.vainqueur()
        self.root.destroy()
        # on cree la derniere fenetre tk
        self.fen_resultat = tk.Tk()
        self.fen_resultat.title('GAGNANT DU JOUR :' + gagnant)
        self.fen_resultat.geometry('900x600')
        self.fen_resultat.resizable(width=False, height=False)
        bg = tk.PhotoImage(file='bg/gagnant.png')  # ici on charge le bg qui a pour img coupe
        bg_label = tk.Label(image=bg)
        bg_label.image = bg
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # la c'est lb de la coupe

        if gagnant == 'match null':
            # la on affiche l'image match null
            logo = tk.PhotoImage(file='logos/' + gagnant + '.png')
            label_logo = tk.Label(image=logo)
            label_logo.image = logo
            label_logo.place(x=100, y=10)
            bg_label.configure(image='')
        else:
            # bon dans ce cas on recupere le vainquer
            # gagant_logo = self.vainqueur
            # on recupere son logo
            logo = tk.PhotoImage(file='logos2D/' + gagnant + '.png')
            label_logo = tk.Label(image=logo)
            label_logo.image = logo
            label_logo.place(x=100, y=100)
        self.fen_resultat.after(1000, self.auto_quit)
        self.fen_resultat.mainloop()

    def auto_quit(self):
        time.sleep(5)
        sys.exit()

    def vainqueur(self):
        # Comparer les scores pour trouver le vainqueur le vainqueur
        if scores.SCORE["scoreA"] > scores.SCORE["scoreB"]:
            # alors l'equipe A est le vainqueur
            vainqueur = self.equipeA_name
        elif scores.SCORE["scoreA"] < scores.SCORE["scoreB"]:
            # alors l'equipe B est le vainqueur
            vainqueur = self.equipeB_name
        else:
            vainqueur = 'match null'
        return vainqueur
