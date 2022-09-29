/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Arrays;
import javax.swing.JButton;
import javax.swing.JTextField;
import modelo.Correo;
import modelo.CuatroEnLinea;
import modelo.Jugador;
import modelo.Sesion;
import modelo.Tablero;
import modelo.popUpMessage;
import vista.Vista;

/**
 *
 * @author dario
 */
public class Controlador implements ActionListener {

    private Sesion modelo;
    private Vista vista;
    private CuatroEnLinea juego;
    private Jugador player;

    public Controlador(Sesion modelo, Vista vista) {
        this.vista = vista;
        this.modelo = modelo;
    }

    public void iniciar() {
        vista.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent arg) {
        String comando = arg.getActionCommand();
        switch (comando) {
            case "PANEL_INICIAR_SESION":
                btnIniciarSesionActionPerformed(arg);
                break;
            case "PANEL_REGISTRAR":
                btnRegistrarActionPerformed(arg);
                break;
            case "REGISTRAR_USUARIO":
                btnRegistrarUsuarioActionPerformed(arg);
                break;
            case "VOLVER_CREAR_PARTIDA":
                backBtnCrearPartidaActionPerformed(arg);
                break;
            case "VOLVER_REGISTRO_USUARIO":
                volverRegistroUsuarioActionPerformed(arg);
                break;
            case "INICIAR_SESION":
                btnIniciarActionPerformed(arg);
                break;
            case "CREAR_PARTIDA":
                btnCrearPartidaNuevaActionPerformed(arg);
                break;
            case "VOLVER_INICIAR_SESION":
                volverIniciarSesionActionPerformed(arg);
                break;
            case "PANEL_CREAR_PARTIDA":
                btnCrearPartidaActionPerformed(arg);
                break;
            case "UNIRSE_PARTIDA":
                btnUnirsePartidaActionPerformed(arg);
                break;
            case "CERRAR_SESION":
                btnCerrarSesionActionPerformed(arg);
                break;
            default:
                System.out.println("Comando no definido");
                break;
        }
    }
    
    private void btnIniciarSesionActionPerformed(java.awt.event.ActionEvent evt) {                                                 
        vista.iniciarSesion.setVisible(true);
        JButton b = (JButton) evt.getSource();
        b.getParent().setVisible(false);
    }                                                
                                       
    private void volverRegistroUsuarioActionPerformed(java.awt.event.ActionEvent evt) {                                                      
        vista.login.setVisible(true);
        esconderPanelActual(evt);
    }   
    
    private void btnRegistrarActionPerformed(java.awt.event.ActionEvent evt) {                                             
        vista.registrarUsuario.setVisible(true);
        JButton b = (JButton) evt.getSource();
        b.getParent().setVisible(false);
    }                                            

    private void volverIniciarSesionActionPerformed(java.awt.event.ActionEvent evt) {                                                    
        vista.login.setVisible(true);
        esconderPanelActual(evt);
    }                          
    
    private void btnIniciarActionPerformed(java.awt.event.ActionEvent evt) {           
        System.out.println("INCIAR SESION");
//        volverIniciarSesionActionPerformed(evt);
        String usuario = vista.fieldUsuario.getText();
        String contraseña = vista.fieldContraseña.getText();
        ArrayList<JTextField> camposTexto = new ArrayList<>(Arrays.asList(vista.fieldUsuario,vista.fieldContraseña));
        limpiarCampos(camposTexto);
        
        if(modelo.iniciarSesion(usuario, contraseña) != null){
            player  = modelo.iniciarSesion(usuario, contraseña) ;
            popUpMessage.infoBox("Bienvenido " + player.getNombre(), "Inicio de Sesion");
            JButton b = (JButton) evt.getSource();
            b.getParent().getParent().setVisible(false);
            vista.pantallaJuego.setVisible(true);
        }else{
            popUpMessage.infoBox("El usuario o contraseña son incorrectos", "Error");
        }
        
    }     
    
    private void esconderPanelActual(ActionEvent evt){
        JButton b = (JButton) evt.getSource();
        b.getParent().setVisible(false);        
    }

    private void btnRegistrarUsuarioActionPerformed(ActionEvent arg) {
        String nombre = vista.fieldNombre.getText();
        String apellidos = vista.fieldApellidos.getText();
        String correo = vista.fieldCorreo.getText();    
        Jugador usuario = new Jugador(nombre,apellidos,correo);
//        envioContraseña(usuario);
        modelo.registrarJugador(usuario);
    }

    private void envioContraseña(Jugador usuario) {
        String destinatario = usuario.getCorreo();
        String contenido = "Bienvenido a nuestro juego 4 en linea su contraseña es: " + usuario.getContraseña();
        String asunto = "Contraseña cuatro en linea.";
        Correo enviarContraseña = new Correo(destinatario, asunto, contenido);
        enviarContraseña.enviarEmail();
    }
    
    private void limpiarCampos(ArrayList<JTextField> campoText){
        for(int i = 0; i < campoText.size(); i++){
            campoText.get(i).setText("");
        }
    }
    private void btnIniciarJuegoActionPerformed(ActionEvent evt) {
        System.out.println("btnIniciarJuegoActionPerformed");
    }

    private void btnCrearPartidaNuevaActionPerformed(ActionEvent arg) {
        //Datos de los campos de texto
//        String nombrePartida = vista.nombrePartida.getText();
        String colorJ1 = vista.colorFichaJ1.getSelectedItem().toString();
        String colorJ2 = vista.colorFichaJ2.getSelectedItem().toString();
        int filas = Integer.valueOf(vista.numFilas.getSelectedItem().toString());
        int columnas = Integer.valueOf(vista.numFilas.getSelectedItem().toString());
        ArrayList<JTextField> camposDeTexto = new ArrayList<>(Arrays.asList(vista.nombrePartida));        
        if(validarCrearPartida(camposDeTexto,colorJ1,colorJ2)){
            juego = new CuatroEnLinea(8,8,2,"Rojo","Azul");
            Tablero tablero = new Tablero(juego);
//        CuatroEnLinea logica = new CuatroEnLinea(8,8,2,)
//        new ConnectFour();
        }
        
    }
    private boolean validarCrearPartida(ArrayList<JTextField> pCamposDeTexto, String pColorJ1, String pColorJ2){
        if(!validarCamposVacios(pCamposDeTexto) ){
            popUpMessage.infoBox("EL nombre del servidor no puede estár vacío.", "Error");
            return false;
        }else if(pColorJ1.equals(pColorJ2)){
            popUpMessage.infoBox("El color del jugador 1 no puede ser igual al del jugador 2", "Error");
            return false;
        }
        return true;
    }
    private boolean validarCamposVacios(ArrayList<JTextField> pTextField){
        for(int i = 0; i<pTextField.size();i++){
            if(pTextField.get(i).getText().equals("")){
                return false;
            }
        }
       return true;
    }

    private void btnCrearPartidaActionPerformed(ActionEvent evt) {
        esconderPanelActual(evt);
        vista.crearPartida.setVisible(true);
        System.out.println("btnCrearPartidaActionPerformed");
    }

    private void backBtnCrearPartidaActionPerformed(ActionEvent evt) {
        esconderPanelActual(evt);
        vista.pantallaJuego.setVisible(true);
    }

    private void btnUnirsePartidaActionPerformed(ActionEvent evt) {
        esconderPanelActual(evt);
        vista.unirsePartida.setVisible(true);
        
    }

    private void btnCerrarSesionActionPerformed(ActionEvent evt) {
        esconderPanelActual(evt);        
        player = null;
        vista.pantallaInicio.setVisible(true);
    }
    

}
