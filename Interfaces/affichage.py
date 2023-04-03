from CDT.Simulation.arene import Arene
import math
import matplotlib.pyplot as plt
import random
from tkinter import *
class Affichage() :

    def __init__(self,arene):
        self.arene=arene
        self.fenetre=Tk()
        #self.fenetre.state('zoomed')
        self.acanvas= Canvas(self.fenetre,width = Arene.arene_longueur*3, height = Arene.arene_largeur*3 , bd=0, bg="white")
        self.acanvas.pack(padx=10,pady=10)
        self.liste_objet=[]
        self.liste_fleche=[]
    def clear(self):
        self.acanvas.delete(ALL)
        self.liste_objet=[]

    def updateAffichage(self,robot,obstacles):
        ray_r=robot.rayon_robot
        if len(self.liste_objet)>0:
            self.acanvas.delete(self.liste_objet[-1])
            self.liste_objet.pop()
        if len(self.liste_fleche)>0:
            self.acanvas.delete(self.liste_fleche[-1])
            self.liste_fleche.pop()
        self.acanvas.create_oval((robot.x + ray_r)*2.5, (robot.y + ray_r)*2.5,( robot.x - ray_r)*2.5, (robot.y - ray_r)*2.5, fill='black')
        self.liste_objet.append(self.acanvas.create_oval((robot.x + ray_r)*2.5, (robot.y + ray_r)*2.5,( robot.x - ray_r)*2.5, (robot.y - ray_r)*2.5, fill='red'))
        
        x1= robot.x *2.5
        y1 = robot.y *2.5
        x2 = x1 + ray_r *2.5 * math.cos(robot.orientation)
        y2 = y1 + ray_r *2.5 * math.sin(robot.orientation)
        self.liste_fleche.append(self.acanvas.create_line(x1,y1,x2,y2,arrow=LAST,fill='blue'))
        for o in obstacles:
            self.acanvas.create_oval((o.x + o.rayon)*2.5,(o.y + o.rayon)*2.5,(o.x - o.rayon)*2.5,( o.y - o.rayon)*2.5, fill='green')
        self.fenetre.update()
        
        #exercice 1 manipulation simple 
        #q1.1
    for x, y in [50, 50], [450, 50], [50, 450], [450, 450]:
        canvas.create_rectangle(x-20, y-20, x+20, y+20, fill="red")

# Dessiner le robot rond au milieu
    robot = canvas.create_oval(240, 240, 260, 260, fill="blue")

    #q1.2
        for o in obstacles:
            self.acanvas.create_oval((o.x + o.rayon)*2.5,(o.y + o.rayon)*2.5,(o.x - o.rayon)*2.5,( o.y - o.rayon)*2.5, fill='orange')
        self.fenetre.update()
        
         for o in obstacles:
            self.acanvas.create_oval((o.x + o.rayon)*2.5,(o.y + o.rayon)*2.5,(o.x - o.rayon)*2.5,( o.y - o.rayon)*2.5, fill='blue')
        self.fenetre.update()
    
    #2.3
    def dessiner(b):
        if self:
            robot.abaisser_crayon()
        else:
            robot.lever_crayon()
        return self.b
    #exercice 2 strategie avancé
    #2.1
# Dessiner le chiffre 1 à droite
    def dessiner_un(self):  # sourcery skip: remove-redundant-pass
        if dessiner(b)==True:
            acanvas.create_line(400, 100, 400, 400, width=20, fill="black")
            fenetre.update()
        else:
            pass
# Dessiner le chiffre 0 à gauche*
    def dessiner_zero(self):
        if dessiner(b)==True:
            canvas.create_oval(100, 100, 400, 400, width=20, outline="black")
            fenetre.update()  
            fenetre.after(1000)
        else :
            pass
# Fermer la fenêtre
    fenetre.destroy()




