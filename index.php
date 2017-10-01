<meta charset="utf-8"/>

<?php

try
{
	$db = new PDO('pgsql:host=localhost;dbname=dbtest', 'testman', 'test');
	$db->query('set names utf8');
	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

	require('main.php');
}

catch (PDOException $e)
{
	die('<p> <h1>C\'EST L\'ÉCHEC!</h1>'.'La connexion à échoué. <br/>Erreur : '.$e->getMessage().'</p>');
}

$db = null;

?>