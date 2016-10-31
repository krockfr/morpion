
# -*- coding=utf-8 -*-


class Grille:

    def __init__(self):
        #|  0 |  0 |  0 | 
        #|  0 |  0 |  0 | 
        #|  0 |  0 |  0 | 
        self.grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


    def afficher(self):
        for ligne in xrange(0,3):
            print "| ",
            for colonne in xrange(0,3):
                print str(self.grille[ligne][colonne]) + " | ",
                
            print " "
        

    #symbole : croix ou rond
    def jouer(self, symbole, ligne, colonne):
        print symbole
        success = True
        #test des paramètres

        if ((symbole != "rond" and symbole != "croix") or (ligne > 2 or ligne < 0) or (colonne > 2 or colonne < 0)):
            print " "
            print "case prise => REJOUER"
            print " "
            success = False
        else:

            if (self.verifier_coup_jouer(ligne, colonne) == True):
                if (symbole == "rond"):
                    self.grille[ligne][colonne] = 'O'
                if (symbole == "croix"):
                    self.grille[ligne][colonne] = 'X'
            else:
                success = False
            
        return success
            
    
    def verifier_coup_jouer(self, ligne, colonne):
        success = True
        
        if (self.grille[ligne][colonne] != 0):
            success = False
            print " "
            print "case déjà prise"
            print " "
            
        return success
        
    def verifier_grille_pleine(self):
        success = True
        for ligne in xrange(0,3):
            for colonne in xrange(0,3):
                if (self.grille[ligne][colonne] == 0):
                    success = False
                    
        return success
        
    
    #retourne une string "rond" ou "croix" ou "non"
    def verifier_gagner(self):
        
        gagnant = "non"
        
        if self.grille[0][0] == "X" and self.grille[0][1] == "X" and self.grille[0][2] == "X":
            gagnant = "croix"
            
        if self.grille[1][0] == "X" and self.grille[1][1] == "X" and self.grille[1][2] == "X":
            gagnant = "croix"
            
        if self.grille[2][0] == "X" and self.grille[2][1] == "X" and self.grille[2][2] == "X":
            gagnant = "croix"
            
        if self.grille[0][0] == "X" and self.grille[1][0] == "X" and self.grille[2][0] == "X":
            gagnant = "croix"
            
        if self.grille[0][1] == "X" and self.grille[1][1] == "X" and self.grille[2][1] == "X":
            gagnant = "croix"
            
        if self.grille[0][2] == "X" and self.grille[1][2] == "X" and self.grille[2][2] == "X":
            gagnant = "croix"
            
        if self.grille[0][0] == "X" and self.grille[1][1] == "X" and self.grille[2][2] == "X":
            gagnant = "croix"
            
        if self.grille[0][2] == "X" and self.grille[0][1] == "X" and self.grille[2][0] == "X":
            gagnant = "croix"
        
        
        
        if self.grille[0][0] == "O" and self.grille[0][1] == "O" and self.grille[0][2] == "O":
            gagnant = ""
            
        if self.grille[1][0] == "O" and self.grille[1][1] == "O" and self.grille[1][2] == "O":
            gagnant = "rond"
            
        if self.grille[2][0] == "O" and self.grille[2][1] == "O" and self.grille[2][2] == "O":
            gagnant = "rond"
            
        if self.grille[0][0] == "O" and self.grille[1][0] == "O" and self.grille[2][0] == "O":
            gagnant = "rond"
            
        if self.grille[0][1] == "O" and self.grille[1][1] == "O" and self.grille[2][1] == "O":
            gagnant = "rond"
            
        if self.grille[0][2] == "O" and self.grille[1][2] == "O" and self.grille[2][2] == "O":
            gagnant = "rond"
            
        if self.grille[0][0] == "O" and self.grille[1][1] == "O" and self.grille[2][2] == "O":
            gagnant = "rond"
            
        if self.grille[0][2] == "O" and self.grille[0][1] == "O" and self.grille[2][0] == "O":
            gagnant = "rond"
        
        
        
        return gagnant
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            