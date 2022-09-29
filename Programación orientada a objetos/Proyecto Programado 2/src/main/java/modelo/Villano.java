package modelo;

/**
 * Clase Villano Contiene nombre, ciudad, tipo
 *
 * @author G3
 * @version 1.0
 */
public class Villano extends Persona {

//Creacion de atributos
    /**
     * Crea el atributo de nombre villano de tipo String
     */
    private String nombreVillano;

    /**
     * Crea el atributo de Tipo de tipo String
     */
    public String tipo;

    /**
     * Funcion que devuelve el atributo nombre villano de tipo String
     *
     * @return nombreVillano
     */
    public String getNombreVillano() {
        return nombreVillano;
    }

    /**
     * Funcion que devuelve el atributo tipo de tipo String
     *
     * @return Tipo
     */
    public String getTipo() {
        return tipo;
    }

    /**
     * Funcion que modifica el atributo nombre villano de tipo String y recibe
     * como parametro un pNombre
     *
     * @param pNombre
     */
    public void setNombreVillano(String pNombre) {
        this.nombreVillano = pNombre;
    }


    /**
     * Funcion que modifica el atributo Tipo de tipo String y recibe como
     * parametro un pTipo
     *
     * @param pTipo
     */
    public void setTipo(String pTipo) {
        this.tipo = pTipo;
    }

//Creacion de metodos
    /**
     * Funcion que devuelve el atributo nombre de tipo String
     *
     * @return nombre
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * Funcion que modifica el atributo nombre de tipo String y recibe como
     * parametro un pNombre
     *
     * @param pNombre
     */
    public void setNombre(String pNombre) {
        this.nombre = pNombre;
    }

    public Villano(String pNombre,String nombreVillano, String tipo, String pImagen, String pImagenAtq) {
        super(pNombre, pImagen, pImagenAtq);
        this.nombreVillano = nombreVillano;
        this.tipo = tipo;
    }
    
    /**
     *
     */
    public Villano(){
        
    }

}
