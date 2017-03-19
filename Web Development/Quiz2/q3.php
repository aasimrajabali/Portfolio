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
	if ($_SESSION['number'] == 3) {
		$answer = $_POST['q3'];  
		if ($answer == "3b") {          
			print("That is Correct. <br>");
			$_SESSION['correct'] += 10;
		}
		else {
			print("That is Incorrect. <br>");
		}  
		print<<<QUESTION_4
		<html><head><link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head>
			<body>
				<h3> Astronomy Quiz </h3>
				<form method = "post" action = "q4.php">
				<p><b>4)</b> Stars that live the longest have<br>
				a) high mass <input type="checkbox" name="q4" value="a" > <br>
				b) high temperature <input type="checkbox" name="q4" value="b"> <br>
				c) lots of hydrogen <input type="checkbox" name="q4" value="c"> <br>
				d) small mass <input type="checkbox" name="q4" value="d"> <br> <br> 
				<input type="submit" value="Submit">
				</p>
			</body>
		</html>
QUESTION_4;
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