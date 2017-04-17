#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

"""L'objet Case représente les éléments constitutifs des cartes.
Les trois cases par défaut sont l'Obstacle qui empêche le mouvement, le Passage qui permet de le mouvement et la Sortie qui représente la fin du labyrinthe et la victoire."""

class Case():

	def __init__(self, nom, symbole, traversable, sortie):
		self.nom = nom
		self.symbole = symbole
		self.traversable = traversable
		self.sortie = sortie

	def __str__(self):
		str_traversable = ""
		if self.traversable:
			str_traversable = "non "
		return self.nom + " est une case " + str_traversable + "traversable symbolisée par le caratère " + self.symbole

class Obstacle(Case):
	"""L'objet Obstacle est la case par défaut qui ne peut être traversée"""
	def __init__(self, nom, symbole):
		super(Obstacle, self).__init__(nom, symbole, False, False)

class Passage(Case):
	"""L'objet Passage est la case par défaut qui peut être traversée"""
	def __init__(self, nom, symbole):
		super(Obstacle, self).__init__(nom, symbole, True, False)

class Sortie(Case):
	"""L'objet Sortie est la case par défaut représentant la fin du labyrinthe"""
	def __init__(self, nom, symbole):
		super(Obstacle, self).__init__(nom, symbole, True, True)