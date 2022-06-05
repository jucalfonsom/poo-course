class User extends Account {
    // Attributes
    Integer id;
    String email;
    String password;

    // Constructor
    public User(String name, String document, Integer id, String email, String password){
        super(name, document);
        this.id = id;
        this.email = email;
        this.password = password;
    }
}