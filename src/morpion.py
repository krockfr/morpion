# -*- coding=utf-8 -*-
import pygame
from constantes import *
from pygame.locals import *
from grille import Grille


class Game:


    def __init__(self):
        self.continuer = True


        print "Nouvelle partie"
        self.creer_fenetre()
        self.load_assets()

        self.fenetre.blit(self.fond, (0, 0))

        pygame.display.flip()


        while self.continuer:
            self.run()


    def creer_fenetre(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((600, 600))

    def load_assets(self):
        self.fond = pygame.image.load(REP_ASSETS + ASSET_BACKGROUND).convert()

    def run(self):
        print "jeux"





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
    partie = Game()