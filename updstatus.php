<?php
$updater = file_get_contents("https://raw.githubusercontent.com/UXR7b/status/master/status.py");
$file = fopen("status.py", "w");
fwrite($file, $updater);
fclose($file);
echo "v1.1";
?>
