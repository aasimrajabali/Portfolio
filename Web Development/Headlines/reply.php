<?php
extract ($_POST);
$log_name = $_POST["log_name"];
$log_pw = $_POST["log_pw"];

$myfile = fopen("passwd.txt", "r") or die("Unable to open file!");
$usernames = array();
$passwords = array();
$success = False;
$error = False;

while(!feof($myfile)) {	
  $passwd_list =  fgets($myfile);
  $cookie_list = explode(":", $passwd_list); 
  array_push($usernames, $cookie_list[0]); //puts all usernames in the txt file into a list
  array_push($passwords, $cookie_list[1]); //puts all passwords in the txt file into a list
}

fclose($myfile);
for ($i = 0; $i < count($passwords); $i++) {
	$cookie_name = $usernames[$i];
	$cookie_pwd = $passwords[$i];
	$cookie_pwd = substr($cookie_pwd, 0, -1);
	if (empty($log_name) or empty($log_pw)) {
		$error = True;
		break;
	}
	if (($log_pw == $cookie_pwd) and ($log_name == $cookie_name)){   //if the user logs in using a username/pw from the txt file
		$success = True;
		break;
	}
}

if ($success == True) {
	setcookie($log_name,$log_name, time()+120); 
	print<<<SUCCESS_MESSAGE
	<html><head><title>Error Found</title><link rel = "stylesheet" type="text/css" href = "./headline.css"></head><body>
	<script type='text/javascript'>window.alert("You are now logged in.");</script>
	<a href="./login.html">Return to Login</a> <br>
	<a href="./headline.php">Return to Homepage</a> <br> </body></html>
SUCCESS_MESSAGE;
}
elseif ($error == True) {
	print<<<ERROR_MESSAGE5
		<html><head><title>Error Found</title><link rel = "stylesheet" type="text/css" href = "./headline.css"></head><body>
		<script type='text/javascript'>window.alert("Please fill in all info to log in.");</script>
		<a href="./login.html">Return to Login</a> <br>
		<a href="./headline.php">Return to Homepage</a> <br> </body> </html>
ERROR_MESSAGE5;
}
	
else {
	print<<<ERROR_MESSAGE4
		<html><head><title>Error Found</title><link rel = "stylesheet" type="text/css" href = "./headline.css"></head><body>
		<script type='text/javascript'>window.alert("Incorrect username or password.");</script>
		<a href="./login.html">Return to Login</a> <br>
		<a href="./headline.php">Return to Homepage</a> <br> </body> </html>
ERROR_MESSAGE4;
}

 
?>