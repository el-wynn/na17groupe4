-- Insertion dans la table Etudiant
INSERT INTO Etudiant
VALUES ('jiayueqi',
        'JIA',
        'Yueqing',
        'yueqing.jia@etu.utc.fr'
);
INSERT INTO Etudiant
VALUES ('neglokpe',
        'NEGLOKPE',
        'Elvynn',
        'elvynn.neglokpe@etu.utc.fr'
);
INSERT INTO Etudiant
VALUES ('galzinno',
        'GALZIN',
        'Noémie',
        'galzin.noemie@etu.utc.fr'
);

INSERT INTO Etudiant
VALUES ('duboisoc',
        'DUBOIS',
        'Océane',
        'oceane.dubois@etu.utc.fr'
);

-- Insertion dans la table Enseignant
INSERT INTO Enseignant
VALUES ('gonzalez',
        'GONZALEZ',
        'Hernan',
        'hernan.gonzalez@hds.utc.fr'
);
INSERT INTO Enseignant
VALUES ('abelmari',
        'ABEL',
        'Marie-Hélène',
        'marie-helene.abel@hds.utc.fr'
);
INSERT INTO Enseignant
VALUES ('afoutniz',
        'AFOUTNI',
        'Zoubida',
        'zoubida.afoutni@utc.fr'
);

-- Insertion dans la table Exterieur
INSERT INTO Exterieur
VALUES ('azzimont',
        'AZZIMONTI',
        'Brigitte',
        'brigitte.azzimonti@hds.utc.fr'
);
INSERT INTO Exterieur
VALUES ('akrouche',
        'AKROUCHE',
        'Joanna',
        'oanna.akrouche@hds.utc.fr'
);
INSERT INTO Exterieur
VALUES ('bachimon',
        'BACHIMONT',
        'Bruno',
        'bruno.bachimont@hds.utc.fr'
);

-- Insertion dans la table Semestre
INSERT INTO Semestre
VALUES ('A17',
        2017,
        'A');
INSERT INTO Semestre
VALUES ('P17',
        2017,
        'P');
INSERT INTO Semestre
VALUES ('A16',
        2016,
        'A');
INSERT INTO Semestre
VALUES ('P16',
        2016,
        'P');
INSERT INTO Semestre
VALUES ('A15',
        2015,
        'A');
INSERT INTO Semestre
VALUES ('P15',
        2015,
        'P');


-- Insertion dans la table UV
INSERT INTO UV
VALUES ('NA17',
        'Conception de Base De Données');
INSERT INTO UV
VALUES ('TN05',
        'Stage Ouvrier');
INSERT INTO UV
VALUES ('LA13',
        'Anglais Niveau B2');
INSERT INTO UV
VALUES ('SR04',
        'Réseaux Informatiques');
INSERT INTO UV
VALUES ('LO17',
        'Indextation et Recherche');

-- Insertion dans la table Type
INSERT INTO Type
VALUES ('Rapport UV');
INSERT INTO Type
VALUES ('Rapport STAGE');
INSERT INTO Type
VALUES ('Rapport TX');
INSERT INTO Type
VALUES ('Rapport TD');
INSERT INTO Type
VALUES ('Rapport TP');

-- Insertion dans la table Mot_cle
INSERT INTO Mot_cle
VALUES ('XML');
INSERT INTO Mot_cle
VALUES ('SQL');
INSERT INTO Mot_cle
VALUES ('PHP');
INSERT INTO Mot_cle
VALUES ('Perl');
INSERT INTO Mot_cle
VALUES ('HTML');

-- Insertion dans la table Categorie
INSERT INTO Categorie
VALUES ('CS');
INSERT INTO Categorie
VALUES ('TM');
INSERT INTO Categorie
VALUES ('TX');
INSERT INTO Categorie
VALUES ('TSH');
INSERT INTO Categorie
VALUES ('PCB');
INSERT INTO Categorie
VALUES ('SP');

