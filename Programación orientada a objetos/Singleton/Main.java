public class Main {

    public static void main(String[] args) {
        
        Singleton tony = Singleton.getSingletonInstance("Tony Stark");
        Singleton steve = Singleton.getSingletonInstance("Steve Rogers");
        
        // ricardo y steve son referencias a un único objeto de la clase Singleton
        System.out.println(steve.getNombre());
        System.out.println(tony.getNombre());   
    }
}