<?php
$filename = 'lock_status.txt';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Serve the current status
    if (file_exists($filename)) {
        echo file_get_contents($filename);
    } else {
        echo 'unlocked';
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Update the status
    $input = file_get_contents('php://input');
    if (in_array($input, ['locked', 'unlocked'])) {
        file_put_contents($filename, $input);
        echo 'Status updated';
    } else {
        http_response_code(400);
        echo 'Invalid status';
    }
}
?>
