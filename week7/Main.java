public class Main {
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