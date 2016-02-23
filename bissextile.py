#!/usr/bin/python3.4
#-*-coding:Utf-8 -*

bissextile = False
annee = int(input("Saisissez une année : "))

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
	print(annee, "est un année bissextile")
else:
	print(annee, "n'est pas un année bissextile")