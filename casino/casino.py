#!/usr/bin/python3.4
#-*-coding:Utf-8 -*

from random import randrange
from math 	import ceil

def color(nombre):
	if int(nombre)%2 == 0:
		return "noir"
	else :
		return "rouge"

argent = 200
print("\nBonjour à vous! Vous arrivez à la roulette avec " + str(argent) + "€. \n")

jouer_encore = True

while jouer_encore:
	nombre = 0
	mise = 0
	while (nombre < 1) | (nombre > 50):
		try:
			nombre = int(input("Sur quel nombre, souhaitez-vous miser ? "))
		except Exception:
			pass
		finally:	
			if (nombre < 1) | (nombre > 50):
				print("Merci d'entrer un nombre entre 1 et 50")
	while (mise < 1) | (mise > argent):
		try:
			mise = int(input("Combien souhaitez-vous misez sur le " + str(nombre) + " " + color(nombre) + " ? "))
			print("Mise : " + str(mise))
			print("Argent : " + str(argent))
		except Exception:
			pass
		finally:
			if (mise < 1) | (mise > argent):
				print("Merci d'entrer une mise positive et inférieure à votre argent total (" + str(argent) + "€).")

	argent -= mise

	roulette = randrange(0,49) + 1
	print("\nLes jeux sont faits! Vous avez misé " + str(mise) + " sur le " + str(nombre) + " " + color(nombre))

	print("La roulette tourne, ralenti, et s'arrête sur le " + str(roulette) + " " + color(roulette) + ".\n\n")

	gain = 0
	if nombre == roulette:
		gain = 3*mise
		print("La chance est avec vous! Vous avez gagné 3 fois votre mise soit " + str(gain) + "€! \n")
	elif nombre%2 == roulette%2:
		gain = ceil(0.5*mise)
		print("Félicitation! En misant sur la bonne couleur vous avez gagné la moitié de votre mise soit " + str(gain) + "€! \n")
	else:
		gain = -mise
		print("Dommage! Vous perdez votre mise de " + str(mise) + "€! \n")

	argent += mise + gain
	if argent <= 0:
		print("Vous avez tout perdu! À bientôt.")
		break

	print("Vous disposez maintenant de " + str(argent) + "€. ")

	if input("Souhaitez-vous continuer à jouer ? (o/n)").casefold() == "n":
		jouer_encore = False
