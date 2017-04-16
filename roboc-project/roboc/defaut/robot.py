#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

class Robot:

	def __init__(self, nom = "C3PO"):
		self.nom = nom

	def __str__(self):
		return "Bonjour à vous, je m'appelle {0} et j'ai besoin de votre aide pour sortir du labyrinthe.".format(self.nom)

	def __repr__(self):
		return "<Robot"