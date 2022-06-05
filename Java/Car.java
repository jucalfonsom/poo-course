class Car {
    // Attributes
    Integer id;
    String license;
    Account driver;
    Integer passenger;

    // Constructor
    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;
    }

    // Methods
    void printDataCar(){
        System.out.println("License: " + license + "Name driver: "+ driver.name);
    }
}