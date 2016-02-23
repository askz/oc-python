#!/usr/bin/python3.4
#-*-coding:Utf-8 -*

bissextile = False
annee = int(input("Saisissez une année : "))

if annee % 400 == 0:
	bissextile = True
elif annee % 100 == 0:
	bissextile = False
elif annee % 4 == 0:
	bissextile = True
else:
	bissextile = False

if bissextile == True:
	print(annee, "est un année bissextile")
else:
	print(annee, "n'est pas un année bissextile")