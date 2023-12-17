import tkinter as tk
from random import randint

fenetre_principal = tk.Tk()

# recherche de la taille de l'ecran
screen_width = fenetre_principal.winfo_screenwidth()
screen_height = fenetre_principal.winfo_screenheight()

fenetre_principal.geometry(str(screen_width) + "x" + str(screen_height))


#ajout des widgets

#print(self.equipeA_name + '.png')
fenetre_principal.resizable(width = False , height = False)
#ajoutons un bg image
#bg = tk.PhotoImage(file = 'bg' + str(randint(1,9)) +'.png')
#bg_label = tk.Label(image = bg )
#bg_label.place(x= 0 , y = 0 ,relwidth = 1 , relheight = 1)

logo_equipe_A = tk.PhotoImage( file = 'tc1.png')

logo_A = tk.Label(image = logo_equipe_A)
logo_A.image = logo_equipe_A
logo_A.grid(sticky = tk.W , padx = screen_width/10  , pady = screen_height/9 , row = 0 )
logo_equipe_B = tk.PhotoImage( file = 'tc2.png')
logo_B = tk.Label(image = logo_equipe_B)
logo_B.image = logo_equipe_B
logo_B.grid(sticky = tk.W , padx = 7*screen_width/10 , row = 0 )




# ajoutons le label score text
score_title = tk.Label(fenetre_principal , text = 'Score' , font = ('algerian' , 50 , 'bold' , 'underline'))
score_title.place(x = 4*screen_width/10 + 60 , y = 4*screen_height/9 - 50)

# score pour equipeA
scoreA = tk.Label(fenetre_principal , text = score , font = ('Book antiqua' , 100 , 'bold' , 'underline'), bg = 'green', fg = 'white')
scoreA.place(x = 3*screen_width/10 - 60 , y = 5*screen_height/9 + 50)
# score pour equipeB text
scoreB = tk.Label(fenetre_principal , text = '90' , font = ('Book antiqua' , 100 , 'bold' , 'underline') , bg = 'green', fg = 'white')
scoreB.place(x = 6*screen_width/10 , y = 5*screen_height/9 + 50)

# entrey non apparent
score_for_a = tk.Entry(fenetre_principal)
score_for_a.insert(0 , 0)
# label frame pour equipe 1
grandlabel = tk.LabelFrame( fenetre_principal,text = "JOUEURS", font = ('cambria' , 40 , 'bold'))
grandlabel.grid(row = 2 , sticky = tk.W , padx = screen_width/10  , pady = 0 )
tk.Label(grandlabel,text = 'Joueurs 1' , font = ('verdana',28,'italic' )).grid(row = 2)
tk.Label(grandlabel,text = 'Joueurs 2' , font = ('verdana',28 ,'italic')).grid(row = 3)
tk.Label(grandlabel,text = 'Joueurs 3' , font = ('verdana',28 ,'italic')).grid(row = 4)
tk.Label(grandlabel,text = 'Joueurs 4' , font = ('verdana',28 ,'italic')).grid(row = 5)
tk.Label(grandlabel,text = 'Joueurs 5' , font = ('verdana',28 ,'italic')).grid(row = 6)

# label frame pour equipe 2
grandlabel_2 = tk.LabelFrame(fenetre_principal,text = "JOUEURS", font = ('cambria' , 40 , 'bold'))
grandlabel_2.grid(row = 2 , sticky = tk.W , padx = 7*screen_width/10 + 80 , pady = 0 )
tk.Label(grandlabel_2,text = 'Joueurs 1' , font = ('verdana',28,'italic' )).grid(row = 2)
tk.Label(grandlabel_2,text = 'Joueurs 2' , font = ('verdana',28 ,'italic')).grid(row = 3)
tk.Label(grandlabel_2,text = 'Joueurs 3' , font = ('verdana',28 ,'italic')).grid(row = 4)
tk.Label(grandlabel_2,text = 'Joueurs 4' , font = ('verdana',28 ,'italic')).grid(row = 5)
tk.Label(grandlabel_2,text = 'Joueurs 5' , font = ('verdana',28 ,'italic')).grid(row = 6)

ajouter = tk.Button(text= 'ajouter des score a A' , command = ajout_a_10)
ajouter.place( x =screen_width/10 )

# ajouter des point a equipe A

# fonction dajout de score

def ajout_a_10():
	valeur = score_for_a.get()
	valeur = valeur  + 10
	score_for_a.insert(valeur)


# j'utilise ceci pour creer des trait de liaison
"""
zone_dessin = tk.Canvas(fenetre_principal,width=50,height=50)
zone_dessin.grid(row = 1)
zone_dessin.create_line(26,28,40,30, fill="black",width=2)
"""
# ajoutons le label score


fenetre_principal.mainloop()