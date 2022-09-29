package src;

/**
 * 
 * @author Keilor Martines
 * @version %I%
 */
public class Cliente{

	// Atributos

	/*
	 * Nombre del cliente.
	 */

	private String nombreCliente;

	/*
	 * Tipo de identificador del cliente.
	 */

	private String tipoIDCliente;

	/*
	 * Identificador del cliente.
	 */

	private int IDCliente;

	/*
	 * Cantón donde reside el cliente.
	 */

	private String cantonCliente;

	/*
	 * Fecha de nacimiento del cliente.
	 */

	private String fechaNacimientoCliente;

	/*
	 * Número telefónico del cliente.
	 */

	private int telefonoCliente;

	/*
	 * Correo electrónico del cliente.
	 */

	private String correoCliente;

	// Métodos de obtención de datos.

	/*
	 * @return nombreCliente.
	 */

	public String getNombreCliente(){
		return nombreCliente;
	}

	/*
	 * @return tipoIDCLiente.
	 */

	public String getTipoIDCliente(){
		return tipoIDCliente;
	}

	/*
	 * @return IDCliente.
	 */

	public int getIDCliente(){
		return IDCliente;		
	}

	/*
	 * @return cantonCliente.
	 */

	public String getCantonCliente(){
		return cantonCliente;
	}

	/*
	 * @return fechaNacimientoCliente.
	 */

	public String getFechaNacimientoCliente(){
		return fechaNacimientoCliente;
	}

	/*
	 * @return telefonoCliente.
	 */

	public int getTelefonoCliente(){
		return telefonoCliente;
	}

	/*
	 * @return correoCliente.
	 */

	public String getCorreoCliente(){
		return correoCliente;
	}
	
	// Métodos de modificación de valores.
	
	/*
	 * Modificar el nombre del cliente.
	 * @param nombre del cliente.
	 */
	 
	public void setNombreCliente(String nuevoNombre){
		this.nombreCliente = nuevoNombre;
	}
	
	/*
	 * Modificar el tipo de identificador del cliente.
	 * @param tipo de identificador del cliente.
	 */
	 
	public void setTipoIDCliente(String nuevoTipo){
		this.tipoIDCliente = nuevoTipo;
	}
	
	/*
	 * Modificar el identificador del cliente.
	 * @param identificador del cliente.
	 */
	 
	public void setIDCliente(int nuevoID){
		this.IDCliente = nuevoID;
	}
	
	/*
	 * Modificar el cantón donde reside el cliente. 
	 * @param cantón del cliente.
	 */
	 
	public void setCantonCliente(String nuevoCanton){
		this.cantonCliente = nuevoCanton;
	}
	
	/*
	 * Modificar la fecha de nacimiento del cliente.
	 * @param fecha de nacimiento del cliente.
	 */
	 
	public void setFechaNacimientoCliente(String nuevaFechaNacimiento){
		this.fechaNacimientoCliente = nuevaFechaNacimiento;
	}
	
	/*
	 * Modificar el número telefónico del cliente.
	 * @param número de teléfono del cliente.
	 */
	 
	public void setTelefonoCliente(int nuevoNumero){
		this.telefonoCliente = nuevoNumero;
	}
	
	/*
	 * Modificar el correo electrónico del cliente.
	 * @param correo electrónico del cliente.
	 */
	 
	public void setCorreoCliente(String nuevoCorreo){
		this.correoCliente = nuevoCorreo;
	}
	
	public void ToString() { 
        System.out.println("Nombre: " + this.getNombreCliente() + "\n" + 
               "Tipo ID: " + this.getTipoIDCliente() + "\n" + 
               "ID: " + this.getIDCliente() + "\n" + 
               "Cantón: " + this.getCantonCliente() + "\n" +
               "Fecha de Nacimiento: " + this.getFechaNacimientoCliente() + "\n" +
               "Número de Teléfono: " + this.getTelefonoCliente() + "\n" + 
               "Correo electrónico: " + this.getCorreoCliente()); 
    } 
	
	// Constructor de la clase.
	
	public Cliente(String nombre, String TipoID, int ID, String Canton, String FechaNacimiento, int Telefono, String Correo){
		this.nombreCliente = nombre;
		this.tipoIDCliente = TipoID;
		this.IDCliente = ID;
		this.cantonCliente = Canton;
		this.fechaNacimientoCliente = FechaNacimiento;
		this.telefonoCliente = Telefono;
		this.correoCliente = Correo;
	}
}
