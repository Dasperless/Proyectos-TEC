package src;

import java.util.Date;

/**
 *
 * Clase Empleado Contiene nombre empleado, tipo de ID del empleado, ID del
 * empleado, rol del empleado, fecha de nacimiento del empleado, fecha de
 * ingreso del empleado, numero de telefono del empleado y correo electronico
 * del empleado.
 *
 * @author Keilor Martinez.
 * @version 1.0
 */
public class Empleado {

// Atributos
    /**
     * String que contiene el nombre del empleado.
     */
    private String nombreEmpleado;

    /**
     * String con el tipo de Identificador del empleado.
     */
    private String tipoIDEmpleado;

    /**
     * VAlor entero con el identificador del empleado.
     */
    private int IDEmpleado;

    /**
     * String con el rol del empleado.
     */
    private String rolEmpleado;

    /**
     * Fecha de nacimiento del empleado.
     */
    private Date fechaNacimientoEmpleado;

    /**
     * Fecha de ingreso del empleado.
     */
    private Date fechaIngresoEmpleado;

    /**
     * Vaor entero con el numero de telefono del empleado.
     */
    private int telefonoEmpleado;

    /**
     * Correo electronico del empleado.
     */
    private String correoEmpleado;

//Métodos.
    /**
     * Devuelve el nombre del empleado.
     *
     * @return nombreEmpleado
     */
    public String getNombreEmpleado() {
        return nombreEmpleado;
    }

    /**
     * Devuelve el tipo de identificador del empleado.
     *
     * @return tipoIDEmpleado
     */
    public String getTipoIDEmpleado() {
        return tipoIDEmpleado;
    }

    /**
     * Devuelve el identificador del empleado.
     *
     * @return IDEmpleado
     */
    public int getIDEmpleado() {
        return IDEmpleado;
    }

    /**
     * Devuelve el rol del empleado.
     *
     * @return rolEmpleado
     */
    public String getRolEmpleado() {
        return rolEmpleado;
    }

    /**
     * Devuelve la fecha de nacimiento del empleado.
     *
     * @return fechaNacimientoEmpleado.
     */
    public Date getFechaNacimientoEmpleado() {
        return fechaNacimientoEmpleado;
    }

    /**
     * Devuelve la fecha de ingreso del empleado.
     *
     * @return fechaIngresoEmpleado
     */
    public Date getFechaIngresoEmpleado() {
        return fechaIngresoEmpleado;
    }

    /**
     * Devuelve el numero de telefono del empleado.
     *
     * @return telefonoEmpleado
     */
    public int getTelefonoEmpleado() {
        return telefonoEmpleado;
    }

    /**
     * Devuelve el correo electronico del empleado.
     *
     * @return correoEmpleado
     */
    public String getCorreoEmpleado() {
        return correoEmpleado;
    }

    /**
     * Modifica el nombre del empleado.
     *
     * @param nuevoNombre
     */
    public void setNombreEmpleado(String nuevoNombre) {
        this.nombreEmpleado = nuevoNombre;
    }

    /**
     * Modifica el tipo de ID del empleado.
     *
     * @param nuevoTipoIDEmpleado
     */
    public void setTipoIDEmpleado(String nuevoTipoIDEmpleado) {
        this.tipoIDEmpleado = nuevoTipoIDEmpleado;
    }

    /**
     * Modifica el ID del empleado.
     *
     * @param nuevoIDEmpleado
     */
    public void setIDEmpleado(int nuevoIDEmpleado) {
        this.IDEmpleado = nuevoIDEmpleado;
    }

    /**
     * Modifica el rol del empleado.
     *
     * @param nuevoRolEmpleado
     */
    public void setRolEmpleado(String nuevoRolEmpleado) {
        this.rolEmpleado = nuevoRolEmpleado;
    }

    /**
     *
     * Modifica la fecha de nacimiento del empleado.
     *
     * @param nuevaFechaNacimientoEmpleado
     */
    public void setFechaNacimientoEmpleado(Date nuevaFechaNacimientoEmpleado) {
        this.fechaNacimientoEmpleado = nuevaFechaNacimientoEmpleado;
    }

    /**
     * Modifica la fecha de ingreso del empleado.
     *
     * @param nuevaFechaIngresoEmpleado
     */
    public void setFechaIngresoEmpleado(Date nuevaFechaIngresoEmpleado) {
        this.fechaIngresoEmpleado = nuevaFechaIngresoEmpleado;
    }

    /**
     * Modifica el numero de telefono del empleado.
     *
     * @param nuevoTelefonoEmpleado
     */
    public void setTelefonoEmpleado(int nuevoTelefonoEmpleado) {
        this.telefonoEmpleado = nuevoTelefonoEmpleado;
    }

    /**
     * Modifica el correo electronico del empleado.
     *
     * @param nuevoCorreoElectronico
     */
    public void setCorreoElectronico(String nuevoCorreoElectronico) {
        this.correoEmpleado = nuevoCorreoElectronico;
    }

// Constructor de la clase.
    /**
     *
     * @param nombre
     * @param tipo
     * @param ID
     * @param Rol
     * @param fechaNacimiento
     * @param fechaIngreso
     * @param telefono
     * @param correo
     */
    public Empleado(String nombre, String tipo, int ID, String Rol, Date fechaNacimiento, Date fechaIngreso, int telefono, String correo) {
        this.nombreEmpleado = nombre;
        this.tipoIDEmpleado = tipo;
        this.IDEmpleado = ID;
        this.rolEmpleado = Rol;
        this.fechaNacimientoEmpleado = fechaNacimiento;
        this.fechaIngresoEmpleado = fechaIngreso;
        this.telefonoEmpleado = telefono;
        this.correoEmpleado = correo;
    }
}
