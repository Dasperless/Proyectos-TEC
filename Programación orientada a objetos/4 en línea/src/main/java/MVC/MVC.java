/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MVC;

import controlador.Controlador;
import modelo.Sesion;
import vista.Vista;
//import vista.Conecta4;
//import vista.PanelTablero;

/**
 *
 * @author dario
 */
public class MVC {

    public static void main(String[] args) {
        Sesion registroUsuarios = new Sesion();
        Vista vista = new Vista();
        Controlador controlador = new Controlador(registroUsuarios,vista);
        vista.conectaControlador(controlador);
        controlador.iniciar();  
//        Sesion s = new Sesion();
//        ArrayList<ArrayList<String>> usuarios = s.listaUsuarios();
//        System.out.println(s.getUsuario(usuarios.get(0)).getContraseña());

    }
}
