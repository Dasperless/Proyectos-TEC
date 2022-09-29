
import java.util.Date;

/**
 * Clase MecanicaGeneral Contiene descripcion del trabajo, estado, cedula
 * cliente, placa veh, descripcion veh, descripcion problema, costo, fecha
 * recibido, fecha posible entrega.
 *
 * @author Paula Rubio
 * @version 1.0
 */
public class MecanicaGeneral {

//Atributos
    /**
     * Descripcion del trabajo
     */
    private String desTrabajo;

    /**
     * Estado
     */
    private String estado;

    /**
     * cedula cliente
     */
    private int cedCliente;

    /**
     * Placa vehiculo
     */
    private String placaVeh;

    /**
     * Descripcion vehiculo
     */
    private String desVehiculo;

    /**
     * Descripcion problema
     */
    private String desProblema;

    /**
     * Costo
     */
    private int costo;

    /**
     * Fecha recibido
     */
    private Date fechaRec;

    /**
     * Fecha de posible entrega
     */
    private Date fechaEnt;

//Metodos
    /**
     * Devuelve la descripcion del trabajo
     *
     * @return desTrabajo
     */
    public String getDescripcionTrabajo() {
        return desTrabajo;
    }

    /**
     * Devuelve el estado
     *
     * @return estado
     */
    public String getEstado() {
        return estado;
    }

    /**
     * Devuelve la cedula del cliente
     *
     * @return cedCliente
     */
    public int getCedulaCliente() {
        return cedCliente;
    }

    /**
     * Devuelve la placa del vehiculo
     *
     * @return placaVeh
     */
    public String getPlacaVehiculo() {
        return placaVeh;
    }

    /**
     * Devuelve la descripcion del vehiculo
     *
     * @return desVehiculo
     */
    public String getDescripcionVehiculo() {
        return desVehiculo;
    }

    /**
     * Devuelve la descripcion del problema
     *
     * @return desProblema
     */
    public String getDescripcionProblema() {
        return desProblema;
    }

    /**
     * Devuelve el costo del trabajo
     *
     * @return costo
     */
    public int getCosto() {
        return costo;
    }

    /**
     * Devuelve la fecha de recibido
     *
     * @return fechaRec
     */
    public Date getFechaRecibido() {
        return fechaRec;
    }

    /**
     * Devuelve la fecha de posible entrega
     *
     * @return fechaEnt
     */
    public Date getFechaEntrega() {
        return fechaEnt;
    }

    /**
     * Modifica la descripcion del trabajo
     *
     * @param Descripcion a cambiar
     */
    public void setDescripcionTrabajo(String Descripcion) {
        this.desTrabajo = Descripcion;
    }

    /**
     * Modifica la descripcion del Vehiculo
     *
     * @param Descripcion a cambiar
     */
    public void setDescripcionVehiculo(String Descripcion) {
        this.desVehiculo = Descripcion;
    }

    /**
     * Modifica la descripcion del problema
     *
     * @param Descripcion a cambiar
     */
    public void setDescripcionProblema(String Descripcion) {
        this.desProblema = Descripcion;
    }

    /**
     * Modifica el estado
     *
     * @param Estado a cambiar
     */
    public void setEstado(String Estado) {
        this.estado = Estado;
    }

    /**
     * Modifica la cedula del cliente
     *
     * @param Cedula a cambiar
     */
    public void setCedulaCliente(int Cedula) {
        this.cedCliente = Cedula;
    }

    /**
     * Modifica la placa del vehiculo
     *
     * @param Placa a cambiar
     */
    public void setPlaca(String Placa) {
        this.placaVeh = Placa;
    }

    /**
     * Modifica el costo
     *
     * @param Costo a cambiar
     */
    public void setCosto(int Costo) {
        this.costo = Costo;
    }

    /**
     *
     *
     * @param Fecha a cambiar
     */
    public void setFechaRecibido(Date Fecha) {
        this.fechaRec = Fecha;
    }

    /**
     * Modifica la fecha de entrega
     *
     * @param Fecha a cambiar
     */
    public void setFechaEntrega(Date Fecha) {
        this.fechaEnt = Fecha;
    }
    
    /**
     * 
     * @param DesTrabajo
     * @param Estado
     * @param cedula
     * @param placa
     * @param DesVehiculo
     * @param DesProblema
     * @param costo
     * @param FechaRec
     * @param FechaEnt 
     */
    public MecanicaGeneral(String DesTrabajo, String Estado, int cedula, String placa, String DesVehiculo, String DesProblema, int costo, Date FechaRec, Date FechaEnt) {
        this.desTrabajo = DesTrabajo;
        this.estado = Estado;
        this.cedCliente = cedula;
        this.placaVeh = placa;
        this.desVehiculo = DesVehiculo;
        this.desProblema = DesProblema;
        this.costo = costo;
        this.fechaRec = FechaRec;
        this.fechaEnt = FechaEnt;
    }

}
