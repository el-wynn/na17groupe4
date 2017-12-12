#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import cx_Oracle as cx
connection = cx.connect("na17a015", "7iNpUoSO", "sme-oracle.sme.utc/nf26")


def recherche_etu() :
	cursor = connection.cursor()

	nom =raw_input("Quel est le nom de l'étudiant que vous recherchez ? : ")
	cursor.execute("SELECT COUNT (*) FROM (SELECT nom, prenom, login FROM Etudiant WHERE nom = '"+nom+"' )")
	count = cursor.fetchall()[0][0]
	if count == 0 :
		#on cherche par le nom, vu qu'on ne connaît pas de base le login des gens
		print ("Pas d'etudiant ayant ce nom.")
		cursor.close()
		return 0
	else :
		cursor=connection.cursor()
		cursor.execute("SELECT * FROM Etudiant WHERE nom = '"+nom+"'")
		for row in cursor :
			print("on est là 2")
			print("login : {:20s} nom: {:20s} prenom: {:50s}".format(row[0], row[1], row[2]))
			#Quand le nom est bon on cherche à récupérer le login (la clé) + cas des homonymes
			etu =raw_input("Tapez le login de l'etudiant qui vous interesse : ")
			cursor.execute("SELECT * FROM Etudiant WHERE login = '" +etu+ "'")
			#on vérifie que le nom tapé est bien dans la base
			count = cursor.fetchall()[0][0]
			if count == 0 :
				print ("Mauvais login")
				return 0
			else :

				return etu

def recherche_par_etu() :
	cursor = connection.cursor()
	etu = recherche_etu()
	if etu != 0 :
		cursor.execute("SELECT COUNT (*) FROM (SELECT d.iddoc, d.titre FROM Documents d, TABLE(d.auteur) au WHERE au.Etudiant.login ='"+etu+"' AND d.archivedoc <> 'Y')")
		count = cursor.fetchall()[0][0]
		
		if count > 0 :
			cursor=connection.cursor()
			cursor.execute("SELECT d.iddoc, d.titre FROM Documents d WHERE d.auteur.login ='"+etu+"' AND d.archivedoc <> 'Y'")
			for row in cursor:
				print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))
			
		else :
			print("pas de documents à afficher")
		info_doc()





recherche_par_etu()
