<?php
if(isset($_POST['Submit'])) {
extract ($_POST);

$loginUser = $_POST["loginUser"];
$loginPassword = $_POST["loginPassword"];

$myfile = fopen("./passwd.txt", "r") or die("Unable to open file!");
$fileinfo =  fread($myfile,filesize("./passwd.txt"));
fclose($myfile);

$pieces = explode(PHP_EOL,$fileinfo);
$success = False;

for ($i = 0; $i < count($pieces); $i++) {
  $varSplit = explode(":", $pieces[$i]);
  $textUser = $varSplit[0];
  $textPass = $varSplit[1];
     if (($loginUser == $textUser) && ($loginPassword == $textPass)){
                        $success = True;
                        break;
      }
 }
if ($success == True) {
        print<<<SUCCESS
        <script type='text/javascript'>window.alert("Login Successful.");</script>
SUCCESS;
                
}
else {
        print<<<ERROR
                <script type='text/javascript'>window.alert("Password and Username Incorrect.");</script>
ERROR;

}

}


?>

<html>
<head>
<title>Students Database Login </title>
</head>
<body>

<h2>Login</h2>

<table width = "35%" border = "1">
<form method = "post" action = "<?php echo $_SERVER['PHP_SELF']; ?>">
<tr>
<td> Enter name </td>
<td> <input type = "text" name = "loginUser" size = "45" /></td>
</tr>
<tr>
<td> Password </td>
<td> <input type = "password" name = "loginPassword" size = "45" /></td>
</tr>
</table>
<input type = "submit" value = "Submit" name="Submit" />
<input type = "reset" value = "Reset" />
</form>
</body>
</html>