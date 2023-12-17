import tkinter as tk
from pygame import mixer
from random import randint
import prematch
from main import Main


class Debut:
    def __init__(self):
        self.root = tk.Tk()
        self.equipeA = prematch.EQUIPE_A
        self.equipeB = prematch.EQUIPE_B
        self.root.title(self.equipeA.upper() + ' vs ' + self.equipeB.upper())
        self.root.geometry('1300x600+150+100')
        self.root.resizable(width=False, height=False)
        self.create_widgets()
        self.root.bind("<Return>", self.lancer_le_match)
        self.root.mainloop()

    def create_widgets(self):
        bg = tk.PhotoImage(file='bg/bg2.png')
        bg_label = tk.Label(self.root, image=bg)
        bg_label.image = bg
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        logo_equipe_A = tk.PhotoImage(file='logos/' + self.equipeA.lower() + '_1_3D.png')
        logo_A = tk.Label(image=logo_equipe_A)
        logo_A.image = logo_equipe_A
        logo_A.place(x=100, y=100)

        logo_equipe_B = tk.PhotoImage(file='logos/' + self.equipeB.lower() + '_2_3D.png')
        logo_B = tk.Label(image=logo_equipe_B)
        logo_B.image = logo_equipe_B
        logo_B.place(x=875, y=95)
        bouton = tk.Button(self.root, text='Entrez dans le Match', font=('calibri', '18', 'italic'), bg='#cc3638',
                           fg='white',
                           command=lambda: self.lancer_le_match(None))
        bouton.place(x=520, y=500)

        self.sound()

    def lancer_le_match(self, event):
        self.root.destroy()
        mixer.music.stop()
        Main()

    def sound(self):
        mixer.init()
        mixer.music.load("sons/son" + str(randint(2, 5)) + ".mp3")
        mixer.music.set_volume(0.4)
        mixer.music.play()


if __name__ == '__main__':
    Debut()
