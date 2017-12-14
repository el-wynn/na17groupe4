#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import cx_Oracle
import os
import sys
import time
import datetime

pathlocal = os.getcwd() + '/'

connection = cx_Oracle.connect("na17a013","txtAAC0I","sme-oracle.sme.utc/nf26")


#fonction pour archiver un document
def archive_doc() :
        print("Vous souhaitez archiver un document, voici la liste des documents qui ne sont pas encore archivés")

        cursor = connection.cursor()
        cursor.execute("""SELECT COUNT (*) FROM( SELECT iddoc, titre FROM Documents WHERE archivedoc <> 'Y') """)
        count = cursor.fetchall()[0][0]
        if count == 0 :
                print("Il n'y a pas de documents à afficher")
                return 0
        else :
                cursor = connection.cursor()
                cursor.execute(""" SELECT iddoc, titre FROM Documents WHERE archivedoc <> 'Y' """)
                for row in cursor:
                        print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))
                print("Selectionnez le document que vous souhaitez archiver")
                doc=input()

                cursor.execute("UPDATE Documents SET archivedoc='Y' WHERE iddoc = :idoc", idoc=doc)

                cursor.close()
                connection.commit()

#fonction pour ajouter une licence

def ajout_licence() :
        print("Vous souhaitez ajouter un licence, voici les licences déjà existantes \n")
        cursor = connection.cursor()
        cursor.execute("select * from licence")
        for row in cursor:
                print(row)

        code=raw_input("Donnez le nom de code de la licence que vous souhaitez insérer : ")
        des=raw_input("Donnez la description de la licence : ")

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


#fonction pour ajouter une catégorie

def ajout_categorie() :
        print("Vous souhaitez ajouter une categorie \n")

        cursor = connection.cursor()
        cursor.execute("select * from categorie")

        for row in cursor:
                print(row)
        nom=raw_input("Donnez le nom de la categorie que vous souhaitez insérer : ")

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


#fonction pour enlever un document de l'archive

def retour_archive() :
        print("Vous souhaitez retirer un document de l'archive \n")

        cursor = connection.cursor()
        cursor.execute("""SELECT COUNT (*) FROM( SELECT iddoc, titre FROM Documents WHERE archivedoc <> 'N') """)
        count = cursor.fetchall()[0][0]
        if count > 0 :
                cursor=connection.cursor()
                cursor.execute(""" SELECT iddoc, titre FROM Documents WHERE archivedoc <> 'N' """)
                for row in cursor:
                        print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))

                print("Selectionnez le document que vous souhaitez archiver")
                doc=input()

                cursor.execute("UPDATE Documents SET archivedoc='N' WHERE iddoc = :idoc", idoc=doc)

                cursor.close()
                connection.commit()
        else :
                print("Il n'y a pas encore de documents archivés")


#fonction pour imprimer les informations sur un document
def info_doc() :
        print("Selectionnez l'id du documents sur lequel vous souhaitez obtenir plus d'informations")
        doc=input()
        cursor = connection.cursor()
        cursor.execute("SELECT d.iddoc FROM Documents d WHERE d.iddoc= :idoc ", idoc=doc)

        for row in cursor:
                print("id :" ,row)

        cursor.execute("SELECT d.titre FROM Documents d WHERE d.iddoc= :idoc ", idoc=doc)

        for row in cursor:
                print("titre :" ,row)

        cursor.execute("SELECT date_pb FROM Documents d WHERE d.iddoc= :idoc ", idoc=doc)

        for row in cursor:
                print("date de publication :" ,row)

        cursor.execute("SELECT description FROM Documents d WHERE d.iddoc= :idoc ", idoc=doc)

        for row in cursor:
                print("description :" ,row)

        cursor.execute("SELECT aut.Etudiant.nom, aut.Etudiant.prenom FROM Documents d, TABLE(d.auteur) aut WHERE d.iddoc=:idoc ", idoc=doc)

        for row in cursor:
                print("nom de l'auteur : {:50} prénom de l'auteur : {:50}" .format(row[0], row[1]))

        cursor.execute("SELECT ens.Enseignant.nom, ens.Enseignant.prenom FROM Documents d, TABLE(d.professeur) ens WHERE d.iddoc=:idoc ", idoc=doc)

        for row in cursor:
                print("nom de l'enseignant : {:50} prénom de l'enseignant ; {:50}" .format(row[0], row[1]))

        cursor.execute("SELECT l.Licence.nom FROM Documents d, TABLE(d.licencedoc) l WHERE d.iddoc=:idoc ", idoc=doc)

        for row in cursor:
                print("licence : {:50} " .format(row[0]))

        cursor.execute("SELECT m.refMotCle.mot_cle FROM Documents d, TABLE(d.motCle) m WHERE d.iddoc=:idoc ", idoc=doc)
        print("mots-clé associés : ")
        for row in cursor:
                print(" {:50} " .format(row[0]))


