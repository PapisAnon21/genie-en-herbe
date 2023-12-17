import tkinter as tk
import main

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
        try:
            main.widgets["score_A"] = {"name": "Score A", "widget": self.scoreA,
                                       "x": main.widgets_placement["score_A"]["x"],
                                       "y": main.widgets_placement["score_A"]["y"]}
        except Exception as e:
            main.widgets["score_A"] = {"name": "Score A", "widget": self.scoreA,
                                       "x": 2.5 * self.screen_width / 10 - 50, "y": 4.3 * self.screen_height / 9}
        self.scoreA.place(x=main.widgets["score_A"]["x"], y=main.widgets["score_A"]["y"])

        # score pour equipeB text
        self.scoreB = tk.Label(self.root, text=0, font=('Book antiqua', 120, 'bold', 'underline'),
                               bg='khaki', fg='red', width=3)
        try:
            main.widgets["score_B"] = {"name": "Score B", "widget": self.scoreB,
                                       "x": main.widgets_placement["score_B"]["x"],
                                       "y": main.widgets_placement["score_B"]["y"]}
        except Exception as e:
            main.widgets["score_B"] = {"name": "Score B", "widget": self.scoreB,
                                       "x": 5 * self.screen_width / 10 + 40, "y": 4.3 * self.screen_height / 9}
        self.scoreB.place(x=main.widgets["score_B"]["x"], y=main.widgets["score_B"]["y"])

        self.scoreA.bind("<Button-1>", lambda event: self.variation_score(event, self.scoreA, 10))
        self.scoreB.bind("<Button-1>", lambda event: self.variation_score(event, self.scoreB, 10))

        self.root.bind('<Key-1>', lambda event: self.variation_score(event, self.scoreA, 10))
        self.root.bind('<Key-2>', lambda event: self.variation_score(event, self.scoreB, 10))

        # --------------------------------------------
        # bouton pour incrementer le score
        btn_add_10_A = tk.Button(text='+10 Points'.upper(), command=lambda: self.variation_score(None, self.scoreA, 10),
                                 font=('calibri', '16', 'italic'), bg='white', fg='blue')
        try:
            main.widgets["add_10_A"] = {"name": "+10 Points (A)", "widget": btn_add_10_A,
                                        "x": main.widgets_placement["add_10_A"]["x"],
                                        "y": main.widgets_placement["add_10_A"]["y"]}
        except Exception as e:
            main.widgets["add_10_A"] = {"name": "+10 Points (A)", "widget": btn_add_10_A,
                                        "x": self.screen_width / 10 + 70, "y": 7 * self.screen_height / 9 - 25}
        btn_add_10_A.place(x=main.widgets["add_10_A"]["x"], y=main.widgets["add_10_A"]["y"])

        btn_add_20_A = tk.Button(text='+20 Points'.upper(), command=lambda: self.variation_score(None, self.scoreA, 20),
                                 font=('calibri', '16', 'italic'), bg='white', fg='blue')
        try:
            main.widgets["add_20_A"] = {"name": "+20 Points (A)", "widget": btn_add_20_A,
                                        "x": main.widgets_placement["add_20_A"]["x"],
                                        "y": main.widgets_placement["add_20_A"]["y"]}
        except Exception as e:
            main.widgets["add_20_A"] = {"name": "+20 Points (A)", "widget": btn_add_20_A,
                                        "x": 3 * self.screen_width / 10 - 100, "y": 7 * self.screen_height / 9 - 25}
        btn_add_20_A.place(x=main.widgets["add_20_A"]["x"], y=main.widgets["add_20_A"]["y"])

        btn_add_10_B = tk.Button(text='+10 Points'.upper(), command=lambda: self.variation_score(None, self.scoreB, 10),
                                 font=('calibri', '16', 'italic'), bg='white', fg='red')
        try:
            main.widgets["add_10_B"] = {"name": "+10 Points (B)", "widget": btn_add_10_B,
                                        "x": main.widgets_placement["add_10_B"]["x"],
                                        "y": main.widgets_placement["add_10_B"]["y"]}
        except Exception as e:
            main.widgets["add_10_B"] = {"name": "+10 Points (B)", "widget": btn_add_10_B,
                                        "x": 6 * self.screen_width / 10 + 150, "y": 7 * self.screen_height / 9 - 25}
        btn_add_10_B.place(x=main.widgets["add_10_B"]["x"], y=main.widgets["add_10_B"]["y"])

        btn_add_20_B = tk.Button(text='+20 Points'.upper(), command=lambda: self.variation_score(None, self.scoreB, 20),
                                 font=('calibri', '16', 'italic'), bg='white', fg='red')
        try:
            main.widgets["add_20_B"] = {"name": "+20 Points (B)", "widget": btn_add_20_B,
                                        "x": main.widgets_placement["add_20_B"]["x"],
                                        "y": main.widgets_placement["add_20_B"]["y"]}
        except Exception as e:
            main.widgets["add_20_B"] = {"name": "+20 Points (B)", "widget": btn_add_20_B,
                                        "x": 6 * self.screen_width / 10 + 300, "y": 7 * self.screen_height / 9 - 25}
        btn_add_20_B.place(x=main.widgets["add_20_B"]["x"], y=main.widgets["add_20_B"]["y"])

        # boutons pour decreminter le score
        btn_m_10_A = tk.Button(text='-10 Points'.upper(), command=lambda: self.variation_score(None, self.scoreA, -10),
                               font=('calibri', '16', 'italic'), bg='black', fg='blue')
        try:
            main.widgets["add_m10_A"] = {"name": "-10 Points (A)", "widget": btn_m_10_A,
                                        "x": main.widgets_placement["add_m10_A"]["x"],
                                        "y": main.widgets_placement["add_m10_A"]["y"]}
        except Exception as e:
            main.widgets["add_m10_A"] = {"name": "-10 Points (A)", "widget": btn_m_10_A,
                                         "x": self.screen_width / 10 + 70, "y": 7 * self.screen_height / 9 + 25}
        btn_m_10_A.place(x=main.widgets["add_m10_A"]["x"], y=main.widgets["add_m10_A"]["y"])

        btn_m_20_A = tk.Button(text='-20 Points '.upper(), command=lambda: self.variation_score(None, self.scoreA, -20),
                               font=('calibri', '16', 'italic'), bg='black', fg='blue')
        try:
            main.widgets["add_m20_A"] = {"name": "-20 Points (A)", "widget": btn_m_20_A,
                                         "x": main.widgets_placement["add_m20_A"]["x"],
                                         "y": main.widgets_placement["add_m20_A"]["y"]}
        except Exception as e:
            main.widgets["add_m20_A"] = {"name": "-20 Points (A)", "widget": btn_m_20_A,
                                         "x": 3 * self.screen_width / 10 - 100, "y": 7 * self.screen_height / 9 + 25}
        btn_m_20_A.place(x=main.widgets["add_m20_A"]["x"], y=main.widgets["add_m20_A"]["y"])

        btn_m_10_B = tk.Button(text='-10 Points '.upper(), command=lambda: self.variation_score(None, self.scoreB, -10),
                               font=('calibri', '16', 'italic'), bg='black', fg='red')
        try:
            main.widgets["add_m10_B"] = {"name": "-10 Points (B)", "widget": btn_m_10_B,
                                         "x": main.widgets_placement["add_m10_B"]["x"],
                                         "y": main.widgets_placement["add_m10_B"]["y"]}
        except Exception as e:
            main.widgets["add_m10_B"] = {"name": "-10 Points (B)", "widget": btn_m_10_B,
                                         "x": 6 * self.screen_width / 10 + 150, "y": 7 * self.screen_height / 9 + 25}
        btn_m_10_B.place(x=main.widgets["add_m10_B"]["x"], y=main.widgets["add_m10_B"]["y"])

        btn_m_20_B = tk.Button(text='-20 Points '.upper(), command=lambda: self.variation_score(None, self.scoreB, -20),
                               font=('calibri', '16', 'italic'), bg='black', fg='red')
        try:
            main.widgets["add_m20_B"] = {"name": "-20 Points (B)", "widget": btn_m_20_B,
                                         "x": main.widgets_placement["add_m20_B"]["x"],
                                         "y": main.widgets_placement["add_m20_B"]["y"]}
        except Exception as e:
            main.widgets["add_m20_B"] = {"name": "-20 Points (B)", "widget": btn_m_20_B,
                                         "x": 6 * self.screen_width / 10 + 300, "y": 7 * self.screen_height / 9 + 25}
        btn_m_20_B.place(x=main.widgets["add_m20_B"]["x"], y=main.widgets["add_m20_B"]["y"])

        SCORE["scoreA"] = int(self.scoreA["text"])
        SCORE["scoreB"] = int(self.scoreB["text"])

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
