package src;

import java.util.ArrayList;

/**
 *
 * Clase Marca Contiene Categorias.
 *
 * @author Darío Vargas
 *
 * @version 1.0
 */
public class Marca {

//Atributos
    private ArrayList<String> categorias = new ArrayList<String>();// ArrayList con las categorias

//Metodos
    /**
     * Modifica la categoria
     *
     * @param pCategoria
     */
    public void agregarCategoria(String pCategoria) {
        categorias.add(pCategoria);
    }

    /**
     * Elimina una categoria de un indice especifico
     *
     * @param pIndice
     */
    public void eliminarCategoria(int pIndice) {
        categorias.remove(pIndice);
    }

    /**
     * Devuelve un String con la categoria de un indice específico
     *
     * @param pIndice
     * @return categoriaAtIndex
     */
    public String getCategoria(int pIndice) {
        String categoriaAtIndex = categorias.get(pIndice);
        return categoriaAtIndex;
    }

    /**
     * Devuelve un ArrayList con las categorias
     *
     * @return categorias
     */
    public ArrayList<String> getCategorias() {
        return categorias;
    }

}
