<?php


 // get the q parameter from URL
$q = $_REQUEST["q"];

$result = null;

$str_test = strtolower($q);
$success = true;
$myfile = fopen("passwd.txt", "r") or die("Unable to open file!");
while(!feof($myfile)) {	
	//TO VALIDATE USERNAME//
	$passwd_list =  fgets($myfile);
	$list = explode(":", $passwd_list); 
	$user = $list[0]; //username in file
	$user_test = strtolower($user);
	if ($user_test == $str_test) { //if the username is taken
		$success = false;
	}
}
fclose($myfile);

if ($success == false) {
	$result = "Unavailable";
	echo "<span style='color: red;'>" . $result . "</span>";
}
else {
	$result = "Available";
	echo "<span style='color: green;'>" . $result . "</span>";
}

?> 