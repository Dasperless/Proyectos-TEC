package src;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

/**
 * Clase EnderezadoyPintura Contiene cedula cliente, placa vehiculo, descripcion
 * vehículo, partes del vehiculo a enderezar, pintor, poliza, numero de caso,
 * estado, descripcion del trabajo, costo, fecha recibido, fecha posible
 * entrega.
 *
 * @author Maria Paula
 * @version 1.0
 */
public class EnderezadoyPintura {

// Atributos
    /**
     * String que representa el estado del vehiculo.
     */
    private String estado;

    /**
     * Valor entero que contiene la cedula del cliente.
     */
    private int cedCliente;

    /**
     * String con la placa del vehiculo.
     */
    private String placaVeh;

    /**
     * String con una descripcion del vehiculo.
     */
    private String desVehiculo;

    /**
     * String que representa partes del vehiculo a enderezar.
     */
    private String parteEnderezarPintar;

    /**
     * Valor booleano que informa si el vehiculo posee poliza.
     */
    private Boolean poliza;

    /**
     * Valor entero que contiene el numero de caso.
     */
    private final int numCaso;

    /**
     * String con la descripcion del trabajo
     */
    private String desTrabajo;

    /**
     * Valor entero con el costo de un trabajo.
     */
    private int costo;

    /**
     * Fecha recibido del vehiculo con el que se va a trabajar.
     */
    private Date fechaRec;

    /**
     * Fecha de posible entrega del vehiculo despues del trabajo.
     */
    private Date fechaEnt;

    /**
     * Lista que posee la lista de empleados.
     */
    private ArrayList<Empleado> empleados;

//Metodos 
    /**
     * Devuelve la descripcion del trabajo.
     *
     * @return desTrabajo
     */
    public String getDescripcionTrabajo() {
        return desTrabajo;
    }

    /**
     * Devuelve el estado del vehiculo.
     *
     * @return estado
     */
    public String getEstado() {
        return estado;
    }

    /**
     * Devuelve la cedula del cliente.
     *
     * @return cedCliente
     */
    public int getCedulaCliente() {
        return cedCliente;
    }

    /**
     * Devuelve la placa del vehiculo.
     *
     * @return placaVeh
     */
    public String getPlacaVehiculo() {
        return placaVeh;
    }

    /**
     * Devuelve la descripcion del vehiculo.
     *
     * @return desVehiculo
     */
    public String getDescripcionVehiculo() {
        return desVehiculo;
    }

    /**
     * Devuelve las partes del vehiculo a enderezar.
     *
     * @return parteVehEnderezar
     */
    public String getPartesEnderezarPintar() {
        return parteEnderezarPintar;
    }

    /**
     * Devuelve un valor booleano sobre la poliza del vehiculo.
     *
     * @return poliza
     */
    public Boolean getPoliza() {
        return poliza;
    }

    /**
     * Devuelve el numero de caso que se va a trabajar.
     *
     * @return numCaso
     */
    public int getNumeroCaso() {
        return numCaso;
    }

    /**
     * Devuelve el costo del trabajo que se hara al vehiculo.
     *
     * @return costo
     */
    public int getCosto() {
        return costo;
    }

    /**
     * Devuelve la fecha de recibido del vehiculo.
     *
     * @return fechaRec
     */
    public Date getFechaRecibido() {
        return fechaRec;
    }

    /**
     * Devuelve la fecha de posible entrega del vehiculo.
     *
     * @return fechaEnt
     */
    public Date getFechaEntrega() {
        return fechaEnt;
    }

    /**
     * Devuelve la lista de empleados a cargo
     *
     * @return empleados
     */
    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    /**
     * Modifica la descripcion del trabajo que se le hara al vehiculo.
     *
     * @param Descripcion
     */
    public void setDescripcionTrabajo(String Descripcion) {
        this.desTrabajo = Descripcion;
    }

    /**
     * Modifica la descripcion del vehiculo.
     *
     * @param Descripcion
     */
    public void setDescripcionVehiculo(String Descripcion) {
        this.desVehiculo = Descripcion;
    }

