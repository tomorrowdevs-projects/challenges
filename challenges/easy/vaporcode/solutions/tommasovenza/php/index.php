<?php
function vaporwave($initial_string) {
    $string = '';

    for ($i=0; $i < strlen($initial_string); $i++) { 
        $string .= $initial_string[$i] . ' ';
    }
    $result = strtoupper($string);
    // remove last space
    return substr($result, 0, -1);
}

var_dump(vaporwave('I love javascript!'));