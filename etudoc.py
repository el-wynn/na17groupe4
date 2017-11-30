#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import cx_Oracle
import os
import sys

pathlocal = os.getcwd() + '/'

connection = cx_Oracle.connect("na17a013","txtAAC0I","sme-oracle.sme.utc/nf26")

print("Vous êtes un : \n 0- administrateur \n 1- un élève/prof ... (1)")
type=input()

while type<0 or type>1:
	print("L'utilisateur demandé n'exite pas, réessayez")
	type=input()

print(type)

if type == 0 : 
	print("Voici les différentes actions que vous pouvez réaliser : \n 0- archiver un document \n 1- ajouter une licence \n 2- ajouter une categorie\n 3-retirer un document de l'archive \n 4-quitter le mode administrateur \n entrez le numéro de l'action que vous souhaitez réaliser")
	action=input()
	while action > 4:
		print("L'action demandée n'existe pas réessayez")
		action=input()
	if action == 0 : 
		print("vous souhaitez archiver un document, voici la liste des documents qui ne sont pas encore archivés")

		cursor = connection.cursor()
		cursor.execute(""" SELECT titre FROM Documents WHERE archivedoc <> 'Y' """)
		i=0
		for doc in cursor:
			print("Document", i, "nom :", doc)
			i=i+1

	if action == 1 :
		print("Vous souhaitez ajouter un licence, voici les licences déjà existantes \n")
		cursor = connection.cursor()
 		cursor.execute("select * from licence")

		for row in cursor:
   			print(row)

		code=raw_input("donnez le nom de code de la licence que vous souhaitez insérer : ")
		des=raw_input("donnez la description de la licence : ")

		cursor = connection.cursor()
		add_cat=("INSERT INTO Licence(code, nom) VALUES( '" + code + "', '"+des+"')")

		cursor.execute(add_cat)

		
		cursor.close()
		connection.commit()

	if action == 2 :
		print("vous souhaitez ajouter une categorie \n")

		cursor = connection.cursor()
 		cursor.execute("select * from categorie")

		for row in cursor:
   			print(row)

		nom=raw_input("donnez le nom de la categorie que vous souhaitez insérer : ")


		cursor = connection.cursor()
		add_cat=("INSERT INTO Categorie(nom) VALUES( '" + nom + "')")

		cursor.execute(add_cat)

		
		cursor.close()
		connection.commit()

	if action == 3 :
		print("Vous souhaitez retirer un document de l'archive \n")

	if action == 4 : 
		exit()


if type == 1 :
	print("voici les différentes actions que vous pouvez réaliser : \n 0 - ajouter un document \n 1-rechercher un document \n 2-quitter le mode utilisateur")

	action=input()

	while action > 2:
		print("L'action demandée n'existe pas réessayez")
		action=input()
	if action == 0 : 
		print("Vous souhaitez ajouter un document")



	if action == 1 :
		print("Vous souhaitez rechercher un document \n")

	if action == 2 :
		exit()





