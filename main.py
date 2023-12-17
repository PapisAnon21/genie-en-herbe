import tkinter as tk
from teams import Teams
from chrono import Chrono
from scores import Scores
import prematch
import countdown
import remplacement
import fin_match
from web_electronic import envoi_donne_au_serveur_players_teams
import time, threading 


def foo(): 
    print(time.ctime())
    print("salut") 
    threading.Timer(10, foo).start() 

foo()

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
JOUEURS_A = []
JOUEURS_B = []
LABS_JOUEURS_A = []
LABS_JOUEURS_B = []


class Main:
    def __init__(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        self.root = tk.Tk()
        self.teams = Teams(self.root)
        self.equipeA_name = prematch.EQUIPE_A
        self.equipeB_name = prematch.EQUIPE_B
        SCREEN_WIDTH = self.root.winfo_screenwidth()
        SCREEN_HEIGHT = self.root.winfo_screenheight()
        self.root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT) + "+0+0")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")
        self.create_widgets()
        self.joueurs()
        foo()
        MenuBar(self.root)
        countdown.CountDown(self.root)
        self.root.title(self.equipeA_name.upper() + ' vs ' + self.equipeB_name.upper())
        try:
            self.envoi_donne_au_serveur_team_player()
        except:
            print("erreur lors de l'envoi au Serveur")
        self.root.mainloop()

    def create_widgets(self):
        self.logo_equipe_A = tk.PhotoImage(file='logos/' + self.equipeA_name + '_1_3D.png')
        self.logo_A = tk.Label(image=self.logo_equipe_A, bg="white")
        self.logo_A.image = self.logo_equipe_A
        self.logo_A.place(x=1 * SCREEN_WIDTH / 10, y=0)

        self.logo = tk.PhotoImage(file='logos/logo.png')
        self.logo_p = tk.Label(image=self.logo, bg="white")
        self.logo_p.place(x=4 * SCREEN_WIDTH / 10)

        self.logo_equipe_B = tk.PhotoImage(file='logos/' + self.equipeB_name + '_2_3D.png')
        self.logo_B = tk.Label(image=self.logo_equipe_B, bg="white")
        self.logo_B.image = self.logo_equipe_B
        self.logo_B.place(x=7 * SCREEN_WIDTH / 10, y=0)
        Chrono(root=self.root)
        Scores(root=self.root)

        tk.Button(text='Fin du Match '.upper(), font=('calibri', '18', 'bold'), bg='white', fg='green',
                  command=lambda: fin_match.FinMatch(self.root)).place(x=9 * SCREEN_WIDTH / 10 - 30,
                                                                       y=6.3 * SCREEN_HEIGHT / 9 + 109)
        tk.Button(text='quitter le match '.upper(), command=self.root.destroy,
                  font=('calibri', '15', 'bold'), bg='white', fg='IndianRed').place(x=1 * SCREEN_WIDTH / 25 - 50,
                                                                                    y=6.3 * SCREEN_HEIGHT / 9 + 115)

    def joueurs(self):
        global JOUEURS_A, JOUEURS_B, LABS_JOUEURS_A, LABS_JOUEURS_B
        # Afficher le noms des Joueurs de l'équipe A
        JOUEURS_A = prematch.NOMS_JOUEUR_A.upper().split(", ")
        grandlabel = tk.LabelFrame(self.root, text="JOUEURS", font=('cambria', 20, 'bold', 'underline'), bg="ivory")
        grandlabel.place(x=1.5 * SCREEN_WIDTH / 25 - 50, y=2.6 * SCREEN_HEIGHT / 9 + 50)
        self.add_player_name(grandlabel, JOUEURS_A, LABS_JOUEURS_A, "blue")

        # Afficher le noms des Joueurs de l'équipe A
        JOUEURS_B = prematch.NOMS_JOUEUR_B.upper().split(", ")
        grandlabel2 = tk.LabelFrame(self.root, text="JOUEURS", font=('cambria', 20, 'bold', 'underline'), bg="ivory")
        grandlabel2.place(x=20.6 * SCREEN_WIDTH / 25 - 60, y=2.6 * SCREEN_HEIGHT / 9 + 50)
        self.add_player_name(grandlabel2, JOUEURS_B, LABS_JOUEURS_B, "red")

    def add_player_name(self, master, joueurs, labs_joueurs, fg):
        for i, joueur in enumerate(joueurs):
            j = tk.Label(master, text=joueur, font=('book antiqua', 18, 'bold'), fg=fg, bg="ivory", width=19)
            j.grid(row=2 + i, pady=3)
            labs_joueurs.append(j)
    def envoi_donne_au_serveur_team_player(self):
        donne_envoyer = {
    
                        'equipe' : {
                            'equipeA': self.equipeA_name , 
                            'equipeB': self.equipeB_name
                                    },

                        'joueurs' : {
                                    'joueursA' : JOUEURS_A,
                                    'joueursB' : JOUEURS_B
                                    }

                        }
        envoi_donne_au_serveur_players_teams(adresse_serveur, donne_envoyer)
    #def envoi_score_au_serveur():

# Barre de Menu
class MenuBar:
    def __init__(self, root):
        global JOUEURS_A, JOUEURS_B, LABS_JOUEURS_A, LABS_JOUEURS_B
        self.root = root
        self.barre_menu = tk.Menu(self.root)
        # Menu Remplacements
        self.menu_remplacement = tk.Menu(self.barre_menu, tearoff=0)
        self.barre_menu.add_cascade(label="Remplacement", menu=self.menu_remplacement)
        self.menu_remplacement.add_command(label="Equipe A",
                                           command=lambda: remplacement.Remplacement(JOUEURS_A, LABS_JOUEURS_A))
        self.menu_remplacement.add_command(label="Equipe B",
                                           command=lambda: remplacement.Remplacement(JOUEURS_B, LABS_JOUEURS_B))
        # Menu Couleurs
        menu_couleur = tk.Menu(self.barre_menu, tearoff=0)
        self.barre_menu.add_cascade(label="Couleur")
        self.root.config(menu=self.barre_menu)
