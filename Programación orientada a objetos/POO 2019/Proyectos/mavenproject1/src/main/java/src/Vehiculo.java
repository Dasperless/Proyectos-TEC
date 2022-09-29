
/**
 * Clase Vehiculo
 * Contiene marca y modelo
 *
 * @author Paula Rubio
 * @version 1.0
 */
public class Vehiculo {

    //Atributos
    /**
     * Modelo del vehiculo
     */
    private Modelo modelo;
    /**
     * Marca del vehiculo
     */
    private String marca;

    /**
     * Año
     */
    private int año;

    /**
     * Placa
     */
    private String Placa;

    /**
     * Devuelve la marca
     *
     * @return marca
     */
    public String getMarca() {
        return marca;
    }

    /**
     * Devuelve el modelo
     *
     * @return modelo
     */
    public Modelo getModelo() {
        return modelo;
    }

    /**
     * Devuelve el año
     *
     * @return año
     */
    public int getAño() {
        return año;
    }

    /**
     * Devuelve la placa
     *
     * @return placa
     */
    public String getPLaca() {
        return Placa;
    }

    /**
     * Modifica la marca
     *
     * @param marca a cambiar
     */
    public void setMarca(String marca) {
        this.marca = marca;
    }

    /**
     * Modifica el modelo
     *
     * @param modelo a cambiar
     */
    public void setModelo(Modelo modelo) {
        this.modelo = modelo;
    }

    /**
     * Modifica la placa
     *
     * @param placa a cambiar
     */
    public void setPlaca(String placa) {
        this.Placa = placa;
    }

    /**
     * Modifica el año
     *
     * @param año a cambiar
     */
    public void setMarca(int año) {
        this.año = año;
    }

    /**
     * Constructor del vehiculo
     *
     * @param marca, modelo
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
