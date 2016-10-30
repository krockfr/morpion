
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
				
			print
		

	#symbole : croix ou rond
	def jouer(self, symbole, ligne, colonne):
		print symbole
		success = True
		#test des paramètres
		import pdb; pdb.set_trace()
		if ((symbole != "rond" and symbole != "croix") or (ligne > 2 and ligne < 0) or (colonne > 2 and colonne < 0)):
			print "erreur"
			success = False
		else:
			print "OK"

			