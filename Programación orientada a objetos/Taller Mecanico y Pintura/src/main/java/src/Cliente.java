package src;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 *
 * Clase Cliente Contiene nombre del cliente, tipo de ID del cliente, canton
 * donde reside el cliente, fecha de nacimiento del cliente numero de telefono
 * del cliente y el correo electronico del cliente.
 *
 * @author Keilor Martinez
 * @version 1.0
 */
public class Cliente {

// Atributos
    /**
     * String con el nombre del cliente.
     */
    private String nombreCliente;

    /**
     * String con el tipo de identificador del cliente.
     */
    private String tipoIDCliente;

    /**
     * Strng con el identificador del cliente.
     */
    private int IDCliente;

    /**
     * String con el canton donde reside el cliente.
     */
    private String cantonCliente;

    /**
     * String con la fecha de nacimiento del cliente.
     */
    private Date fechaNacimientoCliente;

    /**
     * Valor entero con el numero telefonico del cliente.
     */
    private int telefonoCliente;

    /**
     * Correo electronico del cliente.
     */
    private String correoCliente;

// Métodos.
    /**
     * Devuelve el nombre del cliente.
     *
     * @return nombreCliente
     */
    public String getNombreCliente() {
        return nombreCliente;
    }

    /**
     * Devuelve el tipo de identificacion del cliente.
     *
     * @return tipoIDCliente
     */
    public String getTipoIDCliente() {
        return tipoIDCliente;
    }

    /**
     * Devuelve el identificador del cliente.
     *
     * @return IDCliente
     */
    public int getIDCliente() {
        return IDCliente;
    }

    /**
     * Devuelve el canton de donde reside el cliente.
     *
     * @return cantonCliente
     */
    public String getCantonCliente() {
        return cantonCliente;
    }

    /**
     * Devuelve la fecha de nacimiento del cliente.
     *
     * @return fechaNacimientoCliente
     */
    public Date getFechaNacimientoCliente() {
        return fechaNacimientoCliente;
    }

    /**
     * Devuelve el numero telefonico del cliente.
     *
     * @return telefonoCliente
     */
    public int getTelefonoCliente() {
        return telefonoCliente;
    }

    /**
     * Devuelve el correo electronico del cliente.
     *
     * @return correoCliente
     */
    public String getCorreoCliente() {
        return correoCliente;
    }

    /**
     * Modifica el nombre del cliente.
     *
     * @param nuevoNombre
     */
    public void setNombreCliente(String nuevoNombre) {
        this.nombreCliente = nuevoNombre;
    }

    /**
     * Modifica el tipo de identificador del cliente.
     *
     * @param nuevoTipo
     */
    public void setTipoIDCliente(String nuevoTipo) {
        this.tipoIDCliente = nuevoTipo;
    }

    /**
     * Modifica el identificador del cliente.
     *
     * @param nuevoID
     */
    public void setIDCliente(int nuevoID) {
        this.IDCliente = nuevoID;
    }

    /**
     * Modifica el canton donde reside el cliente.
     *
     * @param nuevoCanton
     */
    public void setCantonCliente(String nuevoCanton) {
        this.cantonCliente = nuevoCanton;
    }

    /**
     * Modifica la fecha de nacimiento del cliente.
     *
     * @param nuevaFechaNacimiento
     */
    public void setFechaNacimientoCliente(Date nuevaFechaNacimiento) {
        this.fechaNacimientoCliente = nuevaFechaNacimiento;
    }

    /**
     * Modifica el numero telefonico del cliente.
     *
     * @param nuevoNumero
     */
    public void setTelefonoCliente(int nuevoNumero) {
        this.telefonoCliente = nuevoNumero;
    }

    /**
     * Modificar el correo electronico del cliente.
     *
     * @param nuevoCorreo
     */
    public void setCorreoCliente(String nuevoCorreo) {
        this.correoCliente = nuevoCorreo;
    }

    /**
     * Devuelve un String con la información del cliente
     *
     * @return msj
     */
    @Override
    public String toString() {
        DateFormat dateFormat = new SimpleDateFormat("d-MM-y");
        String msj = "******* Información del cliente *******\n";
        msj += "Nombre del cliente: " + nombreCliente + "\n";
        msj += "Tipo de identificación: " + tipoIDCliente + "\n";
        msj += "Identificación: " + IDCliente + "\n";
        msj += "Cantón: " + cantonCliente + "\n";
        msj += "Fecha nacimiento: " + dateFormat.format(fechaNacimientoCliente) + "\n";
        msj += "Telefono: " + telefonoCliente + "\n";
        msj += "Correo: " + correoCliente + "\n";
        return msj;
    }

// Constructor de la clase.
    /**
     *
     * @param nombre
     * @param TipoID
     * @param ID
     * @param Canton
     * @param FechaNacimiento
     * @param Telefono
     * @param Correo
     */
    public Cliente(String nombre, String TipoID, int ID, String Canton, Date FechaNacimiento, int Telefono, String Correo) {
        this.nombreCliente = nombre;
        this.tipoIDCliente = TipoID;
        this.IDCliente = ID;
        this.cantonCliente = Canton;
        this.fechaNacimientoCliente = FechaNacimiento;
        this.telefonoCliente = Telefono;
        this.correoCliente = Correo;
    }
}
