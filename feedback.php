<?php 
ob_start(); 
require 'config.php'; // Include database connection

// Fetching POST data
$view = $_POST['view']; // Service satisfaction
$name = $_POST['name']; // User's name
$comments = $_POST['comments']; // User's comments
$email = $_POST['email']; // User's email
$num = $_POST['num']; // User's phone number

// Prepare and bind the SQL statement
$stmt = $con->prepare("INSERT INTO `poll` (`name`, `email`, `phone`, `feedback`, `suggestions`) VALUES (?, ?, ?, ?, ?)");
$stmt->bind_param("sssss", $name, $email, $num, $view, $comments);

// Execute the statement and check for success
if ($stmt->execute()) {
    echo '<script>alert("Thank You..! Your Feedback is Valuable to Us"); location.replace(document.referrer);</script>';
} else {
    die("Error: " . $stmt->error); // Display error if the query fails
}

$stmt->close(); // Close the prepared statement
mysqli_close($con); // Close the database connection
ob_end_flush(); // End output buffering
?>
