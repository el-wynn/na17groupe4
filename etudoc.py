#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import cx_Oracle
import os
import sys

pathlocal = os.getcwd() + '/'

connection = cx_Oracle.connect("na17a013","txtAAC0I","sme-oracle.sme.utc/nf26")

def archive_doc() :
	print("vous souhaitez archiver un document, voici la liste des documents qui ne sont pas encore archivés")

	cursor = connection.cursor()
	cursor.execute(""" SELECT iddoc, titre FROM Documents WHERE archivedoc <> 'Y' """)
	for row in cursor:
		print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))
	print("Selectionnez le document que vous souhaitez archiver")
	doc=input()

	cursor.execute("UPDATE Documents SET archivedoc='Y' WHERE iddoc = :idoc", idoc=doc)

	cursor.close()
	connection.commit()

def ajout_licence() : 
	print("Vous souhaitez ajouter un licence, voici les licences déjà existantes \n")
	cursor = connection.cursor()
	cursor.execute("select * from licence")
	for row in cursor:
		print(row)

	code=raw_input("donnez le nom de code de la licence que vous souhaitez insérer : ")
	des=raw_input("donnez la description de la licence : ")

	cursor = connection.cursor()
	add_licence=("INSERT INTO Licence(code, nom) VALUES( '" + code + "', '"+des+"')")

	try : 
		cursor.execute(add_licence)

	except  cx_Oracle.DatabaseError as exc:
		error, = exc.args
		if error.code == 1:
 			print("L'élement existe déjà dans la base de données")
			exit()
	finally : 
		cursor.close()
	print("L'insertion à été réalisée correctement")
	connection.commit()


def ajout_categorie() :
	print("vous souhaitez ajouter une categorie \n")

	cursor = connection.cursor()
 	cursor.execute("select * from categorie")

	for row in cursor:
		print(row)
	nom=raw_input("donnez le nom de la categorie que vous souhaitez insérer : ")

	cursor = connection.cursor()
	add_cat=("INSERT INTO Categorie(nom) VALUES( '" + nom + "')")

	try : 
		cursor.execute(add_cat)

	except  cx_Oracle.DatabaseError as exc:
 		error, = exc.args
    		if error.code == 1:
    			print("L'élement existe déjà dans la base de données")
			exit()
	finally : 
		cursor.close()
	print("L'insertion à été réalisée correctement")
	connection.commit()

def retour_archive() : 
	print("Vous souhaitez retirer un document de l'archive \n")

	cursor = connection.cursor()
	cursor.execute(""" SELECT iddoc, titre FROM Documents WHERE archivedoc <> 'N' """)
	for row in cursor:
		print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))

	print("Selectionnez le document que vous souhaitez archiver")
	doc=input()

	cursor.execute("UPDATE Documents SET archivedoc='N' WHERE iddoc = :idoc", idoc=doc)

	cursor.close()
	connection.commit()


def menu_personne() :
	print("Vous êtes un : \n 0- administrateur \n 1- un élève/prof ... \n 2-vous voulez quitter")
	type=input()
	while type<0 or type>2:
		print("L'utilisateur demandé n'exite pas, réessayez")
		type=input()

	return type

def menu_admin() : 
	print("Voici les différentes actions que vous pouvez réaliser : \n 0- archiver un document \n 1- ajouter une licence \n 2- ajouter une categorie\n 3-retirer un document de l'archive \n 4-quitter le mode administrateur \n entrez le numéro de l'action que vous souhaitez réaliser")
	action=input()
	return action

def menu_eleve() : 
	print("voici les différentes actions que vous pouvez réaliser : \n 0 - ajouter un document \n 1-rechercher un document \n 2-quitter le mode utilisateur")

	action=input()

	while action > 2:
		print("L'action demandée n'existe pas réessayez")
		action=input()

	return action
etat = 1

while etat == 1 : 
	type=menu_personne()
	etat = 2
	while etat == 2 : 

		if type == 0 : 
			action=menu_admin()

			#l'action demandée n'existe pas
			while action > 4:
				print("L'action demandée n'existe pas réessayez")
				action=menu_admin

			#archive d'un document
			if action == 0 : 
				archive_doc()
		
			#ajouter une licence
			if action == 1 :
				ajout_licenc()
			#ajouter une categorie
			if action == 2 :
				ajout_categorie()
			#enlever un document de l'archive
			if action == 3 :
				retour_archive()
	
			if action == 4 : 
				etat = 1
		


		if type == 1 :
			action=menu_eleve()
			if action == 0 : 
				print("Vous souhaitez ajouter un document")
		

#A FAIRE

			if action == 1 :
				print("Vous souhaitez rechercher un document \n")
				while action<3 :
					print("Vous souhaitez faire une recherche par : \n 0-categorie \n 1- mot clé \n 2 - nom de l'auteur \n 3 - semestre \n 4 - retour au menu élève")
					recherche = input()
					if recherche == 0 :
						cursor = connection.cursor()
						cursor.execute("select * from categorie")

						i=0
						for row in cursor:
							print("numéro : ", i, " Categorie:", row)
							i=i+1
						print("Selectionnez le numéro de la categorie dans laquelle vous souhaitez rechercher un document")
						cat=input()
					if recherche == 1:
					#recherche par mot clé
						exit()

					if recherche == 2 : 
					#recherche par auteur		
						exit()


					if recherche == 3 : 
					#recherche par semestre
						saison = raw_input('Entrez la saison (P ou A) : ')
						annee=raw_input("entrez l'année (ex : 2017) : ")

						sel_semestre=("SELECT nom FROM Documents d WHERE d.semestredoc.saison='"+saison+"' AND d.semestredoc.annee='" +annee+ "')")

						cursor = connection.cursor()
						cursor.execute(sel_semestre)
					
						for row in cursor:
	   						print(row)
				
				
					if recherche == 4 :
						etat = 2
						type =1
		



			if action == 2 :
				etat=1
	
	
		if type == 2 :
			exit()



