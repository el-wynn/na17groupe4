-- Création d'une vue pour tous les étudiant
CREATE VIEW ETUDIANTS
AS
   SELECT *
   FROM Etudiant;

-- Création d'une vue Document Total
CREATE VIEW DOCUMENTS_TOTAL
AS
  SELECT Document.iddoc ID_DOC,
  Document.titre Titre,
  Document.date_pb Date_pb,
  Document.description Description,
  Document.archive Etat_Archive,

  Document.semestre Semestre,
  Semestre.annee Annee,
  Semestre.saison Saison,
  Document.uv Code_UV,
  UV.nom Nom_UV,
  Document.type Type_Doc,
  Document.categorie categorie,

  Etudiant.login Code_Etu,
  Etudiant.nom NOM_Etu,
  Etudiant.prenom Prenom_Etu,
  Etudiant.mail Mail_Etu,

  Enseignant.login Code_Ens,
  Enseignant.nom NOM_Ens,
  Enseignant.prenom Prenom_Ens,
  Enseignant.mail Mail_Ens,

  Exterieur.login Code_Ext,
  Exterieur.nom NOM_Ext,
  Exterieur.prenom Prenom_Ext,
  Exterieur.mail Mail_Ext,

  Mot_cle.mot Mot_cle,
  Licence.code Code_Licence,
  Licence.nom Nom_Licence

  FROM Document
  INNER JOIN Semestre ON Document.semestre = Semestre.semestre
  INNER JOIN UV ON Document.uv = UV.code

  INNER JOIN Ecrire ON Document.iddoc = Ecrire.document
  INNER JOIN Etudiant ON Ecrire.etudiant = Etudiant.login

  INNER JOIN Valider ON Document.iddoc = Valider.document
  INNER JOIN Enseignant ON Valider.enseignant = Enseignant.login

  INNER JOIN Participer ON Document.iddoc = Participer.document
  INNER JOIN Exterieur ON Participer.exterieur = Exterieur.login

  INNER JOIN Caracteriser ON Document.iddoc = Caracteriser.document
  INNER JOIN Mot_cle ON Caracteriser.mot_cle = Mot_cle.mot

  INNER JOIN Publication ON Document.iddoc = Publication.document
  INNER JOIN Licence ON Publication.licence = Licence.code;

-- Création d'une vue pour Type Rapport UV
CREATE VIEW EXEMPLE_TYPE
AS
  SELECT DISTINCT ID_DOC,Titre,Date_pb,Annee,NOM_Etu,Prenom_Etu,Type_Doc
  FROM DOCUMENTS_TOTAL
  WHERE Type_Doc = 'Rapport UV';
