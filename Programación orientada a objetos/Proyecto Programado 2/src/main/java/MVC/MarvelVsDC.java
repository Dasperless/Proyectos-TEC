package MVC;

import controlador.Controlador;
import modelo.Modelo;
import vista.Vista;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author dario
 */
public class MarvelVsDC {

    /**
     *
     * @param args
     */
    public static void main(String[] args) {
        Modelo mod = new Modelo();
        Vista view = new Vista();
        Controlador ctrl = new Controlador(view,mod);
        ctrl.iniciar();
    }
}
