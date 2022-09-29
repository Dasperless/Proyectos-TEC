package src;

/**
 * 
 * @author Keilor Martines
 * @version %I%
 */
class Empleado{

	// Atributos

	/*
	 * Nombre del empleado.
	 */	

	private String nombreEmpleado;

	/*
	 * Tipo de Identificador del empleado.
	 */

	private String tipoIDEmpleado;

	/*
	 * Identificador del empleado.
	 */

	private int IDEmpleado;

	/*
	 * Rol del empleado.
	 */

	private String rolEmpleado;

	/*
	 * Fecha de nacimiento del empleado.
	 */

	private String fechaNacimientoEmpleado;

	/*
	 * Fecha de ingreso del empleado.
	 */

	private String fechaIngresoEmpleado;

	/*
	 * Número de teléfono del empleado.
	 */

	private int telefonoEmpleado;

	/*
	 * Correo electrónico del empleado.
	 */

	private String correoEmpleado;


	// Métodos de obtención de datos.

	/*
	 * @return nombreEmpleado.
	 */

	public String getNombreEmpleado(){
		return nombreEmpleado;
	}

	/*
	 * @return tipoIDEmpleado.
	 */

	public String getTipoIDEmpleado(){
		return tipoIDEmpleado;
	}

	/*
	 * @return IDEmpleado.
	 */

	public int getIDEmpleado(){
		return IDEmpleado;
	}

	/*
	 * @return rolEmpleado.
	 */

	public String getRolEmpleado(){
		return rolEmpleado;
	}

	/*
	 * @return fechaNacimientoEmpleado;
	 */

	public String getFechaNacimientoEmpleado(){
		return fechaNacimientoEmpleado;
	}

	/*
	 * @return fechaIngresoEmpleado.
	 */

	public String getFechaIngresoEmpleado(){
		return fechaIngresoEmpleado;
	}	

	/*
	 * @return telefonoEmpleado.
	 */

	public int getTelefonoEmpleado(){
		return telefonoEmpleado;
	}

	/*
	 * @return correoEmpleado.
	 */

	public String getCorreoEmpleado(){
		return correoEmpleado;
	}


	// Mètodos de modificación de datos.

	/*
	 * Modificar el nombre del empleado.
	 * @param nuevoNombre.
	 */

	public void setNombreEmpleado(String nuevoNombre){
		this.nombreEmpleado = nuevoNombre;
	}

	/*
	 * Modificar el tipo de ID del empleado.
	 * @param  nuevoTipoIDEmpleado.
	 */

	public void setTipoIDEmpleado(String nuevoTipoIDEmpleado){
		this.tipoIDEmpleado = nuevoTipoIDEmpleado;
	}

	/*
	 * Modificar el ID del empleado.
	 * @param nuevoIDEmpleado.
	 */

	public void setIDEmpleado(int nuevoIDEmpleado){
		this.IDEmpleado = nuevoIDEmpleado;
	}

	/*
	 * Modificar el rol del empleado.
	 * @param nuevoRolEmpleado.
	 */

	public void setRolEmpleado(String nuevoRolEmpleado){
		this.rolEmpleado = nuevoRolEmpleado;
	}

	/*
	 * Modificar la fecha de nacimiento del empleado.
	 * @param nuevaFechaNacimientoEmpleado.
	 */

	public void setFechaNacimientoEmpleado(String nuevaFechaNacimientoEmpleado){
		this.fechaNacimientoEmpleado = nuevaFechaNacimientoEmpleado;
	}

	/*
	 * Modificar al fecha de ingreso del empleado.
	 * @param nuevaFechaIngresoEmpleado.
	 */

	public void setFechaIngresoEmpleado(String nuevaFechaIngresoEmpleado){
		this.fechaIngresoEmpleado = nuevaFechaIngresoEmpleado;
	}

	/*
	 * Modificar el número de teléfono del empleado.
	 * @param nuevoTelefonoEmpleado.
	 */

	public void setTelefonoEmpleado(int nuevoTelefonoEmpleado){
		this.telefonoEmpleado = nuevoTelefonoEmpleado;
	}

	/*
	 * Modificar el correo electrónico del empleado.
	 * @param nuevoCorreoEmpleado.
	 */

	public void setCorreoElectronico(String nuevoCorreoElectronico){
		this.correoEmpleado = nuevoCorreoElectronico;
	}

	public void ToString() { 
        System.out.println("Nombre: " + this.getNombreEmpleado() + "\n" + 
               "Tipo ID: " + this.getTipoIDEmpleado() + "\n" + 
               "ID: " + this.getIDEmpleado() + "\n" + 
               "Rol: " + this.getRolEmpleado() + "\n" +
               "Fecha de Nacimiento: " + this.getFechaNacimientoEmpleado() + "\n" +
			   "Fecha de Ingreso: " + this.getFechaIngresoEmpleado() + "\n" +
               "Número de Teléfono: " + this.getTelefonoEmpleado() + "\n" + 
               "Correo electrónico: " + this.getCorreoEmpleado()); 
    }

	// Constructor de la clase.

	public Empleado(String nombre, String tipo, int ID, String Rol, String fechaNacimiento, String fechaIngreso, int telefono, String correo){
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
