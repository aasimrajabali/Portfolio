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


$sql = "Delete From " . $table . " WHERE ID = " . $ID;
print($sql);
if ($mysqli->query($sql) === TRUE) {
    echo "Record Deleted successfully";
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

<h2>Delete Record</h2>


<form id= "delete" method = "post" action = "<?php echo $_SERVER['PHP_SELF']; ?>" >
<h3> Enter the ID of the record you want to update</h3>
<table width = "35%" border = "1">
<tr>
<td>ID</td>
<td> <input type = "text" name = "ID" size = "45" /></td>
</tr>
</table>
<input type = "submit" value = "Submit" name = "Submit"/>
<input type = "reset" value = "Reset" />
</form>
<script type="text/javascript">
  document.getElementById("delete").Submit.onclick = checkText;
  
   function checkText(){
    var elt = document.getElementById("delete");
    var ID = elt.ID.value;

    
    
    if(ID == ""){
        alert("Please fill in ID");
       // break; //CHECK IF THIS STOPS PHP CODE FROM RUNNING
    }
    
   
   }


</script>
<a href="./menu.html"> Return To Menu</a>

</body>
</html>