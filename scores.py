import tkinter as tk
from web_electronic import envoi_donne_au_serveur_scores
SCORE = {}


class Scores:
    def __init__(self, root):
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.create_widgets()

    def create_widgets(self):
        self.scoreA = tk.Label(self.root, text=0, font=('Book antiqua', 120, 'bold', 'underline'),
                               bg='khaki', fg='blue', width=3)
        self.scoreA.place(x=2.5 * self.screen_width / 10 - 50, y=4.3 * self.screen_height / 9, height=225)

        # score pour equipeB text
        self.scoreB = tk.Label(self.root, text=0, font=('Book antiqua', 120, 'bold', 'underline'),
                               bg='khaki', fg='red', width=3)
        self.scoreB.place(x=5 * self.screen_width / 10 + 40, y=4.3 * self.screen_height / 9, height=225)

        self.scoreA.bind("<Button-1>", lambda event: self.variation_score(event, self.scoreA, 10))
        self.scoreB.bind("<Button-1>", lambda event: self.variation_score(event, self.scoreB, 10))

        self.root.bind('<Key-1>', lambda event: self.variation_score(event, self.scoreA, 10))
        self.root.bind('<Key-2>', lambda event: self.variation_score(event, self.scoreB, 10))

        # --------------------------------------------
        # bouton pour incrementer le score
        tk.Button(text='+10 Points'.upper(), command=lambda: self.variation_score(None, self.scoreA, 10),
                  font=('calibri', '16', 'italic'), bg='white', fg='blue').place(x=self.screen_width / 10 + 70,
                                                                                 y=7 * self.screen_height / 9 - 25)

        tk.Button(text='+20 Points'.upper(), command=lambda: self.variation_score(None, self.scoreA, 20),
                  font=('calibri', '16', 'italic'), bg='white', fg='blue').place(x=3 * self.screen_width / 10 - 100,
                                                                                 y=7 * self.screen_height / 9 - 25)

        tk.Button(text='+10 Points'.upper(), command=lambda: self.variation_score(None, self.scoreB, 10),
                  font=('calibri', '16', 'italic'), bg='white', fg='red').place(x=6 * self.screen_width / 10 + 150,
                                                                                y=7 * self.screen_height / 9 - 25)

        tk.Button(text='+20 Points'.upper(), command=lambda: self.variation_score(None, self.scoreB, 20),
                  font=('calibri', '16', 'italic'), bg='white', fg='red').place(x=6 * self.screen_width / 10 + 300,
                                                                                y=7 * self.screen_height / 9 - 25)

        # boutons pour decreminter le score
        tk.Button(text='-10 Points'.upper(), command=lambda: self.variation_score(None, self.scoreA, -10),
                  font=('calibri', '16', 'italic'), bg='black', fg='blue').place(x=self.screen_width / 10 + 70,
                                                                                 y=7 * self.screen_height / 9 + 25)

        tk.Button(text='-20 Points '.upper(), command=lambda: self.variation_score(None, self.scoreA, -20),
                  font=('calibri', '16', 'italic'), bg='black', fg='blue').place(x=3 * self.screen_width / 10 - 100,
                                                                                 y=7 * self.screen_height / 9 + 25)

        tk.Button(text='-10 Points '.upper(), command=lambda: self.variation_score(None, self.scoreB, -10),
                  font=('calibri', '16', 'italic'), bg='black', fg='red').place(x=6 * self.screen_width / 10 + 150,
                                                                                y=7 * self.screen_height / 9 + 25)

        tk.Button(text='-20 Points '.upper(), command=lambda: self.variation_score(None, self.scoreB, -20),
                  font=('calibri', '16', 'italic'), bg='black', fg='red').place(x=6 * self.screen_width / 10 + 300,
                                                                                y=7 * self.screen_height / 9 + 25)
        SCORE["scoreA"] = int(self.scoreA["text"])
        SCORE["scoreB"] = int(self.scoreB["text"])
        print(SCORE)

    def variation_score(self, event, score, nb_points):
        ancien_score = score['text']
        nouveau_score = ancien_score + nb_points
        if nouveau_score >= 0:
            score['text'] = nouveau_score
        else:
            score["text"] = 0

        if score == self.scoreA:
            SCORE["scoreA"] = int(self.scoreA["text"])
        else:
            SCORE["scoreB"] = int(self.scoreB["text"])
        try:
          self.envoi_du_score()
        except:
          print("erreur lors de l'envoi du score")

    

    def envoi_du_score(self):
      donne_score = {'scoreA':int(self.scoreA["text"]) ,  'scoreB' :  int(self.scoreB["text"])}
      envoi_donne_au_serveur_scores(adresse , donne_score)
