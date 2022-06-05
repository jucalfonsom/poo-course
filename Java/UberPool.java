class UberPool extends Car {
    // Attributes
    String brand;
    String model;

    // Constructor
    public UberPool(String license, Account driver, String brand, String model){
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
}