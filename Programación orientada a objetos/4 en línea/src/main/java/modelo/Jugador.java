package modelo;

import sockets.Conexion;

/**
 *Clase Jugador con todos los atributos y métodos que debe contener un jugador.
 * 
 * @author Dario
 */
public class Jugador {
    String nombre;
    String apellidos;
    String correo;
    String contraseña;
    String partidasGanadas;
    String partidasPerdidas;
    String partidasEmpatadas;
    Conexion conexion;
    
    public Jugador(){}
    public Jugador(String nombre, String apellidos, String correo) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.correo = correo;
        this.partidasEmpatadas = "0";
        this.partidasGanadas = "0";
        this.partidasPerdidas = "0";
        
        setContraseña();
    }
    
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getContraseña() {
        return contraseña;
    }
    
    public void setContraseña(String pContraseña) {
        this.contraseña = pContraseña;
    }

    public void setContraseña() {
        Contraseña nuevaContraseña = new Contraseña();
        contraseña = nuevaContraseña.generarContraseña();
    }

    public String getPartidasGanadas() {
        return partidasGanadas;
    }

    public void setPartidasGanadas(String partidasGanadas) {
        this.partidasGanadas = partidasGanadas;
    }

    public String getPartidasPerdidas() {
        return partidasPerdidas;
    }

    public void setPartidasPerdidas(String partidasPerdidas) {
        this.partidasPerdidas = partidasPerdidas;
    }

    public String getPartidasEmpatadas() {
        return partidasEmpatadas;
    }

    public void setPartidasEmpatadas(String partidasEmpatadas) {
        this.partidasEmpatadas = partidasEmpatadas;
    }
    
    public void setConexion(Conexion pConexion){
        this.conexion = pConexion;
    }
    public Conexion getConexion(){
        return conexion;
    }
    
    
    
}