#fonction pour ajouter un document
def ajout_doc() :
    print("Vous souhaitez ajouter un document \n")
    cursor = connection.cursor()
    #l'id du nouveau document sera l'id max des documents actuel +1
    cursor.execute("SELECT MAX(d.iddoc) FROM Documents d")
    for row in cursor:
            iddoc=int(row[0])+1
    titre=raw_input("Donnez le titre de votre document : ")
    date_pb=datetime.date.today()
    description=raw_input("Donnez la description de votre document : ")
    #Semestre
    while True:
            saison=raw_input("Donnez la saison (P ou A) : ")
            if (saison == 'P') | (saison == 'A') :
                    try :
                            annee=int(raw_input("Donnez l'année (ex : 2017) :"))
                            if (isinstance(annee,int)) &(annee > 1900) & (annee < 2050) :
                                    break
                    except ValueError:
                            annee = 0
    #Categorie
    tab = []
    print("Categories disponibles : ");
    cursor.execute("SELECT * FROM Categorie")
    for row in cursor:
            print(row[0])
            tab.append(row[0])
    loop = True;
    while loop:
            categorie=raw_input("Donnez la catégorie à laquelle appartient le document : ")
            for i in tab:
                    if (categorie == i):
                            loop = False;
    #Licence
    tab = []
    print("Licences disponibles : ");
    cursor.execute("SELECT * FROM Licence")
    for row in cursor:
            print(row[0])
            tab.append(row[0])
    loop = True;
    while loop:
            licence=raw_input("Donnez la licence du document : ")
            for i in tab:
                    if (licence == i):
                            loop = False;
    #Mot_cle
    mot_cle=raw_input("Attribuez un mot clé : ")
    cursor.execute("SELECT * from MotCle WHERE mot_cle = '"+mot_cle+"'")
    count = cursor.fetchone()
    #On ajoute si le mot cle n'existe pas
    if count == 0 :
            cursor.execute("INSERT INTO MotCle(mot_cle) VALUES('"+mot_cle+"')")

    #Etudiants
    tab_etu = []
    while True:
            nb_etu=input("Combien y a-t-il d'auteurs? (1 minimum) : ")
            if nb_etu > 0 :
                    break
    for i in range(0,nb_etu):
            print("Renseignez les auteurs (%d restants) : " % (nb_etu-i))
            while True : 
                    login=raw_input("Login : ")
                    if len(login) == 8 :
                            break
                    print("Login incorrect.")
            cursor.execute("SELECT COUNT(*) FROM Etudiant WHERE login = '" +login+ "'")
            count = cursor.fetchone()[0]
            #Si le login existe
            if count > 0 :
                    cursor.execute("SELECT e.nom, e.prenom FROM Etudiant e WHERE e.login = '" +login+ "'")
                    for row in cursor : 
                            nom=row[0]
                            prenom=row[1]
            #Sinon, ajout dans la table Etudiants
            else :
                    while True :
                            nom=raw_input("Nom : ")
                            prenom=raw_input("Prénom : ")
                            #Verifie si le nom/prenom contients des nombres
                            if any(i.isdigit() for i in (nom+prenom)) == False :
                                    break;
                    cursor.execute("INSERT INTO Etudiant(login,nom,prenom) VALUES ('"+login+"','"+nom.title()+"','"+prenom.title()+"')")
            tab_etu.append(login)
    #liste_etu=",".join(tab_etu)

    #Enseignants
    tab_ens = []
    while True:
            nb_ens=input("Combien y a-t-il d'enseignant tuteurs du documents? : ")
            if nb_ens > 0 :
                    break
    for i in range(0,nb_ens):
            print("Renseignez les enseignants (%d restants) : " % (nb_ens-i))
            while True : 
                    login=raw_input("Login : ")
                    if len(login) == 8 :
                            break
                    print("Login incorrect.")
            cursor.execute("SELECT COUNT(*) FROM Enseignant WHERE login = '" +login+ "'")
            count = cursor.fetchone()[0]
            #Si le login existe
            if count > 0 :
                    cursor.execute("SELECT e.nom, e.prenom FROM Enseignant e WHERE e.login = '" +login+ "'")
                    for row in cursor : 
                            nom=row[0]
                            prenom=row[1]
            #Sinon, ajout dans la table Enseignant
            else :
                    while True :
                            nom=raw_input("Nom : ")
                            prenom=raw_input("Prénom : ")
                            #Verifie si le nom/prenom contients des nombres
                            if any(i.isdigit() for i in (nom+prenom)) == False :
                                    break;
                    cursor.execute("INSERT INTO Enseignant(login,nom,prenom) VALUES ('"+login+"','"+nom.title()+"','"+prenom.title()+"')")
            tab_ens.append(login)
    #liste_ens=",".join(tab_ens)
    cursor = connection.cursor()
    try :
            cursor.execute("DECLARE osemestre REF typSemestre; ocategorie REF typCategorie; olicence REF typLicence; omotcle REF typMotCle; oetu REF typeEtu; oens REF typeEns; BEGIN SELECT REF(s) INTO osemestre FROM Semestre s WHERE s.annee='"+str(annee)+"' AND s.saison='"+saison+"'; SELECT REF(c) INTO ocategorie FROM Categorie c WHERE c.nom='"+categorie+"'; SELECT REF(l) INTO olicence FROM Licence l WHERE l.code='"+licence+"'; SELECT REF(m) INTO omotcle FROM MotCle m WHERE m.mot_cle='"+mot_cle+"'; SELECT REF(etu) INTO oetu FROM Etudiant etu WHERE etu.login='"+str(tab_etu[0])+"'; SELECT REF(ens) INTO oens FROM Enseignant ens WHERE ens.login='"+str(tab_ens[0])+"'; INSERT INTO Documents (idDoc,archivedoc, titre, date_pb, auteur, professeur, description, semestredoc, categorie, licencedoc, motCle) VALUES('"+str(iddoc)+"','N','"+titre+"',sysdate,listeEtu(refetu(oetu)),listeEns(refens(oens)),'"+description+"',osemestre,ocategorie,listeLicence(refLicence(olicence)),listeMotCle(refMotCle(omotcle))); END;")
    except  cx_Oracle.DatabaseError as exc:
            error = exc.args
            print("Une erreur est survenue lors de l'insertion (Code d'erreur: %d)" % error.code)
    finally :
            cursor.close()        
   
    print("L'insertion à été réalisée correctement")
    connection.commit()

