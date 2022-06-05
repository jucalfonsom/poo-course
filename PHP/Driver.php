<?php

class Driver extends Account {
    public $id;
    public $email;
    public $password;

    public function __construct($name, $document, $id, $email, $password) {
        parent::__construct($name, $document);
        $this->id = $id;
        $this->email = $email;
        $this->password = $password;
    }
}

?>