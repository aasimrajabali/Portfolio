<?php
	session_start();
	$now = time(); // Checking the time now when page starts.
	$_SESSION['number'] += 1;	
	if ($now > $_SESSION['expire']) { //if the user exceeded the time allowed 
		print ("Your 15 minutes are up. Your result will be your score before your time expired. <br> <a href='./login.html'>Return to Login Page </a> <br>");		
		session_destroy();
		exit($_SESSION['correct'] . " out of 60.");
		
		$correct = $_SESSION['correct'];
		$user = $_SESSION['user'];
		$myresults = fopen("results.txt","a") or die("Unable to open file!");
		fwrite($myresults, "$user:$correct\n");
		fclose($myresults);
	}
	if ($_SESSION['number'] == 1) {
		$answer = $_POST['q1'];  
		if ($answer == "false") {          
			print("That is Correct. <br>");
			$_SESSION['correct'] += 10;
		}
		else {
			print("That is Incorrect. <br>");
		}  
		print<<<QUESTION_2
		<html><head><link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head>
			<body>
				<h3> Astronomy Quiz </h3>
				<form method = "post" action = "q2.php">
				<p><b>2)</b> Ancient astronomers did consider the heliocentric model 
				of the solar system but rejected it because they could not detect parallax.
				<input type="radio" name="q2" value="true"> True
				<input type="radio" name="q2" value="false"> False <br> <br>
				<input type="submit" value="Submit">
				</p>
			</body>
		</html>
QUESTION_2;
	}
	else {
		print<<<BACKWARDS_MSG
		<html><head><link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head>
			<body>
				<p> Because you went backwards on the quiz, you will no longer recieve points and your results
				will now be recorded. </p>
				<br> <a href='./login.html'>Return to Login Page </a> <br>
			</body>
		</html>
BACKWARDS_MSG;
		$correct = $_SESSION['correct'];
		$user = $_SESSION['user'];
		$myresults = fopen("results.txt","a") or die("Unable to open file!");
		fwrite($myresults, "$user:$correct\n");
		fclose($myresults);
	}
?>