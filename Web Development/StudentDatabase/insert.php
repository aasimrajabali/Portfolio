<?php

if(isset($_POST['Submit'])) {
extract ($_POST);

$myfile = fopen("/u/z/users/cs329e-fa15/aasim612/password_info.txt", "r") or die("Unable to open file!");
$pwd = fgets($myfile);
$pwd = trim($pwd);
fclose($myfile);


// Connect to the MySQL database
$host = "fall-2015.cs.utexas.edu";
$user = "aasim612";
$dbs = "cs329e_aasim612";
$port = "3306";

$mysqli = new mysqli($host, $user, $pwd, $dbs);

if ($mysqli->connect_errno)
{
  die("mysqli_connect failed: " . mysqli_connect_errno());
}



$table = "STUDENTS";
$ID = $_POST["ID"];
$LName = $_POST["LName"];
$FName = $_POST["FName"];
$Major = $_POST["Major"];
$GPA = $_POST["GPA"];


$sql = "INSERT INTO STUDENTS (ID, Last, First,Major,GPA) VALUES (". $ID .",'". $LName ."', '". $FName ."','". $Major ."',". $GPA .")";

if ($mysqli->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $mysqli->error;
}

$mysqli->close();
}
?>

<html>
<head>
<title>Students Database Login</title>
</head>
<body>

<h2>Insert Record</h2>

<table width = "35%" border = "1">
<form id= "insert" method = "post" action = "<?php echo $_SERVER['PHP_SELF']; ?>" >
<tr>
<td>ID</td>
<td> <input type = "text" name = "ID" size = "45" /></td>
</tr>
<tr>
<td>Last Name</td>
<td> <input type = "text" name = "LName" size = "45" /></td>
</tr>
<tr>
<td>First Name</td>
<td> <input type = "text" name = "FName" size = "45" /></td>
</tr>
<tr>
<td>Major</td>
<td> <input type = "text" name = "Major" size = "45" /></td>
</tr>
<tr>
<td>GPA</td>
<td> <input type = "text" name = "GPA" size = "45" /></td>
</tr>
</table>
<input type = "submit" value = "Submit" name = "Submit"/>
<input type = "reset" value = "Reset" />
</form>

<script type="text/javascript">
  document.getElementById("insert").Submit.onclick = checkText;
  
   function checkText(){
    var elt = document.getElementById("insert");
    var ID = elt.ID.value;
    var LName = elt.LName.value;
    var FName = elt.FName.value;
    var Major = elt.Major.value;
    var GPA = elt.GPA.value;
    
    
    if (ID == "" || LName == "" ||FName == ""||Major == "" ||GPA == ""){
        alert("Please fill in all Textboxes");
       // break; //CHECK IF THIS STOPS PHP CODE FROM RUNNING
    }
   
   }


</script>

<a href="./menu.html"> Return To Menu</a>

</body>
</html>