-- Insertion dans la table Licence
INSERT INTO Licence
VALUES ('CC-ZERO',
        'Licence CC-ZERO'
);
INSERT INTO Licence
VALUES ('CC-BY',
        'Licence CC-BY'
);
INSERT INTO Licence
VALUES ('CC-BY-SA',
        'Licence CC-BY-SA'
);
INSERT INTO Licence
VALUES ('CC-BY-ND',
        'Licence CC-BY-ND'
);
INSERT INTO Licence
VALUES ('CC-BY-NC',
        'Licence CC-BY-NC'
);

-- Insertion dans la table Document
INSERT INTO Document
VALUES ('1',
        'Rapport1',
        CURRENT_DATE,
        'Rapport de Stage TN05',
        'FALSE',
        'A17',
        'TN05',
        'Rapport STAGE',
        'SP'
);
INSERT INTO Document
VALUES ('2',
        'Rapport2',
        CURRENT_DATE,
        'Rapport de NA17',
        'FALSE',
        'A16',
        'NA17',
        'Rapport UV',
        'TM'
);
INSERT INTO Document
VALUES ('3',
        'Rapport3',
        CURRENT_DATE,
        'Rapport de SR04',
        'FALSE',
        'P17',
        'SR04',
        'Rapport UV',
        'CS'
);
INSERT INTO Document
VALUES ('4',
        'Rapport4',
        CURRENT_DATE,
        'Rapport de LO17',
        'FALSE',
        'P16',
        'LO17',
        'Rapport UV',
        'TM'
);

-- Insertion dans la table association Ecrire
INSERT INTO Ecrire
VALUES ('jiayueqi',
        '1'
);
INSERT INTO Ecrire
VALUES ('neglokpe',
        '2'
);
INSERT INTO Ecrire
VALUES ('galzinno',
        '3'
);
INSERT INTO Ecrire
VALUES ('duboisoc',
        '4'
);

-- Insertion dans la table association Valider
INSERT INTO Valider
VALUES ('gonzalez',
        '1'
);
INSERT INTO Valider
VALUES ('abelmari',
        '2'
);
INSERT INTO Valider
VALUES ('afoutniz',
        '3'
);
INSERT INTO Valider
VALUES ('afoutniz',
        '4'
);

-- Insertion dans la table association Participer
INSERT INTO Participer
VALUES ('azzimont',
        '1'
);
INSERT INTO Participer
VALUES ('akrouche',
        '2'
);
INSERT INTO Participer
VALUES ('akrouche',
        '3'
);
INSERT INTO Participer
VALUES ('bachimon',
        '4'
);

-- Insertion dans la table association Caracteriser
INSERT INTO Caracteriser
VALUES ('PHP',
        '1'
);
VALUES ('HTML',
        '1'
);
INSERT INTO Caracteriser
VALUES ('XML',
        '2'
);
INSERT INTO Caracteriser
VALUES ('PHP',
        '3'
);
INSERT INTO Caracteriser
VALUES ('Perl',
        '3'
);
INSERT INTO Caracteriser
VALUES ('XML',
        '3'
);
INSERT INTO Caracteriser
VALUES ('PHP',
        '4'
);
INSERT INTO Caracteriser
VALUES ('HTML',
        '4'
);

-- Insertion dans la table association Publication
INSERT INTO Publication
VALUES ('CC-BY',
        '1'
);
INSERT INTO Publication
VALUES ('CC-BY-SA',
        '1'
);
INSERT INTO Publication
VALUES ('CC-ZERO',
        '2'
);
INSERT INTO Publication
VALUES ('CC-BY',
        '3'
);
INSERT INTO Publication
VALUES ('CC-BY-ND',
        '3'
);
INSERT INTO Publication
VALUES ('CC-BY-ND',
        '4'
);
INSERT INTO Publication
VALUES ('CC-BY-SA',
        '4'
);
