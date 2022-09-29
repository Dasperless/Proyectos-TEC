import java.util.Locale;
import java.util.Scanner;
import javax.swing.JOptionPane;
 
public class PersonaApp_Scanner {
 
    public static void main(String[] args) {
 
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("\n");
        sc.useLocale(Locale.US);
         
        //Introducimos los datos
        System.out.println("Introduce el nombre");
        String nombre = sc.next();
  
        System.out.println("Introduce el sexo");
        char sexo = sc.next().charAt(0);
 
        System.out.println("Introduce el peso");
        double peso = sc.nextDouble();
 
        System.out.println("Introduce la altura");
        double altura = sc.nextDouble();
 
        //Creamos objetos con cada constructor
        Persona persona1 = new Persona();
        Persona persona2 = new Persona(nombre, 0, sexo);
        Persona persona3 = new Persona(nombre, 0, sexo, peso, altura);
 
        //Los datos que no esten completos los insertamos con los metodos set
        persona1.setNombre("Sin nombre");
        persona1.setSexo('M');
        persona1.setPeso(0);
        persona1.setAltura(1);
 
        //Usamos metodos para realizar la misma accion para cada objeto
        System.out.println("Persona1");
        System.out.println(persona1.toString());
 
        System.out.println("Persona2");
        System.out.println(persona2.toString());
 
        System.out.println("Persona3");
        System.out.println(persona3.toString());
    }
 
}