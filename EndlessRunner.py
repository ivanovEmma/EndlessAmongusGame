from http.client import GONE
from math import sqrt
from multiprocessing.managers import BaseProxy
from tkinter import *
from PIL import Image,ImageTk

# fonction de déplacement

InAir=False

def upP(event):
    global X,Y,BASE_Y,InAir
    touche = event.keysym
    if touche == 'Up':
        Y = BASE_Y - DEP
        Canevas.coords(rond,0 ,80)
        InAir = True


def down(event):
    global X,Y,BASE_Y,InAir
    touche = event.keysym
    # déplacement vers le haut
    if touche == 'Up':
        while(Y < BASE_Y):
            Y +=1
    Canevas.coords(rond,0 , 110)
    InAir = False


def obst():
    global X,Y,run, OX, OY, speed
    if run == True:
        run = contacte()
        print(contacte())
        OX = OX-(5*speed)
        #augmenter la rapidité de l'obstacle
        if(speed < 3):
            speed = speed*1.001
        elif(speed < 5):
            speed = speed*1.000001
        else:
            speed = speed * 1.0000001

        Canevas.coords(obstacle,OX, OY , OX + 20, OY + 20)

        if OX > -30:
        # mise à jour toutes les 50 ms
            run = contacte()
            fenetre.after(50,obst)


        else :
            OX = bOX
            run = contacte()
            fenetre.after(50,obst)
        run = contacte()





def contacte():
    global InAir
    if -10<OX<40 and InAir == False:
        rond = Canevas.create_image(0,0,anchor=NW,image=death)
        print("kkv",InAir)
        return False
    else:
        return True


def jeu():
    global run, speed
    run = True
    speed = 1.00
    obst()



# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("jeu amoguse")

# Création d'un widget Canvas
DEP = 70
TAILLE = 10
X = 5
BASE_Y = 150
Y = BASE_Y
bOX = X+320
OX = bOX
OY = BASE_Y
Canevas = Canvas(fenetre,width=300,height=200,bg ='cyan')
# Création d'un objet graphique
img = ImageTk.PhotoImage(Image.open("textures/walkingAnim/walk.png"))
death = ImageTk.PhotoImage(Image.open("textures/skulle.png"))
rond = Canevas.create_image(0,110,anchor=NW,image=img)

obstacle = Canevas.create_rectangle(5,5,TAILLE*2,TAILLE*2,fill='white')
terre = Canevas.create_rectangle(0,170,1000,1000,fill='yellow')
# La méthode bind() permet de lier un événement avec une fonction
Canevas.focus_set()
Canevas.bind('<KeyPress>',upP)
Canevas.bind('<KeyRelease>',down)
Canevas.pack(padx=10,pady=10,side=LEFT)
Button(fenetre,text=' Quitter' ,command=fenetre.destroy).pack(side=BOTTOM)
jeu()
fenetre.mainloop()
