<?php
header('Content-Type: application/json');
include('functions.php');

$results = "";
$query = "";
if ((!isset($_POST['make_model'])) || ($_POST['make_model'] == "")){
	$query = "SELECT * FROM airplane_info LIMIT 200;";
}
else {
	$query  = create_query($_POST['make_model']);
}
$results = search_plane($query);
print(json_encode($results));
