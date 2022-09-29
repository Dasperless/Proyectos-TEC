package modelo;

/**
 * Clase Persona Contiene nombre, apellido,
 *
 * @author G3
 * @version 1.0
 */
public class Persona {

//Creacion de atributos
    /**
     * Crea el atributo de nombre de tipo String
     */
    String nombre;
    /**
     * Crea el atributo de apellido de tipo String
     */
    String imagen;
    /**
     * Crea el atributo de imagenAtq de tipo String
     */
    String imagenAtq;

    /**
     *
     * @param pNombre
     */
    public Persona(String pNombre, String pImagen, String pImagenAtq) {
        this.nombre = pNombre;
        this.imagen = pImagen;
        this.imagenAtq = pImagenAtq;
    }

    /**
     *
     */
    public Persona() {

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
     * Funcion que devuelve el atributo imagen de tipo String
     *
     * @return imagen
     */
    public String getImagen() {
        return imagen;
    }

    /**
     * Funcion que modifica el atributo imagen de tipo String
     *
     * @param pImagen Un String con la dirección absoluta de la imagen
     */
    public void setImagen(String pImagen) {
        this.imagen = pImagen;
    }

    /**
     * Funcion que devuelve el atributo imagenAtq de tipo String
     *
     * @return imagen
     */
    public String getImagenAtq() {
        return imagenAtq;
    }

    /**
     * Funcion que modifica el atributo imagenAtq de tipo String
     *
     * @param pImagenAtq
     */
    public void setImagenAtq(String pImagenAtq) {
        imagenAtq = pImagenAtq;
    }
}
