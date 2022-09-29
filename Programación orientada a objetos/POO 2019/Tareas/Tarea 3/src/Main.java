/**
 * Clase LibroApp
 * 
 * @author Darío Vargas
 * @version 2.0.0
 */

public class Main {
    public static void main(String[] args) {
        Biblioteca nuevaBiblioteca = new Biblioteca("Biblioteca Babilonia", "De lunes a viernes de 7:00 AM a 8:00 PM",
                "Babilonia@gmail.com", 27300100);

        Libro marvel = new Libro("1465478906", "Marvel Encyclopedia, New Edition", "Stan Lee", 448, true);
        nuevaBiblioteca.agregarLibro(marvel);
        System.out.println(marvel.toString());

        Libro dcComics = new Libro("1465479759", "DC Comics Ultimate Character Guide, New Edition", "Melanie Scott",
                216, true);
        nuevaBiblioteca.agregarLibro(dcComics);
        System.out.println(dcComics.toString());

        Libro heroAcademia = new Libro("8416693501", "My Hero Academia nº 01: 210 (Manga Shonen)", "Kohei Horikoshi",
                192, true);
        nuevaBiblioteca.agregarLibro(heroAcademia);
        System.out.println(heroAcademia.toString());

        Libro ataqueTitanes = new Libro("8467937025", "Ataque A Los Titanes 27", "Hajime Isayama", 188, true);
        nuevaBiblioteca.agregarLibro(ataqueTitanes);
        System.out.println(ataqueTitanes.toString());

        Libro guardianasNoche = new Libro("8467935111", "Guardianes de la Noche 1", "Hajime Isayama", 192, true);
        nuevaBiblioteca.agregarLibro(guardianasNoche);
        System.out.println(guardianasNoche.toString());

        nuevaBiblioteca.crearReserva(117530565, 1, "10 – Set", "20 – Set ");
        nuevaBiblioteca.crearReserva(117530565, 2, "12 – Set", "15 – Set ");
        nuevaBiblioteca.crearReserva(117530565, 3, "18 – Set", "22 – Set ");
        nuevaBiblioteca.liberarReserva(2);

        System.out.println(nuevaBiblioteca.imprimirReservas("18 – Set"));
    }

    /**
     * System.out.println(numDial);
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