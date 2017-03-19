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
	if ($_SESSION['number'] == 2) {
		$answer = $_POST['q2'];  
		if ($answer == "true") {          
			print("That is Correct. <br>");
			$_SESSION['correct'] += 10;
		}
		else {
			print("That is Incorrect. <br>");
		}  
		print<<<QUESTION_3
		<html><head><link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head>
			<body>
				<h3> Astronomy Quiz </h3>
				<form method = "post" action = "q3.php">
				<p><b>3)</b>The total amount of energy that a star emits is directly related to its <br>
				a) surface gravity and magnetic field <input type="checkbox" name="q3" value="3a"> <br>
				b) radius and temperature <input type="checkbox" name="q3" value="3b"> <br>
				c) pressure and volume <input type="checkbox" name="q3" value="3c"> <br>
				d) location and velocity <input type="checkbox" name="q3" value="3d"> <br> <br>
				<input type="submit" value="Submit">
				</p>
			</body>
		</html>
QUESTION_3;
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