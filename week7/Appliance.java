public abstract class Appliance {

    protected String brand;

    public Appliance(String brand) {
        this.brand = brand;
    }

    public void displayBrand() {
        System.out.println("Brand: " + brand);
    }

    public void turnOn() {
        System.out.println("Power ON");
    }

    public void turnOff() {
        System.out.println("Power OFF");
    }

    public abstract void displayStatus();

    public static class main {
        public static void main(String[] args) {
            WashingMachine wm = new WashingMachine("LG");
            Refrigerator rf = new Refrigerator("Panasonic");
            
            wm.displayBrand();
            wm.turnOn();
            wm.displayStatus();
            wm.turnOff();
            
            System.out.println();
            
            rf.displayBrand();
            rf.turnOn();
            rf.displayStatus();
            rf.turnOff();
        }
    }
}