package src;

/**
 * Clase Vehiculo Contiene marca y modelo
 *
 * @author Maria Paula
 * @version 1.0
 */
public class Vehiculo {

//Atributos
    /**
     * Modelo del vehiculo
     */
    private Modelo modelo;

    /**
     * String con la marca del vehiculo.
     */
    private String marca;

    /**
     * Valor entero con el año del vehiculo.
     */
    private int año;

    /**
     * String con la placa del vehiculo.
     */
    private String Placa;

// Métodos.
    /**
     * Devuelve la marca del vehiculo.
     *
     * @return marca
     */
    public String getMarca() {
        return marca;
    }

    /**
     * Devuelve el modelo del vehiculo.
     *
     * @return modelo
     */
    public Modelo getModelo() {
        return modelo;
    }

    /**
     * Devuelve el año.
     *
     * @return año
     */
    public int getAño() {
        return año;
    }

    /**
     * Devuelve la placa del vehiculo.
     *
     * @return placa
     */
    public String getPLaca() {
        return Placa;
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
     * Modifica el modelo
     *
     * @param modelo
     */
    public void setModelo(Modelo modelo) {
        this.modelo = modelo;
    }

    /**
     * Modifica la placa del vehiculo.
     *
     * @param placa
     */
    public void setPlaca(String placa) {
        this.Placa = placa;
    }

    /**
     * Modifica el año.
     *
     * @param año
     */
    public void setMarca(int año) {
        this.año = año;
    }

    @Override
    public String toString() {
        String msj = "********* Información del vehiculo *********\n";
        msj += modelo.toString();
        msj += "Marca: " + marca + "\n";
        msj += "Año: " + año + "\n";
        msj += "Placa: " + Placa + "\n";

        return msj;
    }

    /**
     * Constructor del vehiculo
     *
     * @param marca
     * @param modelo
     * @param año
     * @param placa
     */
    public Vehiculo(String marca, Modelo modelo, int año, String placa) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.Placa = placa;

    }
}
