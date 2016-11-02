# -*- coding=utf-8 -*-
import pygame
from constantes import *
from pygame.locals import *
from grille import Grille


class Game:


    def __init__(self):
        self.continuer = True
        self.gagne = False
        self.grille = Grille()
        self.joueur_actif = "rond"

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
        self.croix = pygame.image.load(REP_ASSETS + ASSET_CROIX).convert_alpha()
        self.rond = pygame.image.load(REP_ASSETS + ASSET_ROND).convert_alpha()

    def modifie_joueur_actif(self):
        if self.grille.verifier_gagner() == "non":
            if self.joueur_actif == "croix":
                self.joueur_actif = "rond"
            elif self.joueur_actif == "rond":
                self.joueur_actif = "croix"
        else:
            self.gagne = True


    def gestion_evenements(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.continuer = False
            if event.type == KEYDOWN and self.gagne == False:
                if event.key == K_a:
                    print "touche a"
                    self.grille.jouer(self.joueur_actif, 0, 0)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_z:
                    print "touche z"
                    self.grille.jouer(self.joueur_actif, 0, 1)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_e:
                    print "touche e"
                    self.grille.jouer(self.joueur_actif, 0, 2)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_q:
                    print "touche q"
                    self.grille.jouer(self.joueur_actif, 1, 0)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_s:
                    print "touche s"
                    self.grille.jouer(self.joueur_actif, 1, 1)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_d:
                    print "touche d"
                    self.grille.jouer(self.joueur_actif, 1, 2)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_w:
                    print "touche w"
                    self.grille.jouer(self.joueur_actif, 2, 0)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_x:
                    print "touche x"
                    self.grille.jouer(self.joueur_actif, 2, 1)
                    self.modifie_joueur_actif()
                    self.grille.afficher()
                if event.key == K_c:
                    print "touche c"
                    self.grille.jouer(self.joueur_actif, 2, 2)
                    self.modifie_joueur_actif()
                    self.grille.afficher()

    def run(self):
        self.fenetre.blit(self.fond, (0, 0))
        self.gestion_evenements()



        for ligne in xrange(3):
            for colonne in xrange(3):
                if self.grille.grille[ligne][colonne] == "X":
                    self.fenetre.blit(self.croix, [colonne*200, ligne*200])
                if self.grille.grille[ligne][colonne] == "O":
                    self.fenetre.blit(self.rond, [colonne*200, ligne*200])

        if self.gagne == True:
            print self.grille.verifier_gagner()


        pygame.display.flip()






if __name__ == '__main__':
    partie = Game()