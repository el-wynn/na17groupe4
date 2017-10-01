<?php
	echo 'DB chargée<br/>';

	// parcours la vue etudiants
	$req = $db->prepare('SELECT * FROM etudiants');
	$req->execute();

	// affiche la vue etudiants
	echo '<table> <tr> <th>Login</th> <th>Nom</th> <th>Prénom</th> <th>Mail</th> </tr> <tr>';
	while($line=$req->fetch(PDO::FETCH_ASSOC)) {
		echo '<tr>'.
		'<td>'.$line['login'].'</td>'.
		'<td>'.$line['nom'].'</td>'.
		'<td>'.$line['prenom'].'</td>'.
		'<td>'.$line['mail'].'</td>'.
		'</tr>';
	}
	echo '</table>';

	// parcours la vue exemple_type
	$req = $db->prepare('SELECT titre, date_pb, prenom_etu, nom_etu, type_doc FROM exemple_type');
	$req->execute();

	// affiche la vue exemple_type
	echo "<h1> Résultats de la recherche : </h1>";
	echo '<table> <tr> <th>Titre</th> <th>Auteur</th> <th>Date de publication</th> <th>Type</th> </tr> <tr>';
	while($line=$req->fetch(PDO::FETCH_ASSOC)) {
		echo '<tr>'.
		'<td>'.$line['titre'].'</td>'.
		'<td>'.$line['prenom_etu'].' '.$line['nom_etu'].'</td>'.
		'<td>'.date('d\/m\/Y',strtotime($line['date_pb'])).'</td>'.
		'<td>'.$line['type_doc'].'</td>'.
		'</tr>';
	}
	echo '</table>';

	echo '<br/>Thats All, Folks!<br/>';
?>