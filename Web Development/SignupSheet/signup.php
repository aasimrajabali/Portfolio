<html>
<body>
<?php
	$myfile = fopen("./signup.txt", "a") or die("Unable to open file!");
	
	
	$names = array($_POST["user0"],$_POST["user1"], $_POST["user2"],$_POST["user3"],$_POST["user4"],
	$_POST["user5"], $_POST["user6"],$_POST["user7"],$_POST["user8"],$_POST["user9"]);
	$namlen = count($names);
	
	$times = array("8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm");
	$timlen = count($times);
	
	print <<<SIGNUP_PAGETOP
	<html>
	<head>
		<title>Thank You for Signing Up</title>
	</head>
	<body>
	<table align = "center" width = "50%" border = "2">
		<form action = "" method = "post">
			<caption> Thank You for Signing Up </caption> 
			<tr><th> Time </th><th> Name </th></tr>
SIGNUP_PAGETOP;

	for ($i = 0; $i< $namlen; $i++) {
		if (empty($names[i])) {
			print "<tr><td style='text-align:center;'>" . $times[$i] . "</td><td style='text-align:center;'>" . $names[$i] . "</td></tr>";
			fwrite($myfile,"$names[$i] \n");
		}
	}
	fclose($myfile);
	print <<<SIGNUP_PAGEBOTTOM
	</table>
	<br>
		</form>
SIGNUP_PAGEBOTTOM;
?>
</body>
</html>