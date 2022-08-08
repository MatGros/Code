# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:35:07 2022

@author: ENFANTS
"""

# Declacaration classe poney
class Poney:
    
    # Constructeur de poney
    def __init__ (self, nom, sexe, couleur, taille, poids):
        self.nom = nom
        self.sexe = sexe
        self.couleur = couleur
        self.taille = taille
        self.poids = poids
        
    def Peser (self):
        print("Je suis", self.nom,"et je pèse :", self.poids,"Kg")

    def Manger (self, nourriture):    
        # self.nourriture = nourriture
        # self.poids = self.poids + 1
        if nourriture == "foin" :
            self.poids = self.poids + 1
            print("Miam c'est bon la/le :", nourriture)
        elif nourriture == "bonbon" :
            self.poids = self.poids + 3
            print("C'est trop bon la/le :", nourriture)
        else:
            print("Ce n'est pas bon la/le :", nourriture) 
 
                
    
    def Marcher (self):
        print("Je marche tranquilou")
        self.poids = self.poids - 1
        
        
    

p1 = Poney("SPIROU","MALE","Alzan",110,700);
p2 = Poney("BRINDILLE","FEMMELLE","Pie Alzan",120,750);

# print("nom du poney 1 ", p1.nom)
# print("nom du poney 2 ", p2.nom)

p1.Peser()
p2.Peser()

p1.Manger('foin')
p1.Manger('pierre')
p1.Manger('bonbon')

p1.Peser()

p1.Marcher()

p1.Peser()

p2.Manger('foin')
p2.Peser()