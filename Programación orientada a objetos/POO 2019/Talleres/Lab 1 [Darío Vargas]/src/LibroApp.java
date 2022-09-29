/**
 * Clase LibroApp
 * @author Darío Vargas
 * @version 1.0.0   
 */

public class LibroApp {
    /**
     * 
     * @param args
     */
    public static void main(String[] args) {
        Libro marvel = new Libro("1465478906", "Marvel Encyclopedia, New Edition", "Stan Lee", 448, true);
        System.out.println(marvel.toString());
        Libro dcComics = new Libro("1465479759", "DC Comics Ultimate Character Guide, New Edition", "Melanie Scott", 216, false);   
        System.out.println(dcComics.toString());
        
        System.out.println(compararPaginas(marvel,dcComics));
    }

    /**
     * 
     * @param libro1 El primer libro a comparar.
     * @param libro2 el segundo libro a comparar.
     * @return Un string con un mensaje que avisa cual tiene más paginas.
     */
    public static String compararPaginas(Libro libro1, Libro libro2) {
        String msj = "";

        if (libro1.getNumPaginas() > libro2.getNumPaginas()) {
            msj += "El libro " + libro1.getTitulo() + " tiene más paginas que " + libro2.getTitulo() + ".";
        } else if (libro1.getNumPaginas() == libro2.getNumPaginas()) {
            msj += "El libro " + libro1.getTitulo() + " y el libro " + libro2.getNumPaginas()
                    + " Tienen las misma cantidad de páginas.";
        } else {
            msj += "El libro " + libro2.getTitulo() + " tiene más páginas que " + libro1.getTitulo() + ".";
        }
        return msj;
    }
}