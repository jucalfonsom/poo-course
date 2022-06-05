class Driver extends Account {
    constructor(name, document, id, email, password){
        super(name, document);
        this.id = id;
        this.email = email;
        this.password = password;
    }
}