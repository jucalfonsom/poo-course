import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    // Attributes
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;

    // Constructor
    public UberVan(String license, Account driver, String brand, String model,
    Map<String, ArrayList<String,Integer>> typeCarAccepted,
    ArrayList<String> seatsMaterial;){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
}