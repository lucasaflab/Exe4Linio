<?php

use PHPUnit\Framework\TestCase;

class Pruebas extends TestCase
{
  public function testOne()
      {
        include_once 'ex01.php';
        $this->assertSame(ex(1,2),1);
        $this->assertSame(ex(3,4),"Linio");
        $this->assertSame(ex(5,6),"IT");
        $this->assertSame(ex(15,16),"Linianos");
        $this->assertNotNull(ex(1,101));
      }
}

?>
