#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

"""L'objet Case"""

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
	"""L'objet Obstacle est la case par défaut qui ne peut être traversé"""
	def __init__(self, nom, symbole):
		super(Obstacle, self).__init__(nom, symbole, False, False)

class Obstacle(Case):
	"""L'objet Obstacle est la case par défaut qui ne peut être traversé"""
	def __init__(self, nom, symbole):
		super(Obstacle, self).__init__(nom, symbole, True, False)

class sortie(Case):
	"""L'objet Sortie est la case par défaut représentant la fin du labyrinthe"""
	def __init__(self, nom, symbole):
		super(Obstacle, self).__init__(nom, symbole, True, True)