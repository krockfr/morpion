
# -*- coding=utf-8 -*-
import sys
from grille import Grille



def game():
	print "morpion"

	maGrille = Grille() 
	maGrille.afficher()
	maGrille.jouer("rond", 0, 3)





if __name__ == '__main__':
	game()
