#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from carte import Carte

# On charge les cartes existantes
cartes = []
carte = {}
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-3].lower()
		with open(chemin, "r") as fichier:
			chaine = fichier.read()
			x = 0
			y = 0
			for caractere in chaine:
				if caractere == "\n":
					y += 1
					x = 0
					continue
				elif caractere == "\r":
					continue
				elif caractere == "O":
					obstacle = "Mur"
				elif caractere == ".":
					obstacle = "Porte"
				elif caractere == "U":
					obstacle = "Sortie"
				else:
					pass
				carte[x, y] = obstacle
				print("(" + str(y) + ":" + str(x) + ") => " + obstacle)
				x += 1
		
			# Création d'une carte, à compléter
			# carte = Carte(nom_carte, contenu)
			# cartes.append(carte)
			# print(nom_carte)
			# print(carte)
# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
	print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...