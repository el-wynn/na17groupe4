-- Pour la mise en archive d'un doc
Update Document
SET archive = TRUE
WHERE iddoc = 2;

-- Pour supprimer une ligne dans la table
DELETE FROM Categorie
WHERE nom = 'PCB';

-- Pour supprimer la table et sa relation
DROP TABLE Document CASCADE; 
