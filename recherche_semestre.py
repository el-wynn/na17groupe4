#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from datetime import date

import cx_Oracle
import os
import sys
import time
import datetime

pathlocal = os.getcwd() + '/'

connection = cx_Oracle.connect("na17a013","txtAAC0I","sme-oracle.sme.utc/nf26")


#fonction de recherche par semestre
def recherche_semestre() :
	saison = raw_input('Entrez la saison (P ou A) : ')
	annee = raw_input("Entrez l'année (ex : 2017) : ")

	#On vérifie que le semestre entré est bien valide
	today = date.today()
	print(today.year)
	if saison != 'P' and saison != 'A' :
		print("Saison incorrecte.")
	#elif annee < 1972 or annee >= today.year :
	#	print ("Année incorrecte.")

	#Et s'il est valide on execute le select dans la BD
	#gérer doc non archivés
	else :
		cursor = connection.cursor()
		cursor.execute("SELECT COUNT (*) FROM( SELECT d.iddoc, d.titre FROM Documents d WHERE d.semestredoc.saison='"+saison+"' AND d.semestredoc.annee='"+annee+"' AND d.archivedoc <> 'Y') ")
		count = cursor.fetchall()[0][0]
		print(count)
		if count == 0 :
			print("Il n'y a pas de documents à afficher")


		else :
			cursor.execute("SELECT d.iddoc, d.titre FROM Documents d WHERE d.semestredoc.saison ='"+saison+"' AND d.semestredoc.annee ='"+annee+"' AND d.archivedoc <> 'Y'")
			for row in cursor:
				print(row)
        
			info_doc()

		cursor.close()


recherche_semestre()
