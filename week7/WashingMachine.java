public class WashingMachine extends Appliance {
    
    public WashingMachine(String brand) {
        super(brand);
    }
    
    public void displayStatus() {
        System.out.println("Washing clothes...");
    }
}