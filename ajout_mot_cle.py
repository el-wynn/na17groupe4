#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import cx_Oracle as cx
connection = cx.connect("na17a013","txtAAC0I","sme-oracle.sme.utc/nf26")


def ajout_mot(mot_cle) :
	cursor = connection.cursor()
	cursor.execute("INSERT INTO MotCle(mot_cle) VALUES('"+mot_cle+"')")
	cursor.close()
        connection.commit()
	print("ajout réussi")

mot=raw_input("mot-clé :")
ajout_mot(mot)
