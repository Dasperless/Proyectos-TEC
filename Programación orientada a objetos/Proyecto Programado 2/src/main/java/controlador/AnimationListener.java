/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JProgressBar;
import modelo.AntiHeroe;
import modelo.Heroe;
import modelo.Persona;
import modelo.Villano;

/**
 *
 * @author dario
 */
public class AnimationListener implements ActionListener {

    private JComponent target;
    private ArrayList<JComponent> listaComponentes;
    private JLabel rondasGanadasHeroe;
    private JLabel rondasGanadasVillano;
    private JLabel rondas;
    private JProgressBar barraProgreso;
    private Persona heroeAntiheroe;
    private Persona villano;
    private int probabilidad;
    
    /**
     *
     * @param target
     * @param listaComponentes
     * @param rondasGanadasHeroe
     * @param rondasGanadasVillano
     * @param rondas
     * @param barraProgreso
     * @param heroeAntiheroe
     * @param villano
     */
    public AnimationListener(JComponent target, ArrayList<JComponent> listaComponentes, JComponent rondasGanadasHeroe, JComponent rondasGanadasVillano, JComponent rondas, JComponent barraProgreso,Persona heroeAntiheroe, Persona villano) {
        this.target = target;
        this.listaComponentes = listaComponentes;
        this.rondasGanadasHeroe = (JLabel)rondasGanadasHeroe;
        this.rondasGanadasVillano =(JLabel) rondasGanadasVillano;
        this.barraProgreso = (JProgressBar)barraProgreso;
        this.rondas =(JLabel) rondas;
        this.heroeAntiheroe = heroeAntiheroe;
        this.villano = villano;
    }

    /**
     *
     * @param e
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        target.setEnabled(true);
        switchLabelVisible(listaComponentes);
        generarEvento();
        
    }
    
    private int randomNum(int maxNum,int minNum){
        int numero = (int)(Math.random()*maxNum+minNum);
        return numero;
    }
    
    private void generarEvento(){
        int num = randomNum(100,1);
        barraProgreso.setValue(num);
        probabilidad = getProbabilidad();
        gane(num);
    }
    
    
    private int getProbabilidad(){
        if(heroeAntiheroe instanceof AntiHeroe){
            return probabilidadAntiheroe();
        }else{
            return probabilidadHeroe();
        }   
    }

    private void switchLabelVisible(ArrayList<JComponent> listaComponentes) {
        for (int i = 0; i < listaComponentes.size(); i++) {
            JComponent componente = listaComponentes.get(i);
            componente.setVisible(!componente.isVisible());
        }
    }

    private int probabilidadAntiheroe() {
        AntiHeroe antiheroe = (AntiHeroe) heroeAntiheroe;
        Villano villanoActual = (Villano) this.villano;
        if(villanoActual.getNombreVillano().equals(antiheroe.getArchienemigo())){
            return 50;
        }
        switch (villanoActual.getTipo()) {
            case "Social":
                return 80;
            case "Económico":
                return 40;
            default:
                return 0;
        }
    }

    private int probabilidadHeroe() {
        Heroe heroe = (Heroe) heroeAntiheroe;
        Villano villanoActual = (Villano) this.villano;
        if(villanoActual.getNombreVillano().equals(heroe.getArchienemigo())){
            return 50;
        }
        switch (villanoActual.getTipo()) {
            case "Social":
                return 40;
            case "Económico":
                return 80;
            default:
                return 0;
        }
    }

    private void gane(int num) {
        int numRondas = Integer.valueOf(rondas.getText());
        String toString = String.valueOf(numRondas-1);
        rondas.setText(toString);
        if(num < probabilidad){
            int toInt = Integer.valueOf(rondasGanadasHeroe.getText());
            rondasGanadasHeroe.setText(String.valueOf(toInt+1));
        }else{
            int toInt = Integer.valueOf(rondasGanadasVillano.getText());
            rondasGanadasVillano.setText(String.valueOf(toInt+1));            
        }
        
    }
}

