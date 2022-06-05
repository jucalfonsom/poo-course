<?php
class Payment 
{
    public $id = integer;

    public function __construct($id) {
        $this->id = $id;
    }
}
?>