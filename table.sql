
-- Création d'un Type Enum pour Semestre
CREATE TYPE SAISON AS ENUM('A','P');

-- Création de la base de donées
CREATE DATABASE Etudoc;

-- Création de la table Etudiant
DROP TABLE IF EXISTS Etudiant;
CREATE TABLE Etudiant
(
login VARCHAR(8) PRIMARY KEY,
nom VARCHAR(30) NOT NULL,
prenom VARCHAR(30) NOT NULL,
mail VARCHAR(50) NOT NULL UNIQUE
);

-- Création de la table Enseignant
DROP TABLE IF EXISTS Enseignant;
CREATE TABLE Enseignant
(
login VARCHAR(8) PRIMARY KEY,
nom VARCHAR(30) NOT NULL,
prenom VARCHAR(30) NOT NULL,
mail VARCHAR(50) NOT NULL UNIQUE
);

-- Création de la table Exterieur
DROP TABLE IF EXISTS Exterieur;
CREATE TABLE Exterieur
(
login VARCHAR(8) PRIMARY KEY,
nom VARCHAR(30) NOT NULL,
prenom VARCHAR(30) NOT NULL,
mail VARCHAR(50) NOT NULL UNIQUE
);

-- Création de la table Semesre
DROP TABLE IF EXISTS Semestre;
CREATE TABLE Semestre
(
semestre VARCHAR(3) PRIMARY KEY,
annee INTEGER NOT NULL,
saison SAISON NOT NULL
);

-- Création de la table UV
DROP TABLE IF EXISTS UV;
CREATE TABLE UV
(
code VARCHAR(4) PRIMARY KEY,
nom VARCHAR(50) NOT NULL
);

-- Création de la table Type
DROP TABLE IF EXISTS Type;
CREATE TABLE Type
(
nom VARCHAR(30) PRIMARY KEY
);

-- Création de la table Mot_cle
DROP TABLE IF EXISTS Mot_cle;
CREATE TABLE Mot_cle
(
mot VARCHAR(50) PRIMARY KEY
);

-- Création de la table Categorie
DROP TABLE IF EXISTS Categorie;
CREATE TABLE Categorie
(
nom VARCHAR(50) PRIMARY KEY
);

--Création de la table Licence
DROP TABLE IF EXISTS Licence;
CREATE TABLE Licence
(
code VARCHAR(10) PRIMARY KEY,
nom VARCHAR(50) NOT NULL
);

-- Création de la table Document
DROP TABLE IF EXISTS Document;
CREATE TABLE Document
(
iddoc INTEGER NOT NULL PRIMARY KEY,
titre VARCHAR(100) NOT NULL,
date_pb DATE NOT NULL,
description TEXT,
archive BOOLEAN NOT NULL DEFAULT FALSE,
semestre VARCHAR(3) REFERENCES Semestre(semestre) NOT NULL,
uv VARCHAR(4) REFERENCES UV(code) NOT NULL,
type VARCHAR(30) REFERENCES Type(nom) NOT NULL,
categorie VARCHAR(30) REFERENCES Categorie(nom) NOT NULL
);


-- Création de la table association Ecrire
DROP TABLE IF EXISTS Ecrire;
CREATE TABLE Ecrire
(
etudiant VARCHAR(8) REFERENCES Etudiant(login),
document INTEGER REFERENCES Document(iddoc),
PRIMARY KEY (etudiant,document)
);

-- Création de la table association Valider
DROP TABLE IF EXISTS Valider;
CREATE TABLE Valider
(
enseignant VARCHAR(8) REFERENCES Enseignant(login),
document INTEGER REFERENCES Document(iddoc),
PRIMARY KEY (enseignant,document)
);

-- Création de la table association Participer
DROP TABLE IF EXISTS Participer;
CREATE TABLE Participer
(
exterieur VARCHAR(8) REFERENCES Exterieur(login),
document INTEGER REFERENCES Document(iddoc),
PRIMARY KEY (exterieur,document)
);

-- Création de la table association Caracteriser
DROP TABLE IF EXISTS Caracteriser;
CREATE TABLE Caracteriser
(
mot_cle VARCHAR(50) REFERENCES Mot_cle(mot),
document INTEGER REFERENCES Document(iddoc),
PRIMARY KEY (mot_cle,document)
);

-- Création de la table association Publication
DROP TABLE IF EXISTS Publication;
CREATE TABLE Publication
(
licence VARCHAR(50) REFERENCES Licence(code),
document INTEGER REFERENCES Document(iddoc),
PRIMARY KEY (licence,document)
);
