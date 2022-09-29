package src;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

/**
 * Clase MecanicaGeneral Contiene descripcion del trabajo, estado, cedula
 * cliente, placa veh, descripcion veh, descripcion problema, costo, fecha
 * recibido, fecha posible entrega.
 *
 * @author Maria Paula
 * @version 1.0
 */
public class MecanicaGeneral {

//Atributos
    /**
     * String con la descripcion del trabajo.
     */
    private String desTrabajo;

    /**
     * String con el estado del vehiculo.
     */
    private String estado;

    /**
     * Valor entero con la cedula cliente.
     */
    private int cedCliente;

    /**
     * String con la placa del vehiculo.
     */
    private String placaVeh;

    /**
     * String con la descripcion del vehiculo.
     */
    private String desVehiculo;

    /**
     * String con la descripcion del problema.
     */
    private String desProblema;

    /**
     * Valor entero con el costo.
     */
    private int costo;

    /**
     * Fecha recibido del vehiculo.
     */
    private Date fechaRec;

    /**
     * Fecha de posible entrega del vehiculo.
     */
    private Date fechaEnt;

    /**
     * Lista de empleados a cargo.
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
     * Devuelve la descripcion del vehiculo
     *
     * @return desVehiculo
     */
    public String getDescripcionVehiculo() {
        return desVehiculo;
    }

    /**
     * Devuelve la descripcion del problema.
     *
     * @return desProblema
     */
    public String getDescripcionProblema() {
        return desProblema;
    }

    /**
     * Devuelve el costo del trabajo.
     *
     * @return costo
     */
    public int getCosto() {
        return costo;
    }

    /**
     * Devuelve la fecha de recibido.
     *
     * @return fechaRec
     */
    public Date getFechaRecibido() {
        return fechaRec;
    }

    /**
     * Devuelve la fecha de posible entrega.
     *
     * @return fechaEnt
     */
    public Date getFechaEntrega() {
        return fechaEnt;
    }

    /**
     * Devuelve la lista de empleados a cargo.
     *
     * @return empleados
     */
    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    /**
     * Modifica la descripcion del trabajo.
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
     * Modifica la descripcion del problema.
     *
     * @param Descripcion
     */
    public void setDescripcionProblema(String Descripcion) {
        this.desProblema = Descripcion;
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
     * Modifica la lista de empleados a cargo
     *
     * @param empleados
     */
    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }

    /**
     * Modifica el costo.
     *
     * @param Costo
     */
    public void setCosto(int Costo) {
        this.costo = Costo;
    }

    /**
     * Modifica la fecha de recibido.
     *
     * @param Fecha
     */
    public void setFechaRecibido(Date Fecha) {
        this.fechaRec = Fecha;
    }

    /**
     * Modifica la fecha de entrega.
     *
     * @param Fecha
     */
    public void setFechaEntrega(Date Fecha) {
        this.fechaEnt = Fecha;
    }

    /**
     * Devuelve la información del Servicio de Mecanica General.
     * @return msj
     */
    @Override
    public String toString() {
        DateFormat dateFormat = new SimpleDateFormat("d-MM-y");
        String msj = "********* Información del servicio *********\n";
        msj += "Cedula del cliente: " + cedCliente + "\n";
        msj += "Estado: " + estado + "\n";
        msj += "Descripción del vehiculo: " + desVehiculo + "\n";
        msj += "Costo: " + costo + "\n";
        msj += "Descripción del problema: " + desProblema + "\n";
        msj += "Placa del vehiculo: " + placaVeh + "\n";
        msj += "Fecha de entrega: " + dateFormat.format(fechaEnt) + "\n";
        msj += "Fecha de recibido: " + dateFormat.format(fechaRec) + "\n";
        msj += "Empleados a cargo:\n";
        for (int i = 0; i < empleados.size(); i++) {
            msj += "\t" + empleados.get(i).getNombreEmpleado() + "\n";
        }
        return msj;
    }

    /**
     * Constructor
     *
     * @param cedCliente
     * @param estado
     * @param desVehiculo
     * @param costo
     * @param desProblema
     * @param placaVeh
     * @param fechaEnt
     * @param fechaRec
     * @param empleados
     */
    public MecanicaGeneral(String estado, int cedCliente, String placaVeh, String desVehiculo, String desProblema, int costo, Date fechaRec, Date fechaEnt, ArrayList<Empleado> empleados) {
        this.estado = estado;
        this.cedCliente = cedCliente;
        this.placaVeh = placaVeh;
        this.desVehiculo = desVehiculo;
        this.desProblema = desProblema;
        this.costo = costo;
        this.fechaRec = fechaRec;
        this.fechaEnt = fechaEnt;
        this.empleados = empleados;
    }

}
