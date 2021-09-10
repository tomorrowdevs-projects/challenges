<?php
function vaporwave($string) {
  $string = str_replace(" ", "", $string);
  $string = implode(" ",str_split($string));
  $string = strtoupper($string);
  echo $string;
}

vaporwave("Hello, World!");
?>
