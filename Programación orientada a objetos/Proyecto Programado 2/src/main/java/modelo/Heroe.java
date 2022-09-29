package modelo;

/**
 * Clase Heroe Contiene nombre, ciudad
 *
 * @author G3
 * @version 1.0
 */
public class Heroe extends Persona {

//Creacion de atributos
    /**
     * Crea el atributo de nombre heroe de tipo String
     */
    private String nombreHeroe;
    
    /**
     * Crea el atributo de archienemigo de heroe de tipo String
     */
    private String archienemigo;

    /**
     * Funcion que devuelve el atributo archienemigo heroe de tipo String
     *
     * @return nombreHeroe
     */
    public String getArchienemigo() {
        return archienemigo;
    }

    /**
     * Funcion que modifica el atributo archienemigo heroe de tipo String
     *
     * @param archienemigo
     */
    public void setArchienemigo(String archienemigo) {
        this.archienemigo = archienemigo;
    }

    /**
     * Funcion que devuelve el atributo nombre heroe de tipo String
     *
     * @return nombreHeroe
     */
    public String getNombreHeroe() {
        return nombreHeroe;
    }

    /**
     * Funcion que modifica el atributo nombre heroe de tipo String y recibe
     * como parametro un pNombre
     *
     * @param pNombre
     */
    public void setNombreHeroe(String pNombre) {
        this.nombreHeroe = pNombre;
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
     *Constructor para de la clase heroe.
     * @param pIdentidadSecreta La identidad secreta del heroe
     * @param pArchienemigo El archienemigo del heroe.
     * @param pImagen La imagen del heroe
     * @param pImagenAtq La imagen de ataque del heroe.
     * @param pNombreHeroe El nombre del heroe.
     */
    public Heroe(String pIdentidadSecreta, String pNombreHeroe, String pArchienemigo, String pImagen, String pImagenAtq) {
        super(pIdentidadSecreta, pImagen, pImagenAtq);
        this.archienemigo = pArchienemigo;
        this.nombreHeroe = pNombreHeroe;
    }

    /**
     *
     */
    public Heroe() {

    }
}
