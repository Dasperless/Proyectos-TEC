/**
 * Clase Persona
 * Contiene información de una persona
 * @author POO
 * @version 1.0
 */
public class Persona {
 
    //Constantes
    /**
     * Sexo por defecto
     */
    private final static char SEXO_DEF = 'H';
 

    //Atributos
    /**
     * Nombre de la persona
     */
    private String nombre;
 
    /**
     * Edad de la persona
     */
 
    /**
     * Cedula de la persona, se genera al construir el objeto
     */
    private String cedula;
 
    /**
     * Sexo de la persona, H hombre M mujer
     */
    private char sexo;
 
    /**
     * Peso de la persona
     */
    private double peso;
 
    /**
     * Altura de la persona
     */
    private double altura;
 
    //Contructores
    /**
     * Constructor por defecto
     */
    public Persona() {
        this("", 0, SEXO_DEF, 0, 0);
    }
 
    /**
     * Constructor con 3 parametros
     *
     * @param nombre de la persona
     * @param edad de la persona
     * @param sexo de la persona
     */
    public Persona(String nombre, int edad, char sexo) {
        this(nombre, edad, sexo, 0, 0);
    }
 
    /**
     * Constructor con 5 parametros
     *
     * @param nombre de la persona
     * @param edad de la persona
     * @param sexo de la persona
     * @param peso de la persona
     * @param altura de la persona
     */
    public Persona(String nombre, int edad, char sexo, double peso, double altura) {
        this.nombre = nombre;
        this.peso = peso;
        this.altura = altura;
        this.sexo = sexo;
        comprobarSexo();
    }
 
    //Métodos privados
    private void comprobarSexo() {
 
        //Si el sexo no es una H o una M, por defecto es H
        if (sexo != 'H' && sexo != 'M') {
            this.sexo = SEXO_DEF;
        }
    }
 
 
    //Métodos publicos
    /**
     * Modifica el nombre de la persona
     *
     * @param nombre a cambiar
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
 

    /**
     * Modifica el sexo de la persona, comprueba que es correcto
     *
     * @param sexo a cambiar
     */
    public void setSexo(char sexo) {
        this.sexo = sexo;
    }
 
    /**
     * Modifica el peso de la persona
     *
     * @param peso a cambiar
     */
    public void setPeso(double peso) {
        this.peso = peso;
    }
 
    /**
     * Modifica la altura de la persona
     *
     * @param altura a cambiar
     */
    public void setAltura(double altura) {
        this.altura = altura;
    }
 
    /**
     * Devuelve informacion del objeto
     *
     * @return cadena con toda la informacion
     */
    @Override
    public String toString() {
        String sexo;
        if (this.sexo == 'H') {
            sexo = "Hombre";
        } else {
            sexo = "Mujer";
        }
        return "Informacion de la persona:\n"
                + "Nombre: " + nombre + "\n"
                + "Sexo: " + sexo + "\n"
                + "Cedula: " + cedula + "\n"
                + "Peso: " + peso + " kg\n"
                + "Altura: " + altura + " metros\n";
    }
 
}