#fonction pour rechercher des documents par catégorie

def recherche_cat() :
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categorie")
        for row in cursor:
                print(" Categorie:", row)
        print("Ecrivez le nom de la categorie dans laquelle vous souhaitez rechercher un document")
        cat=raw_input()
        cursor.execute("SELECT COUNT (*) FROM( SELECT d.iddoc, d.titre FROM Documents d WHERE d.categorie.nom='"+cat+"' AND archivedoc <> 'Y') ")
        count = cursor.fetchall()[0][0]
        if count > 0 :
                sel_cat=("SELECT d.iddoc, d.titre FROM Documents d WHERE d.categorie.nom='"+cat+"' AND d.archivedoc <> 'Y'")
                cursor = connection.cursor()
                cursor.execute(sel_cat)

                for row in cursor:
                        print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))
                info_doc()

        else :
                print("Il n'y a pas de documents à afficher")

#fonction de recherche par mot clé !! 
def recherche_mot_cle() :
        cursor = connection.cursor()
        cursor.execute("select * from MotCle")
        i=0
        for row in cursor:
                print("Mot Clé:", row)
                i=i+1
        print("Entrez le mot clé qui vous interesse")
        mot=raw_input()
        cursor.execute("SELECT COUNT (*) FROM( SELECT d.iddoc, d.titre FROM Documents d, TABLE (d.motCle) m WHERE m.refMotCle.mot_cle ='"+mot+"' AND d.archivedoc <> 'Y') ")
        count = cursor.fetchall()[0][0]
        if count > 0 :
                sel_mot=( "SELECT d.iddoc, d.titre FROM Documents d, TABLE (d.motCle) m WHERE m.refMotCle.mot_cle ='"+mot+"' AND d.archivedoc <> 'Y'")
                cursor = connection.cursor()
                cursor.execute(sel_mot)

                for row in cursor:
                        print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))
                info_doc()

        else :
                print("Il n'y a pas de documents à afficher")

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
        #       print ("Année incorrecte.")

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
                        cursor.execute("SELECT d.iddoc, d.titre FROM Documents d, TABLE(d.auteur) au WHERE au.Etudiant.login ='"+etu+"' AND d.archivedoc <> 'Y'")
                        for row in cursor:
                                print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))
                        
                else :
                        print("pas de documents à afficher")
                info_doc()




