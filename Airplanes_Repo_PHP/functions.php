<?php 
function search_plane($query) {
	$dbname = "";
	$user= "";
	$password = "";
	$host = "localhost";
	$db_connect = mysqli_connect($host,$user,$password,$dbname);
	$result = mysqli_query($db_connect,$query);
	$row_array = [];
	while($row = mysqli_fetch_assoc($result)){
	$row_array [] = $row; 
	}	mysqli_close($db_connect);
	return $row_array;
}

function create_query($data) {
	$data_split = explode(" ",$data,2);
	$query  = "";
	if (count($data_split) == 2) {
		$query = "SELECT * FROM airplane_info WHERE manufacturer LIKE '$data_split[0]%' AND model LIKE '$data_split[1]%';";
	}
	else {
		$query = "SELECT * FROM airplane_info WHERE manufacturer LIKE '%$data_split[0]%' OR model LIKE '%$data_split[0]%';";
	}
	return $query;
}
?>