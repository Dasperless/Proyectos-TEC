
/**
 *
 * @author Darío Vargas
 */
public class Modelo {
    //Variables
    private String descripModelo;//La descripcion del modelo.
    private String marca;//La marca del modelo.
    private int cantidadAsientos;//La cantidad de asientos del modelo.
    private int cantidadPuertas;//La cantidad de puertas del modelo. 
    private String combustible;//El combustible que usa el modelo.
    private String transmision;//La transmision del modelo

    public Modelo(String descripModelo, String marca, int cantidadAsientos, int cantidadPuertas, String combustible, String transmision) {
        this.descripModelo = descripModelo;
        this.marca = marca;
        this.cantidadAsientos = cantidadAsientos;
        this.cantidadPuertas = cantidadPuertas;
        this.combustible = combustible;
        this.transmision = transmision;
    }
    
    //Getters y Setters 
    public String getDescripModelo() {
        return descripModelo;
    }

    public void setDescripModelo(String descripModelo) {
        this.descripModelo = descripModelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getCantidadAsientos() {
        return cantidadAsientos;
    }

    public void setCantidadAsientos(int cantidadAsientos) {
        this.cantidadAsientos = cantidadAsientos;
    }

    public int getCantidadPuertas() {
        return cantidadPuertas;
    }

    public void setCantidadPuertas(int cantidadPuertas) {
        this.cantidadPuertas = cantidadPuertas;
    }

    public String getCombustible() {
        return combustible;
    }

    public void setCombustible(String combustible) {
        this.combustible = combustible;
    }

    public String getTransmision() {
        return transmision;
    }

    public void setTransmision(String transmision) {
        this.transmision = transmision;
    }
    
}
