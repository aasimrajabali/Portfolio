<?php

if(isset($_POST['viewAll'])) {




$myfile = fopen("/u/z/users/cs329e-fa15/aasim612/password_info.txt", "r") or die("Unable to open file!");
$pwd = fgets($myfile);
$pwd = trim($pwd);
fclose($myfile);


// Connect to the MySQL database
$host = "fall-2015.cs.utexas.edu";
$user = "aasim612";
$dbs = "cs329e_aasim612";
$port = "3306";

$connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);

if (empty($connect))
{
  die("mysqli_connect failed: " . mysqli_connect_error());
}

// Get data from a table in the database and print it out

$table = "STUDENTS";


$result = mysqli_query($connect, "SELECT * from $table ORDER BY LAST, FIRST");


print("<table border=\"1\">");
print("<tr><td>ID</td>");
print("<td>Last Name</td>");
print("<td>First Name</td></tr>");

while ($row = $result->fetch_row())
{
print  "<tr><td>" .  $row[0] . "</td>";
print  "<td>" .  $row[1] . "</td>";
print  "<td>" .  $row[2] . "</td></tr>";
}
print("</table>");
$result->free();

// Close connection to the database
mysqli_close($connect);
}
if(isset($_POST['viewSelected'])) {


$myfile = fopen("/u/z/users/cs329e-fa15/aasim612/password_info.txt", "r") or die("Unable to open file!");
$pwd = fgets($myfile);
$pwd = trim($pwd);
fclose($myfile);


// Connect to the MySQL database
$host = "fall-2015.cs.utexas.edu";
$user = "aasim612";
$dbs = "cs329e_aasim612";
$port = "3306";

$connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);

if (empty($connect))
{
  die("mysqli_connect failed: " . mysqli_connect_error());
}

// Get data from a table in the database and print it out

$table = "STUDENTS";

$ID = $_POST["ID"];
$LName = $_POST["LName"];
$FName = $_POST["FName"];
$Major = $_POST["Major"];
$GPA = $_POST["GPA"];


if($ID != ""){
        $sql = "SELECT * from " . $table . " WHERE ID = " . $ID;
    $result = mysqli_query($connect, $sql);
}
else{
        if($FName != "" && $LName != ""){
        $sql = "SELECT * from " . $table . " WHERE LAST =  '" . $LName . "' AND FIRST = '" . $FName . "'";
        $result = mysqli_query($connect, $sql);
        }
        elseif($FName != ""){
        $sql = "SELECT * from " . $table . " WHERE FIRST = '" . $FName . "'";
        $result = mysqli_query($connect, $sql);
        }
        elseif(LName != ""){
        $sql = "SELECT * from " . $table . " WHERE LAST = '" . $LName . "'";
        $result = mysqli_query($connect, $sql);
        }
}


print("<table border=\"1\">");
print("<tr><td>ID</td>");
print("<td>Last Name</td>");
print("<td>First Name</td></tr>");

while ($row = $result->fetch_row())
{
print  "<tr><td>" .  $row[0] . "</td>";
print  "<td>" .  $row[1] . "</td>";
print  "<td>" .  $row[2] . "</td></tr>";
}
print("</table>");
$result->free();

// Close connection to the database
mysqli_close($connect);

}


?>

<html>
<head>
<title>Students Database View</title>
</head>
<body>

<h2>View</h2>

<form id= "view" method = "post" action = "<?php echo $_SERVER['PHP_SELF']; ?>" >
<h3> Enter the ID of the record you want to Search</h3>
<table width = "35%" border = "1">
<tr>
<td>ID</td>
<td> <input type = "text" name = "ID" size = "45" /></td>
</tr>
</table>
<br>
<h3> Enter the Last Name and/or First Name of the record you want to search</h3>
<table width = "35%" border = "1">
<tr>
<td>Last Name</td>
<td> <input type = "text" name = "LName" size = "45" /></td>
</tr>
<tr>
<td>First Name</td>
<td> <input type = "text" name = "FName" size = "45" /></td>
</tr>
</table>
<br>
<h3> Enter the Last Name and/or First Name of the record you want to search</h3>
<table width = "35%" border = "1">
<tr>
<td>Last Name</td>
<td> <input type = "text" name = "LName" size = "45" /></td>
</tr>
<tr>
<td>First Name</td>
<td> <input type = "text" name = "FName" size = "45" /></td>
</tr>
</table>
<input type = "submit" value = "Submit" name = "viewSelected"/>
<br>
<br>
<br>
<h3>Search all</h3>
<input type = "submit" value = "Submit" name = "viewAll"/>
</form>
</script>


<a href="./menu.html"> Return To Menu</a>

</body>
</html>