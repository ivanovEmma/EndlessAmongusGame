from http.client import GONE
from multiprocessing.managers import BaseProxy
from tkinter import *

# fonction de déplacement

def upP(event):
    global X,Y,BASE_Y
    touche = event.keysym
    if touche == 'Up':
        Y = BASE_Y - DEP
    Canevas.coords(rond,X , Y , X + 20, Y + 20)
    
def down(event):
    global X,Y,BASE_Y
    touche = event.keysym
    # déplacement vers le haut
    if touche == 'Up':
        while(Y < BASE_Y):
            Y +=1
    Canevas.coords(rond,X , Y , X + 20, Y + 20)
    

def obst():
    global X,Y,run, OX, OY
    if run == True:
        OX = OX-3
        Canevas.coords(obstacle,OX, OY , OX + 20, OY + 20)

        if OX > -30:
        # mise à jour toutes les 50 ms
            fenetre.after(50,obst)
            print(OX)
        else :
            OX = bOX
            fenetre.after(50,obst)
            print(OX)
        
            
def contacte():
    global X,Y
    

def jeu():
    global run
    run = True
    obst()
    
    
    
# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Déplacement clavier")

# Création d'un widget Canvas
DEP = 40
TAILLE = 10
X = 5
BASE_Y = 150
Y = BASE_Y
bOX = X+320
OX = bOX
OY = BASE_Y
Canevas = Canvas(fenetre,width=300,height=200,bg ='cyan')
# Création d'un objet graphique
rond = Canevas.create_oval(5,5,TAILLE*2,TAILLE*2,fill='red')
obstacle = Canevas.create_oval(5,5,TAILLE*2,TAILLE*2,fill='white')
terre = Canevas.create_rectangle(0,170,1000,1000,fill='yellow')
# La méthode bind() permet de lier un événement avec une fonction
Canevas.focus_set()
Canevas.bind('<KeyPress>',upP)
Canevas.bind('<KeyRelease>',down)
Canevas.pack(padx=10,pady=10,side=LEFT)
Button(fenetre,text=' Quitter' ,command=fenetre.destroy).pack(side=BOTTOM)
jeu()
fenetre.mainloop()