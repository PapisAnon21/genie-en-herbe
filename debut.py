import tkinter as tk
from teams import Teams
from pygame import mixer
from random import randint
from main import Main


class Debut:
    def __init__(self):
        self.root = tk.Tk()
        self.teams = Teams(self.root)
        self.equipeA_name = self.teams.champA.get()
        self.equipeB_name = self.teams.champB.get()
        self.root.title(self.equipeA_name.upper() + ' vs ' + self.equipeB_name.upper())
        self.root.geometry('1300x600')
        self.root.resizable(width=False, height=False)
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # print(self.equipeA_name + '.png')
        # ajoutons un bg image   file = 'bg' + str(randint(1,9)) +'.png'
        bg = tk.PhotoImage(file='bg/'+ 'bg' + str(randint(1,9)) +'.png')
        bg_label = tk.Label(image = bg)
        bg_label.image = bg
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # ici on ajoute un gif

        logo_equipe_A = tk.PhotoImage(file='logos/' + self.equipeA_name.lower() + '_1_3D.png')
        logo_A = tk.Label(image=logo_equipe_A)
        logo_A.image = logo_equipe_A
        logo_A.place(x=100, y=100)

        logo_equipe_B = tk.PhotoImage(file='logos/' + self.equipeB_name.lower() + '_2_3D.png')
        logo_B = tk.Label(image=logo_equipe_B)
        logo_B.image = logo_equipe_B
        logo_B.place(x=875, y=95)
        bouton = tk.Button(text='Entrez dans le Match', font=('calibri', '18', 'italic'), bg='#cc3638', fg='white',
                           command=self.lancer_le_match)
        bouton.place(x=520, y=500)
        self.sound()

    def lancer_le_match(self):
        self.root.destroy()
        Main()

    def sound(self):
        mixer.init()
        mixer.music.load("sons/son" + str(randint(2, 5)) + ".mp3")
        mixer.music.set_volume(0.4)
        mixer.music.play()