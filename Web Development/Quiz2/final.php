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
	if ($_SESSION['number'] == 6) {
		$answer = $_POST['q6'];  
		$answer = strtolower($answer);
		if ($answer == "age") {          
			print("That is Correct. <br>");
			$_SESSION['correct'] += 10;
		}
		else {
			print("That is Incorrect. <br>");
		}  
		
		$correct = $_SESSION['correct'];
		$user = $_SESSION['user'];
		$myresults = fopen("results.txt","a") or die("Unable to open file!");
		fwrite($myresults, "$user:$correct\n");
		fclose($myresults);
		session_destroy();
		print<<<END_PAGE
		<html><head><link rel = "stylesheet" type = "text/css" href="./quiz2.css"></head>
			<body>
				<h3> End of Quiz </h3>
				<p> Your score is $correct out of 60. Your results are now recorded and you cannot take the quiz more than once. </p>
			</body>
		</html>
END_PAGE;
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