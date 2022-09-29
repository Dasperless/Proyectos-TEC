
import java.util.Date;


/**
 * Clase EnderezadoyPintura
 * Contiene cedula cliente, placa veh, descripcion veh, partes del vehiculo a enderezar, pintor, poliza, numero de caso, estado, descripcion del trabajo,  costo, fecha recibido, fecha posible entrega.
 *
 * @author Paula Rubio
 * @version 1.0
 */
public class EnderezadoyPintura {

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
     * Partes del vehiculo a enderezar
     */
    private String parteEnderezarPinter;

    /**
     * Pintor
     */
    private String pintor;

    /**
     * Poliza
     */
    private Boolean poliza;

    /**
     * Numero de caso
     */
    private static int numCaso = 1;

    /**
     * Descripcion del trabajo
     */
    private String desTrabajo;

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
     * Devuelve las partes del vehiculo a enderezar
     *
     * @return parteVehEnderezar
     */
    public String getPartesEnderezarPintar() {
        return parteEnderezarPinter;
    }

    /**
     * Devuelve el pintor
     *
     * @return pintor
     */
    public String getPintor() {
        return pintor;
    }

    /**
     * Devuelve la poliza
     *
     * @return poliza
     */
    public Boolean getPoliza() {
        return poliza;
    }

    /**
     * Devuelve el numero de caso
     *
     * @return numCaso
     */
    public static int getNumeroCaso() {
        return numCaso;
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
     * Modifica las partes a enderezar
     *
     * @param Partes a cambiar
     */
    public void setPartesEnderezarPintar(String Partes) {
        this.parteEnderezarPinter = Partes;
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
     * Modifica la fecha de recibido
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
     * Modifica el pintor
     *
     * @param Pintor a cambiar
     */
    public void setPintor(String Pintor) {
        this.pintor = Pintor;
    }

    /**
     * Modifica la poliza
     *
     * @param Poliza a cambiar
     */
    public void setPoliza(Boolean Poliza) {
        this.poliza = Poliza;
    }
    
    
    /**
     * Constructor
     *
     * @param estado
     * @param cedCliente
     * @param placaVeh
     * @param desVehiculo
     * @param parteEnderezarPinter
     * @param pintor
     * @param poliza
     * @param desTrabajo
     * @param costo
     * @param fechaRec
     * @param fechaEnt
     */
       
    public EnderezadoyPintura(String estado, int cedCliente, String placaVeh, String desVehiculo, String parteEnderezarPinter, String pintor, Boolean poliza, String desTrabajo, int costo, Date fechaRec, Date fechaEnt) {
        this.estado = estado;
        this.cedCliente = cedCliente;
        this.placaVeh = placaVeh;
        this.desVehiculo = desVehiculo;
        this.parteEnderezarPinter = parteEnderezarPinter;
        this.pintor = pintor;
        this.poliza = poliza;
        this.desTrabajo = desTrabajo;
        this.costo = costo;
        this.fechaRec = fechaRec;
        this.fechaEnt = fechaEnt;
    }



}
