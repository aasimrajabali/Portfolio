<?php
	extract ($_POST);
	$log_name = $_POST["log_name"];
	$log_pw = $_POST["log_pw"];
	$success = False;
	$err1 = False;
	$myfile = fopen("passwd.txt", "r") or die("Unable to open file!");
	$myresults = fopen("results.txt", "r") or die("Unable to open file!");
	
	while(!feof($myfile)) {	
		//TO VALIDATE USERNAME AND PASSWORD//
		$passwd_list =  fgets($myfile);
		$cookie_list = explode(":", $passwd_list); 
		$cookie_pwd = substr($cookie_list[1], 0, -1); //password in the file
		$cookie_name = $cookie_list[0]; //username in file
		if (($log_pw == $cookie_pwd) and ($log_name == $cookie_name)) {
			$success = True;
		}
	  
		//TO CHECK IF USER HAS ALREADY TAKEN THE QUIZ//
		$res_list = fgets($myresults);
		$user_list = explode(":", $res_list);
		$username = $user_list[0]; // gets the name of user already in results list
		if ($log_name == $username) {
			$success = False;
			$error1 = True; 
			break;
		}
		
	}
	fclose($myfile);
	
	
		
	if ($success == True) { //username and password are valid
		session_start();
		$_SESSION['user'] = $_POST["log_name"]; //keeps username in the session
		$_SESSION["correct"] = 0; //keeps track of points
		$_SESSION['start'] = time(); // Taking now logged in time, session ends in 15 minutes.
		$_SESSION['expire'] = $_SESSION['start'] + (15 * 60); //15 min timer
		$_SESSION['number'] = 0; //keeps track of questions
		$tot_num = 6;

		$now = time(); // Checking the time now when home page starts.
		
        if ($now > $_SESSION['expire']) { //if the user exceeded the time allowed 
            session_destroy();
			print ("Session has expired. <a href='./login.html'>Return to Login Page </a>");
		}
		else {
			print<<<QUIZ_QUESTION_1
			<html><head><link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head>
				<body>
					<h3> Astronomy Quiz </h3> 
					<p> You will be given $tot_num questions in this quiz. You can only take the quiz once. If you go backwards or refresh the page at any time 
					in the quiz, the quiz ends and your results will be recorded.<br /><br/>
						Here is your first question: <br /><br />
					<form method = "post" action = "q1.php">
					<p><b>1)</b> According to Kepler the orbit of the earth is a circle with the sun at the center.
					<input type="radio" name="q1" value="true"> True
					<input type="radio" name="q1" value="false"> False <br> <br>
					<input type="submit" value="Submit">
					</p>
				</body>
			</html>
QUIZ_QUESTION_1;
			}	
	}
	
	elseif ($error1 == True) { //if the user enters a username that has already taken the quiz
		print<<<ERROR
		<html><head><link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head>
			<body>
				<p> This user has already taken the quiz. You cannot take the quiz more than once. </p>
				<a href = "./login.html"> Return to Login Page </a>
			</body>
		</html>
ERROR;
	}
	else { //user entered an invalid username, password, or left a box empty
		print<<<ERROR_MESSAGE
		<html><head><title>Error Found</title>
		<link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head><body>
		<script type='text/javascript'>window.alert("Incorrect username or password.");</script>
		<a href="./login.html">Return to Login</a> <br>
		 </body> </html>
ERROR_MESSAGE;
	}
	
?>