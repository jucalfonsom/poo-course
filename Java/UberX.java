class UberX extends Car {
    // Attributes
    String brand;
    String model;

    // Constructor
    public UberX(String license, Account driver, String brand, String model){
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
}