from http.client import GONE
from math import sqrt
from multiprocessing.managers import BaseProxy
from tkinter import *
from PIL import Image,ImageTk
import datetime
import threading


# fonction de déplacement

InAir=False

s = 1

def chrono():
    global s, run, score_var
    if run==True:
        fenetre.after(1000,chrono)
        s=s+1
        score_var.set(f"Score: {s}")

#Fonction upP: Lorsque la touche "Up" est appuyée, le personnage saute et retombe après 1 seconde
def upP(event):
    global X,Y,BASE_Y,InAir
    touche = event.keysym
    if touche == 'Up':
        Y = BASE_Y - DEP
        Canevas.coords(rond,0 ,80)
        InAir = True
        Canevas.after(1000, down)
        
#Fonction down(): Lorsque le button "Up" est relachée, le personnage tombe par terre
def down():
    global X,Y,BASE_Y,InAir
    while(Y < BASE_Y):
        Y +=1
    Canevas.coords(rond,0 , 110)
    InAir = False

#Fonction obst(): controlle l'obstacle
c = 0
def obst():
    global X,Y,run, OX, OY, speed,c
    
    if run == True:
        run = contacte()
        #print(contacte())
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
            #change la couleur de l'obstacle
            c = c + 1
            if(c%3 == 0):
                Canevas.itemconfig(obstacle, fill='white')
            elif(c%3 == 1):
                Canevas.itemconfig(obstacle, fill='red')
            elif(c%3 == 2):
                Canevas.itemconfig(obstacle, fill='blue')
            OX = bOX
            run = contacte()
            fenetre.after(50,obst)
        run = contacte()




#Fonction contacte - vérifie si il y a un contacte entre obstacle et personnage
def contacte():
    global InAir
    if -10<OX<40 and InAir == False:
        rond = Canevas.create_image(0,0,anchor=NW,image= death)
        print("kkv",InAir)
        return False
    else:
        return True

#Fonction jeu: contrôle le jeu
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
OY = BASE_Y - 20
Canevas = Canvas(fenetre,width=300,height=200,bg ='black')
# Création d'un objet graphique
img = ImageTk.PhotoImage(Image.open("textures/walkingAnim/walk.png"))
death = ImageTk.PhotoImage(Image.open("textures/dead.png"))
rond = Canevas.create_image(0,110,anchor=NW,image=img)

obstacle = Canevas.create_rectangle(5,5,TAILLE*2,TAILLE*2,fill='white')
terre = Canevas.create_rectangle(0,150,1000,1000,fill='white')
# La méthode bind() permet de lier un événement avec une fonction
Canevas.focus_set()
Canevas.bind('<KeyPress>',upP)
Canevas.pack(padx=10,pady=10,side=LEFT)
Button(fenetre,text=' Quitter' ,command=fenetre.destroy).pack(side=BOTTOM)

# Score display
score_var = StringVar()
score_var.set("Score: 0")
score_label = Label(fenetre, textvariable=score_var)
score_label.pack(side=RIGHT)

jeu()
chrono()
fenetre.mainloop()