    /**
     * Modifica las partes a enderezar del vehiculo.
     *
     * @param Partes
     */
    public void setPartesEnderezarPintar(String Partes) {
        this.parteEnderezarPintar = Partes;
    }

    /**
     * Modifica el estado del vehiculo.
     *
     * @param Estado
     */
    public void setEstado(String Estado) {
        this.estado = Estado;
    }

    /**
     * Modifica la cedula del cliente.
     *
     * @param Cedula
     */
    public void setCedulaCliente(int Cedula) {
        this.cedCliente = Cedula;
    }

    /**
     * Modifica la placa del vehiculo.
     *
     * @param Placa
     */
    public void setPlaca(String Placa) {
        this.placaVeh = Placa;
    }

    /**
     * Modifica el costo del trabajo que se hara al vehiculo.
     *
     * @param Costo
     */
    public void setCosto(int Costo) {
        this.costo = Costo;
    }

    /**
     * Modifica la fecha de recibido del vehiculo.
     *
     * @param Fecha
     */
    public void setFechaRecibido(Date Fecha) {
        this.fechaRec = Fecha;
    }

    /**
     * Modifica la fecha de entrega dek vehiculo.
     *
     * @param Fecha
     */
    public void setFechaEntrega(Date Fecha) {
        this.fechaEnt = Fecha;
    }

    /**
     * Modifica la poliza del vehiculo.
     *
     * @param Poliza
     */
    public void setPoliza(Boolean Poliza) {
        this.poliza = Poliza;
    }

    /**
     * Modifica los empleados a cargo de los trabajos que se le haran al
     * vehiculo.
     *
     * @param empleados
     */
    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }

    /**
     * Devuelve la información del Servicio Enderezado y pintura.
     *
     * @return msj
     */
    @Override
    public String toString() {
        DateFormat dateFormat = new SimpleDateFormat("d-MM-y");
        String msj = "********* Información del servicio *********\n";
        msj += "Cedula del cliente: " + cedCliente + "\n";
        msj += "Estado: " + estado + "\n";
        msj += "Numero de caso: " + numCaso + "\n";
        msj += "Partes a enderezar y Pintar: " + parteEnderezarPintar + "\n";
        msj += "Descripción del vehiculo: " + desVehiculo + "\n";
        msj += "Póliza: ";
        if (poliza) {
            msj += "Sí";
        } else {
            msj += "No";
        }
        msj += "Placa del vehiculo: " + placaVeh + "\n";
        msj += "Fecha de entrega: " + dateFormat.format(fechaEnt) + "\n";
        msj += "Fecha de recibido: " + dateFormat.format(fechaRec) + "\n";
        msj += "Empleados a cargo:\n";
        for (int i = 0; i < empleados.size(); i++) {
            msj += "\t" + empleados.get(i).getNombreEmpleado() + "\n";
        }
        msj += "Costo: " + costo + "\n";
        return msj;
    }

    /**
     * Constructor
     *
     * @param estado
     * @param placaVeh
     * @param cedCliente
     * @param numCaso
     * @param desVehiculo
     * @param partesEnderezarPintar
     * @param poliza
     * @param costo
     * @param fechaEnt
     * @param fechaRec
     * @param empleados
     */
    public EnderezadoyPintura(String estado, int cedCliente, String placaVeh, int numCaso, String desVehiculo, String partesEnderezarPintar, Boolean poliza, int costo, Date fechaRec, Date fechaEnt, ArrayList<Empleado> empleados) {
        this.numCaso = numCaso;
        this.estado = estado;
        this.cedCliente = cedCliente;
        this.placaVeh = placaVeh;
        this.desVehiculo = desVehiculo;
        this.parteEnderezarPintar = partesEnderezarPintar;
        this.poliza = poliza;
        this.costo = costo;
        this.fechaRec = fechaRec;
        this.fechaEnt = fechaEnt;
        this.empleados = empleados;
    }

}
