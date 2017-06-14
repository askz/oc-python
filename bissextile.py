#!/usr/bin/python3.4
#-*-coding:Utf-8 -*

annee = int(input("Saisissez une année : "))

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
	print(annee, "est une année bissextile")
else:
	print(annee, "n'est pas une année bissextile")
