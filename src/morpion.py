
# -*- coding=utf-8 -*-
from grille import Grille



def game():
    print " tic tac toe "

    maGrille = Grille() 



    while 1:
        print " "
        maGrille.afficher()
        print " "
        
        print " "
        print "joueur croix :"
        joueur_croix_ligne = input("ligne >> ")
        joueur_croix_colonne = input("colonne >> ")
        maGrille.jouer("croix", joueur_croix_ligne, joueur_croix_colonne)
        if maGrille.verifier_gagner() != "non":
            print "GAGNANT: " + maGrille.verifier_gagner()
            print " "
            maGrille.afficher()
            print " "
            break
        
        print " "
        maGrille.afficher()
        print " "
        
        print " "
        print "joueur rond :"
        joueur_rond_ligne = input("ligne >> ")
        joueur_rond_colonne = input("colonne >> ")
        maGrille.jouer("rond", joueur_rond_ligne, joueur_rond_colonne)
        if maGrille.verifier_gagner() != "non":
            print "GAGNANT: " + maGrille.verifier_gagner()
            print " "
            maGrille.afficher()
            print " "
            break
        
        print " "
        maGrille.afficher()
        print " "
        

if __name__ == '__main__':
    game()
