<?php

function ex($ini,$fin){

  for ($i=$ini; $i < $fin; $i++) {
    if ($i%3==0 and $i%5==0) {$res="Linianos";}
    elseif($i%3==0){$res="Linio";}
    elseif ($i%5==0){$res="IT";}
    else {$res=$i;}
    echo "$res\n";
  }
  return $res;

}

$ini=1;
$fin=101;


// ex($ini,$fin);

?>
