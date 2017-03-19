<?php
$myfile = fopen("passwd.txt", "r") or die("Unable to open file!");
$usernames = array();
$name_exists = False;
while(!feof($myfile)) {
  $passwd_list =  fgets($myfile) . "<br>";
  $cookie_list = explode(":", $passwd_list);
  array_push($usernames, $cookie_list[0]); //puts all usernames in the txt file into a list
}

for ($i = 0; $i < count($usernames); $i++) {
	$cookie_name = $usernames[$i];
	if(isset($_COOKIE[$cookie_name])) { 
		$name_exists = True;
	}
}

fclose($myfile);

	
	if($name_exists == True) { //if you have logged in, you should be able to visit the headlines
		print <<<LOGIN_CONFIRMED
		<html>
		<head>
			<title>Newspaper Headline</title>
			<link rel = "stylesheet" type="text/css" href = "./headline.css">
		</head>
		<body>
			<h1>UT Longhorns Newspaper</h1>
			<a href="./headline1.html"> Sports </a> <br>
			<a href="./headline2.html"> Arts/Leisure </a> <br>
			<a href="./headline3.html"> Current Events </a> <br>
			<a href="./headline4.html"> Upcoming Events </a> <br>
			<a href="./headline5.html"> Business </a> <br>
		</body>
		</html>
LOGIN_CONFIRMED;
	}
	else { 
		print <<<NON_LOGIN
		<html>
		<head>
			<title>Newspaper Headline</title>
			<link rel = "stylesheet" type="text/css" href = "./headline.css">
		</head>
		<body>
			<h1>UT Longhorns Newspaper</h1>
			<a href="./login.html"> Sports </a> <br>
			<a href="./login.html"> Arts/Leisure </a> <br>
			<a href="./login.html"> Current Events </a> <br>
			<a href="./login.html"> Upcoming Events </a> <br>
			<a href="./login.html"> Business </a> <br>
		</body>
		</html>
NON_LOGIN;
	}
?>
	