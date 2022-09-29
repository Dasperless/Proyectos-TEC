/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package modelo;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Clase contraseña que genera una contraseña aleatorea
 *
 * @author dario
 */
public class Contraseña {

    private int largoPredeterminado = 10;
    private String numeros = "123456789";
    private String mayusculas = "abcdefghijklmnopqrstuvwxyz";
    private String minusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public Contraseña() {
    }

    public String generarContraseña() {
        String contraseña = "";
        ArrayList<String> token = new ArrayList<>(Arrays.asList("numeros", "minusculas", "mayusculas"));
        for (int i = 0; i < largoPredeterminado; i++) {
            String tipoToken = token.get(numeroAleatorio(token.size(), 0));
            switch (tipoToken) {
                case "numeros":
                    contraseña += numeros.charAt(numeroAleatorio(numeros.length(),0));
                    break;
                case "minusculas":
                    contraseña += minusculas.charAt(numeroAleatorio(minusculas.length(),0));
                    break;
                case "mayusculas":
                    contraseña += mayusculas.charAt(numeroAleatorio(mayusculas.length(),0));
                    break;
            }
        }
        return contraseña;
    }

    private int numeroAleatorio(int numMax, int numMin) {
        int numero = (int) (Math.random() * numMax + numMin);
        return numero;
    }

}
