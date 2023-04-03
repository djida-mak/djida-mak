 #exercice 1 manipulation simple 
    #1.1
    for x, y in [50, 50], [450, 50], [50, 450], [450, 450]:
        canvas.create_rectangle(x-20, y-20, x+20, y+20, fill="red")

# Dessiner le robot rond au milieu
    robot = canvas.create_oval(240, 240, 260, 260, fill="blue")

    #1.2
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
        
    #2.3
    def dessiner_zero_un():
        string = "01"
        x=50;
        y=50;
        for char in string:
            if char == "0":
                canvas.create_oval(x, y, x+100, y+100, outline="black")
            elif char == "1":
                canvas.create_line(x+50, y, x+50, y+100, width=10, fill="black")
            x += 150
    
    #2.4
# Fermer la fenêtre
    fenetre.destroy()
    #2.5
    def dessiner_chaine(chaine):
        for c in chaine:
            if c == '1':
                dessiner_un()
        elif c=='0':
                dessiner_zero()
            
        
    
