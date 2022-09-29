
import java.util.ArrayList;

/*
 * Clase marca con todas las características 
 * que posee una marca.
 */
/**
 *
 * @author Darío Vargas
 * @version %I%
 */
public class Marcas {
    // Variables

    private ArrayList<String> categorias;// Lista de categorias

    //Métodos
    /**
     *
     * @param pCategoria String con la categoría a agregar.
     */
    public void agregarCategoria(String pCategoria) {
        categorias.add(pCategoria);
    }

    /**
     * 
     * @param pIndice El indice donde se encuentra la categoría a eliminar.
     */
    public void eliminarCategoria(int pIndice) {
        categorias.remove(pIndice);
    }

    
    /**
     * 
     * @param pIndice El indice donde se encuentra la categoría a obtener.
     * @return Un String con el nombre de la categoría.
     */
    public String getCategoria(int pIndice){
        return categorias.get(pIndice);
    }
    
    
    /**
     * 
     * @return Un ArrayList<String> con todas las categorías.
     */
    public ArrayList<String> getCategrias(){
        return categorias;
    }
}
