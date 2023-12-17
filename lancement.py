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
        bg = tk.PhotoImage(file='bg/bg1.png')
        bg_label = tk.Label(self.root, image=bg)
        bg_label.image = bg
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        logo_equipe_A = tk.PhotoImage(file='logos2D/' + self.equipeA.upper() + '.png')
        logo_A = tk.Label(image=logo_equipe_A)
        logo_A.image = logo_equipe_A
        logo_A.place(x=50, y=200)

        logo_equipe_B = tk.PhotoImage(file='logos2D/' + self.equipeB.upper() + '.png')
        logo_B = tk.Label(image=logo_equipe_B)
        logo_B.image = logo_equipe_B
        logo_B.place(x=850, y=200)
        bouton = tk.Button(self.root, text='Commencer le match', font=('calibri', '20', 'bold'), bg='white',
                           fg='#c59c1b',
                           command=lambda: self.lancer_le_match(None))
        bouton.place(x=520, y=500)

        self.sound()

    def lancer_le_match(self, event):
        self.root.destroy()
        mixer.music.stop()
        Main()

    def sound(self):
        mixer.init()
        mixer.music.load("sons/son3.mp3")
        mixer.music.set_volume(0.8)
        mixer.music.play()


if __name__ == '__main__':
    Debut()