#fonction pour afficher le menu de choix entre admin ou eleve
def menu_personne() :
        print("Vous êtes un : \n 0- administrateur \n 1- un élève/prof ... \n 2-vous voulez quitter")
        type=input()
        while type<0 or type>2:
            print("L'utilisateur demandé n'existe pas, réessayez")
            type=input()

        return type


#fonction pour afficher les fonctions que l'admin peut réaliser
def menu_admin() :
        print("Voici les différentes actions que vous pouvez réaliser : \n 0- archiver un document \n 1- ajouter une licence \n 2- ajouter une categorie\n 3-retirer un document de l'archive \n 4-quitter le mode administrateur \n entrez le numéro de l'action que vous souhaitez réaliser")
        action=input()
        return action

#fonction pour afficher les fonctions qu'un utilisateur CAS peut réaliser

def menu_eleve() :
    print("Voici les différentes actions que vous pouvez réaliser : \n 0 - ajouter un document \n 1-rechercher un document \n 2-quitter le mode utilisateur")
    action=input()

    while action > 2:
        print("L'action demandée n'existe pas réessayez")
        action=input()

    return action


#fonction de recherche combinée
def recherche_combinee() :
        #print("Vous voulez rechercher par : \n 0- catégorie \n 1- mot-clé \n 2- semestre \n 3- saisi terminé")
        #choix=input()
        count = 0
        choix = 0
        sql = ""
        cursor = connection.cursor()
        while choix >= 0 and choix <= 3:
                print("Vous voulez rechercher par(Pour terminer votre saisi, tapez 3) : \n 0- catégorie \n 1- mot-clé \n 2- semestre \n 3- saisi terminé")
                choix=input()
                if choix == 0:
                        cursor.execute("SELECT * FROM categorie")
                        for row in cursor:
                                print(" Categorie:", row)
                        print("Ecrivez le nom de la categorie dans laquelle vous souhaitez rechercher un document")
                        cat=raw_input()
                        if count == 1:
                                sql += " UNION SELECT d.iddoc, d.titre FROM Documents d WHERE d.categorie.nom='"+cat+"' AND archivedoc <> 'Y'"
                        else:
                                sql += "SELECT d.iddoc, d.titre FROM Documents d WHERE d.categorie.nom='"+cat+"' AND archivedoc <> 'Y'"
                        count = 1
                if choix == 1:
                        cursor.execute("SELECT * FROM MOTCLE")
                        for row in cursor:
                                print(" MotCle:", row)
                        print("Ecrivez le mot-clé dans laquelle vous souhaitez rechercher un document")
                        motcle=raw_input()
                        if count == 1:
                                sql += " UNION SELECT d.iddoc, d.titre FROM Documents d, TABLE(d.motCle) m WHERE m.refMotCle.mot_cle= '"+motcle+"' AND archivedoc <> 'Y'"
                        else:
                                sql += "SELECT d.iddoc, d.titre FROM Documents d, TABLE(d.motCle) m WHERE m.refMotCle.mot_cle= '"+motcle+"' AND archivedoc <> 'Y'"
                        count = 1
                if choix == 2:
                        cursor.execute("SELECT * FROM SEMESTRE")
                        for row in cursor:
                                print(" semestre:", row)
                        print("Ecrivez le nom du semestre(A ou P) dans laquelle vous souhaitez rechercher un document")
                        sem=raw_input()
                        print("Ecrivez le nom de l'année dans laquelle vous souhaitez rechercher un document")
                        an=raw_input()
                        if count == 1:
                                sql += " UNION SELECT d.iddoc, d.titre FROM Documents d WHERE d.semestredoc.saison = '"+sem+"' AND d.semestredoc.annee = '"+an+"' AND archivedoc <> 'Y'"
                        else:
                                sql += "SELECT d.iddoc, d.titre FROM Documents d WHERE d.semestredoc.saison = '"+sem+"' AND d.semestredoc.annee = '"+an+"' AND archivedoc <> 'Y'"
                        count = 1
                if choix == 3:
                        #print(sql)
                        cursor.execute("SELECT COUNT(*) FROM("+sql+")")
                        nb = cursor.fetchall()[0][0]
                        if nb > 0:
                                sel_cat=(sql)
                                cursor = connection.cursor()
                                cursor.execute(sel_cat)
                                for row in cursor:
                                        print("iddoc : {:20s} Titre: {:100s}".format(row[0], row[1]))
                                info_doc()
                        else :
                                print("Il n'y a pas de documents à afficher")
                        choix = 4
                        count = 0


