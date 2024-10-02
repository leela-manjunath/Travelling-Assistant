<?php
require 'config.php'; // Include the config file

// Test the connection
if ($con) {
    echo "Connected successfully to the database!";
} else {
    echo "Connection failed!";
}

// Close the connection
mysqli_close($con);
?>
