<?php

require_once('./Account.php');

class Car 
{
    public $id;
    public $license;
    public $driver;
    public $passengers;

    public function __construct($license, $driver) {
        $this->license = $license;
        $this->driver = $driver;
    }

    public function PrintDataCar(){
        print 'License: '.$this->license;
        print 'Driver: '.$this->driver->name;
    }
}
?>