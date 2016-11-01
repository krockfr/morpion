# -*- coding=utf-8 -*-
import pygame
from constantes import *
from pygame.locals import *
from grille import Grille


class Game:


    def __init__(self):
        self.continuer = True
        self.grille = Grille()

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
        self.croix = pygame.image.load(REP_ASSETS + ASSET_CROIX).convert()
        self.rond = pygame.image.load(REP_ASSETS + ASSET_ROND).convert()

    def gestion_evenements(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.continuer = False
            if event.type == KEYDOWN:
                if event.key == K_a:
                    print "touche a"
                    self.grille.jouer("croix", 0, 0)
                    self.grille.afficher()
                if event.key == K_z:
                    print "touche z"
                    self.grille.jouer("croix", 0, 1)
                    self.grille.afficher()
                if event.key == K_e:
                    print "touche e"
                    self.grille.jouer("croix", 0, 2)
                    self.grille.afficher()
                if event.key == K_q:
                    print "touche q"
                    self.grille.jouer("croix", 1, 0)
                    self.grille.afficher()
                if event.key == K_s:
                    print "touche s"
                    self.grille.jouer("croix", 1, 1)
                    self.grille.afficher()
                if event.key == K_d:
                    print "touche d"
                    self.grille.jouer("croix", 1, 2)
                    self.grille.afficher()
                if event.key == K_w:
                    print "touche w"
                    self.grille.jouer("croix", 2, 0)
                    self.grille.afficher()
                if event.key == K_x:
                    print "touche x"
                    self.grille.jouer("croix", 2, 1)
                    self.grille.afficher()
                if event.key == K_c:
                    print "touche c"
                    self.grille.jouer("croix", 2, 2)
                    self.grille.afficher()

    def run(self):
        self.gestion_evenements()






if __name__ == '__main__':
    partie = Game()