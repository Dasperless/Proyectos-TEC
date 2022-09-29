package modelo;

/**
 * Clase AntiHeroe Contiene nombre, archienemigo
 *
 * @author G3
 * @version 1.0
 */
public class AntiHeroe extends Persona {

//Creacion de atributos
    /**
     * Crea el atributo de nombre antiheroe de tipo String
     */
    private String nombreAntiHeroe;

    /**
     * Crea el atributo de archienemigo de tipo String
     */
    private String archienemigo;

    /**
     * Funcion que devuelve el atributo nombre antiheroe de tipo String
     *
     * @return nombreHeroe
     */
    public String getNombreAntiHeroe() {
        return nombreAntiHeroe;
    }

    /**
     * Funcion que devuelve el atributo archienemigo de tipo String
     *
     * @return archienemigo
     */
    public String getArchienemigo() {
        return archienemigo;
    }

    /**
     * Funcion que modifica el atributo nombre antiheroe de tipo String y recibe
     * como parametro un pNombre
     *
     * @param pNombre
     */
    public void setNombreAntiHeroe(String pNombre) {
        this.nombreAntiHeroe = pNombre;
    }

    /**
     * Funcion que modifica el atributo archienemigo de tipo String y recibe
     * como parametro un pCiudad
     *
     * @param pCiudad
     */
    public void setArchienemigo(String pCiudad) {
        this.archienemigo = pCiudad;
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

    /**
     *Constructor de la clase AntiHeroe.
     * @param nombreAntiHeroe El nombre del antiheroe.
     * @param pIdetidadSecreta La identidad secreta del antiheroe.
     * @param pArchienemigo El archienemigo del antiheroe.
     * @param pImagen La imagen del antiheroe
     * @param pImagenAtq La imagen de ataque del antiheroe.
     */
    public AntiHeroe( String pIdetidadSecreta,String nombreAntiHeroe, String pArchienemigo, String pImagen, String pImagenAtq) {
        super(pIdetidadSecreta, pImagen, pImagenAtq);
        this.nombreAntiHeroe = nombreAntiHeroe;
        this.archienemigo = pArchienemigo;
    }

    /**
     *
     */
    public AntiHeroe() {

    }

}