#corps du programme principale

etat = 1

while etat == 1 : #etat 1 est l'état ou on choisi admin ou utilisateur cas
        type=menu_personne()
        etat = 2
        while etat == 2 : #etat 2 = on choisi un action a réaliser en fonction des fonctions qui nous sont proposées

            if type == 0 : #partie admin
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
                            ajout_licence()
                    #ajouter une categorie
                    if action == 2 :
                            ajout_categorie()
                    #enlever un document de l'archive
                    if action == 3 :
                            retour_archive()

                    if action == 4 :
                            etat = 1


            if type == 1 : #partie user CAS
                    action=menu_eleve()
                    if action == 0 :
                            ajout_doc()


                    if action == 1 :
                            print("Vous souhaitez rechercher un document \n")
                            while action<3 :
                                    print("Vous souhaitez faire une recherche par : \n 0-categorie \n 1- mot clé \n 2 - nom de l'auteur \n 3 - semestre \n 4 - recherche combinée \n 5 - retour au menu élève")
                                    recherche = input()
                                    if recherche == 0 :
                                            recherche_cat()

                                    if recherche == 1:
                                            #recherche par mot clé
                                            recherche_mot_cle()

                                    if recherche == 2 :
                                    	#recherche par auteur
                                            recherche_par_etu()


                                    if recherche == 3 :
                                    #recherche par semestre
                                            recherche_semestre()

                                    if recherche == 4 :
                                    #recherche par semestre
                                            recherche_combinee()

                                    if recherche == 5 :
                                            recherche = 6
                                            action = 6
                                            etat = 2



                    if action == 2 :
                            etat=1

            if type == 2 :
                    exit()
