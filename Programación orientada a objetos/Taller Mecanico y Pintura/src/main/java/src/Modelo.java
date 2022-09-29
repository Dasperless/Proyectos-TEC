package src;

/**
 * Clase Modelo Contiene descripcion de modelo, marca, cantidad de asientos,
 * cantidad de puertas, combustible, transmision.
 *
 * @author Darío Vargas
 * @version 1.0
 */
public class Modelo {

//Atributos
    /**
     * String con la descripcion del modelo.
     */
    private String descripModelo;

    /**
     * String con la marca del vehiculo.
     */
    private String marca;

    /**
     * Valor entero con la cantidad de asientos del vehiculo.
     */
    private int cantidadAsientos;

    /**
     * Valor entero con la cantidad de puertas del vehiculo.
     */
    private int cantidadPuertas;

    /**
     * String con el tipo de combustible que utiliza.
     */
    private String combustible;

    /**
     * String con la transmision del vehiculo.
     */
    private String transmision;

    /**
     * Constructor de la clase
     *
     * @param descripModelo
     * @param marca
     * @param cantidadAsientos
     * @param cantidadPuertas
     * @param combustible
     * @param transmision
     */
    public Modelo(String descripModelo, String marca, int cantidadAsientos, int cantidadPuertas, String combustible, String transmision) {
        this.descripModelo = descripModelo;
        this.marca = marca;
        this.cantidadAsientos = cantidadAsientos;
        this.cantidadPuertas = cantidadPuertas;
        this.combustible = combustible;
        this.transmision = transmision;
    }

// Metodos
    /**
     * Devuelve un String con la descripcion del modelo
     *
     * @return descripModelo
     */
    public String getDescripModelo() {
        return descripModelo;
    }

    /**
     * Modifica la descripcion del modelo
     *
     * @param descripModelo
     */
    public void setDescripModelo(String descripModelo) {
        this.descripModelo = descripModelo;
    }

    /**
     * Devuelve un String con la marca del vehiculo.
     *
     * @return marca
     */
    public String getMarca() {
        return marca;
    }

    /**
     * Modifica la marca del vehiculo.
     *
     * @param marca
     */
    public void setMarca(String marca) {
        this.marca = marca;
    }

    /**
     * Devuelve un entero con la cantidad de asientos del vehiculo.
     *
     * @return cantidadAsientos
     */
    public int getCantidadAsientos() {
        return cantidadAsientos;
    }

    /**
     * Modifica la cantidad de asientos del vehiculo.
     *
     * @param cantidadAsientos
     */
    public void setCantidadAsientos(int cantidadAsientos) {
        this.cantidadAsientos = cantidadAsientos;
    }

    /**
     * Devuelve un entero con la cantidad de puertas del vehiculo.
     *
     * @return cantidadPuertas
     */
    public int getCantidadPuertas() {
        return cantidadPuertas;
    }

    /**
     * Modifica la cantidad de puertas del vehiculo.
     *
     * @param cantidadPuertas
     */
    public void setCantidadPuertas(int cantidadPuertas) {
        this.cantidadPuertas = cantidadPuertas;
    }

    /**
     * Devuelve un String con el tipo de combustible del vehiculo.
     *
     * @return combustible
     */
    public String getCombustible() {
        return combustible;
    }

    /**
     * Modifica el tipo de combustible del vehiculo.
     *
     * @param combustible
     */
    public void setCombustible(String combustible) {
        this.combustible = combustible;
    }

    /**
     * Devuelve un String con el tipo de transmision del vehiculo.
     *
     * @return transmision
     */
    public String getTransmision() {
        return transmision;
    }

    /**
     * Devuelve un String con la información del modelo.
     *
     * @return msj
     */
    @Override
    public String toString() {
        String msj = "";
        msj += "\n[Información del modelo]:\n";
        msj += "Descripción del modelo: " + descripModelo + "\n";
        msj += "Marca: " + marca + "\n";
        msj += "Cantidad de asientos: " + cantidadAsientos + "\n";
        msj += "Cantidad de puertas: " + cantidadPuertas + "\n";
        msj += "Combustible: " + combustible + "\n";
        msj += "Transmisión: " + transmision + "\n\n";
        return msj;
    }

    /**
     * Modifica el tipo de transmision
     *
     * @param transmision
     */
    public void setTransmision(String transmision) {
        this.transmision = transmision;
    }

}
