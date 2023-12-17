import tkinter as tk
from teams import Teams
from chrono import Chrono
from scores import Scores
import prematch
import countdown
import remplacement
import fin_match
import json

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
JOUEURS_A = []
JOUEURS_B = []
LABS_JOUEURS_A = []
LABS_JOUEURS_B = []

widgets = {}
widgets_placement = {}
try:
    with open("save.json", "r") as sv:
        widgets_placement = json.load(sv)
except Exception as e:
    widgets_placement = {}


class MoveWidget:
    def __init__(self, widget, root):
        self.widget = widget
        self.root = root
        self.x = widgets[self.widget]["x"]
        self.y = widgets[self.widget]["y"]
        self.dx = 4
        self.dy = 4
        self.win = tk.Toplevel(self.root)
        self.win.resizable(False, False)
        self.win.geometry("200x150")
        self.bind_win()
        self.btn_up = tk.Button(self.win, text="Up", command=lambda: self.move_up(None))
        self.btn_down = tk.Button(self.win, text="Down", command=lambda: self.move_down(None))
        self.btn_left = tk.Button(self.win, text="Left", command=lambda: self.move_left(None))
        self.btn_right = tk.Button(self.win, text="right", command=lambda: self.move_right(None))
        self.btn_fin = tk.Button(self.win, text="Terminé", command=self.finish, bg="green", fg="white")

        self.btn_up.pack(anchor=tk.N, side=tk.TOP)
        self.btn_down.pack(anchor=tk.S, side=tk.BOTTOM)
        self.btn_left.pack(anchor=tk.W, side=tk.LEFT)
        self.btn_right.pack(anchor=tk.E, side=tk.RIGHT)
        self.btn_fin.pack(anchor=tk.CENTER, side=tk.BOTTOM, pady=35)

        self.win.mainloop()

    def move_right(self, event):
        self.x += self.dx
        widgets[self.widget]["widget"].place(x=self.x, y=self.y)
        self.update_position()

    def move_left(self, event):
        self.x -= self.dx
        widgets[self.widget]["widget"].place(x=self.x, y=self.y)
        self.update_position()

    def move_down(self, event):
        self.y += self.dy
        widgets[self.widget]["widget"].place(x=self.x, y=self.y)
        self.update_position()

    def move_up(self, event):
        self.y -= self.dy
        widgets[self.widget]["widget"].place(x=self.x, y=self.y)
        self.update_position()

    def finish(self):
        self.unbind_win()
        self.win.destroy()

    def bind_win(self):
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)

    def unbind_win(self):
        self.root.unbind("<Right>")
        self.root.unbind("<Left>")
        self.root.unbind("<Up>")
        self.root.unbind("<Down>")

    def update_position(self):
        widgets[self.widget]["x"] = self.x
        widgets[self.widget]["y"] = self.y


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

        countdown.CountDown(self.root)
        self.root.title(self.equipeA_name.upper() + ' vs ' + self.equipeB_name.upper())
        MenuBar(self.root)
        self.root.mainloop()
        for wid in widgets:
            widgets_placement[wid] = {"x": widgets[wid]["x"], "y": widgets[wid]["y"]}

        with open("save.json", "w") as save:
            json.dump(widgets_placement, save)

    def create_widgets(self):
        self.logo_equipe_A = tk.PhotoImage(file='logos/' + self.equipeA_name + '_1_3D.png')
        self.logo_A = tk.Label(image=self.logo_equipe_A, bg="white")
        self.logo_A.image = self.logo_equipe_A
        try:
            widgets["logo_A"] = {"name": "Logo A", "widget": self.logo_A, "x": widgets_placement["logo_A"]["x"],
                                 "y": widgets_placement["logo_A"]["y"]}
        except Exception as e:
            widgets["logo_A"] = {"name": "Logo A", "widget": self.logo_A, "x": 1 * SCREEN_WIDTH / 10, "y": 0}
        self.logo_A.place(x=widgets["logo_A"]["x"], y=widgets["logo_A"]["y"])

        self.logo = tk.PhotoImage(file='logos/logo.png')
        self.logo_p = tk.Label(image=self.logo, bg="white")
        try:
            widgets["logo_p"] = {"name": "Logo Principal", "widget": self.logo_p, "x": widgets_placement["logo_p"]["x"],
                                 "y": widgets_placement["logo_p"]["y"]}
        except Exception as e:
            widgets["logo_p"] = {"name": "Logo Principal", "widget": self.logo_p, "x": 4 * SCREEN_WIDTH / 10, "y": 0}
        self.logo_p.place(x=widgets["logo_p"]["x"], y=widgets["logo_p"]["y"])

        self.logo_equipe_B = tk.PhotoImage(file='logos/' + self.equipeB_name + '_2_3D.png')
        self.logo_B = tk.Label(image=self.logo_equipe_B, bg="white")
        self.logo_B.image = self.logo_equipe_B
        try:
            widgets["logo_B"] = {"name": "Logo B", "widget": self.logo_B, "x": widgets_placement["logo_B"]["x"],
                                 "y": widgets_placement["logo_B"]["y"]}
        except Exception as e:
            widgets["logo_B"] = {"name": "Logo B", "widget": self.logo_B, "x": 7 * SCREEN_WIDTH / 10, "y": 0}
        self.logo_B.place(x=widgets["logo_B"]["x"], y=widgets["logo_B"]["y"])
        
        Scores(root=self.root)

        btn_fin_match = tk.Button(text='Fin du Match '.upper(), font=('calibri', '18', 'bold'), bg='white', fg='green',
                                  command=lambda: fin_match.FinMatch(self.root))
        try:
            widgets["fin_match"] = {"name": "Bouton Fin du Match", "widget": btn_fin_match,
                                    "x": widgets_placement["fin_match"]["x"],
                                    "y": widgets_placement["fin_match"]["y"]}
        except Exception as e:
            widgets["fin_match"] = {"name": "Bouton Fin du Match", "widget": btn_fin_match,
                                    "x": 9 * SCREEN_WIDTH / 10 - 30,
                                    "y": 6.3 * SCREEN_HEIGHT / 9 + 109}
        btn_fin_match.place(x=widgets["fin_match"]["x"], y=widgets["fin_match"]["y"])

        btn_quit_match = tk.Button(text='quitter le match '.upper(), command=self.root.destroy,
                                   font=('calibri', '15', 'bold'), bg='white', fg='IndianRed')



        try:
            widgets["quit_match"] = {"name": "Bouton quitter le match", "widget": btn_quit_match,
                                     "x": widgets_placement["quit_match"]["x"],
                                     "y": widgets_placement["quit_match"]["y"]}
        except Exception as e:
            widgets["quit_match"] = {"name": "Bouton quitter le match", "widget": btn_quit_match,
                                     "x": 1 * SCREEN_WIDTH / 25 - 50, "y": 6.3 * SCREEN_HEIGHT / 9 + 115}
        btn_quit_match.place(x=widgets["quit_match"]["x"], y=widgets["quit_match"]["y"])


        #####ici
        Chrono(root=self.root)
        my_chrono_bouton = Chrono(self.root)
        deplacer_chrono_frame = my_chrono_bouton.creation_chrono_widgets()
        #Chrono(root=self.root).buttons_frame
        try:
            widgets["chronon_btns"] = {"name": "Boutons_chrono", "widget":deplacer_chrono_frame ,
                                     "x": widgets_placement["chronon_btns"]["x"] ,
                                     "y": widgets_placement["chronon_btns"]["y"]}
        except Exception as e:
            widgets["chronon_btns"] = {"name": "Boutons_chrono", "widget": deplacer_chrono_frame,
                                     "x":3 * SCREEN_WIDTH / 10 + 240, "y": 0.7 * SCREEN_HEIGHT / 9 + 180}
        deplacer_chrono_frame.place(x=widgets["chronon_btns"]["x"], y=widgets["chronon_btns"]["y"])

        text_chrono = my_chrono_bouton.create_text()

        try:
            widgets["chrono_text"] = {"name": "chrono_text", "widget":text_chrono ,
                                     "x": widgets_placement["chrono_text"]["x"] ,
                                     "y": widgets_placement["chrono_text"]["y"]}
        except Exception as e:
            widgets["chrono_text"] = {"name": "chrono_text", "widget": text_chrono,
                                     "x":3 * SCREEN_WIDTH / 10 + 140, "y": 1 * SCREEN_WIDTH / 9 - 25}
        text_chrono.place(x=widgets["chrono_text"]["x"], y=widgets["chrono_text"]["y"])


    def joueurs(self):
        global JOUEURS_A, JOUEURS_B, LABS_JOUEURS_A, LABS_JOUEURS_B
        # Afficher le noms des Joueurs de l'équipe A
        JOUEURS_A = prematch.NOMS_JOUEUR_A.upper().split(", ")
        grandlabel = tk.LabelFrame(self.root, text="JOUEURS", font=('cambria', 20, 'bold', 'underline'), bg="ivory")
        try:
            widgets["noms_A"] = {"name": "Joueurs A", "widget": grandlabel,
                                 "x": widgets_placement["noms_A"]["x"],
                                 "y": widgets_placement["noms_A"]["y"]}
        except Exception as e:
            widgets["noms_A"] = {"name": "Joueurs A", "widget": grandlabel, "x": 1.5 * SCREEN_WIDTH / 25 - 50,
                                 "y": 2.6 * SCREEN_HEIGHT / 9 + 50}
        grandlabel.place(x=widgets["noms_A"]["x"], y=widgets["noms_A"]["y"])

        self.add_player_name(grandlabel, JOUEURS_A, LABS_JOUEURS_A, "blue")

        # Afficher le noms des Joueurs de l'équipe A
        JOUEURS_B = prematch.NOMS_JOUEUR_B.upper().split(", ")
        grandlabel2 = tk.LabelFrame(self.root, text="JOUEURS", font=('cambria', 20, 'bold', 'underline'), bg="ivory")
        try:
            widgets["noms_B"] = {"name": "Joueurs B", "widget": grandlabel2,
                                 "x": widgets_placement["noms_B"]["x"],
                                 "y": widgets_placement["noms_B"]["y"]}
        except Exception as e:
            widgets["noms_B"] = {"name": "Joueurs B", "widget": grandlabel2, "x": 20.6 * SCREEN_WIDTH / 25 - 60,
                                 "y": 2.6 * SCREEN_HEIGHT / 9 + 50}
        grandlabel2.place(x=widgets["noms_B"]["x"], y=widgets["noms_B"]["y"])

        self.add_player_name(grandlabel2, JOUEURS_B, LABS_JOUEURS_B, "red")

    def add_player_name(self, master, joueurs, labs_joueurs, fg):
        for i, joueur in enumerate(joueurs):
            j = tk.Label(master, text=joueur, font=('book antiqua', 18, 'bold'), fg=fg, bg="ivory", width=19)
            j.grid(row=2 + i, pady=3)
            labs_joueurs.append(j)


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
        """
        # Menu Couleurs
        menu_couleur = tk.Menu(self.barre_menu, tearoff=0)
        self.barre_menu.add_cascade(label="Couleur", menu=menu_couleur)
        """
        # Menu Configurations
        self.config_menu = tk.Menu(self.barre_menu, tearoff=0)
        self.barre_menu.add_cascade(menu=self.config_menu, label="Configurations")

        self.move_widget = tk.Menu(self.config_menu, tearoff=0)
        self.config_menu.add_cascade(menu=self.move_widget, label="Déplacer Widget")

        for element in widgets:
            self.move_widget.add_command(label=widgets[element]["name"],
                                         command=lambda el=element: MoveWidget(widget=el, root=self.root))

        self.root.unbind("<Right>")
        self.root.config(menu=self.barre_menu)
