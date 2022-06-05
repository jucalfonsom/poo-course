class Car {
    // Attributes
    Integer id;
    String license;
    Account driver;
    private Integer passenger;

    // Constructor
    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;
        passenger = 4;
        System.out.println("Passenger: "+ passenger)
    }

    // Methods
    void printDataCar(){
        if(passenger != null){
            System.out.println("License: " + license + "Name driver: "+ driver.name + "Passengers: " + passenger);
        }
    }

    // Getters Getters
    public Integer getPassenger(){
        return passenger;
    }

    //Setters
    public void setPassenger(Integer passenger){
        if(passenger == 4){
            this.passenger = passenger;
        }else{
            System.out.println("You need to assign four passengers")
        } 
    }
}