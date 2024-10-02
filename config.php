<?php
// Database connection parameters
$servername = "localhost:3308"; // Host name with port
$username = "root";               // Default XAMPP username
$password = "";                   // Default XAMPP password (usually blank)
$dbname = "feedback";             // Database name

// Create connection
$con = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$con) {
    die("Connection failed: " . mysqli_connect_error());
}

// Optional: Set character set to UTF-8 for proper encoding
mysqli_set_charset($con, "utf8");
?>
