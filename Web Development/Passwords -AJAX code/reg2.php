<?php
	extract ($_POST);
	$reg_user = $_POST["reg_user"];
	$reg_user_test = strtolower($reg_user);
	$reg_pwd = $_POST["reg_pwd"];
	$reg_pwd = md5($reg_pwd); // gets password in encrypted form
	$success = True; //we assume the username has not been taken
	$myfile = fopen("passwd.txt", "r") or die("Unable to open file!");
	while(!feof($myfile)) {	
		//TO VALIDATE USERNAME//
		$passwd_list =  fgets($myfile);
		$list = explode(":", $passwd_list); 
		$user = $list[0]; //username in file
		$user_test = strtolower($user);
		if ($user == $reg_user_test) { //if the username is taken
			$success = False;
			break;
		}
	}
	fclose($myfile);
	if ($success == True) {
		$myresults = fopen("passwd.txt","a") or die("Unable to open file!");
		fwrite($myresults, "$reg_user:$reg_pwd\n"); //stores the new username and encrypted password
		fclose($myresults);
		print <<<THANK_MSG
		<html>
		<head>
			<script>
				window.alert("Thanks for Registering.");
			</script>
		</head>
		<h1>Registration Successful </h1>
		<a href="./hwk14.html">Return to Registration Screen</a>
		</html>
THANK_MSG;
	}
	if ($success == False) {
		print <<<ERROR
		<html>
			<head>
				<title>Failed Registration</title>
			</head>
			
			<body>
				<h1> Registration Failed </h1>
				<p>You entered a username already taken</p>
				<a href="./hwk14.html">Return to Registration Screen</a>
			</body>
		</html>
ERROR;
	}
	
?>