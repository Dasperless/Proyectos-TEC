import java.util.ArrayList;

/**
 * Clase Biblioteca
 * 
 * @author Darío Vargas
 * @version 1.0.0
 */
public class Biblioteca {

    /** Nombre de la biblioteca */
    public String biblioteca;
    /** Horario de la biblioteca */
    public String horarioBiblioteca;
    /** Correo de la biblioteca */
    public String correo;
    /** Teléfono de la biblioteca */
    public int telefono;
    /** Array con los libros de la biblioteca */
    public ArrayList<Libro> libros = new ArrayList<>();
    /** Reservas de la biblioteca */
    public ArrayList<Reserva> reservas = new ArrayList<>();

    Biblioteca(String pNombre, String pHorario, String pCorreo, int pNumero) {
        setBiblioteca(pNombre);
        setHorarioBiblioteca(pHorario);
        setCorreo(pCorreo);
        setTelefono(pNumero);
    }

    /** Sección de Metodos */

    /**
     * 
     * @param pCedula         Un int con el número de cédula de la persona que
     *                        reserva el libro.
     * @param pCodigoLibro    Un int con el codigo del libro a reservar.
     * @param pFechaSolicitud Un String con la fecha de solicitud del libro.
     * @param pFechaEntrega   Un String con la fecha de entrega del libro.
     * @return Un entero con el código de reserva. Si hay un error retorna 0.
     */

    public int crearReserva(int pCedula, int pCodigoLibro, String pFechaSolicitud, String pFechaEntrega) {
        int indice = pCodigoLibro - 1;
        if (indice >= libros.size() || indice < 0) {
            System.out.println("No existe el código del libro.");
            return 0;
        }

        Libro libroReserva = libros.get(indice);
        if (libroReserva.getEstaDisponible()) {
            libroReserva.setEstaDisponible(false);
            Reserva nuevaReserva = new Reserva(pCedula, libroReserva, pFechaSolicitud, pFechaEntrega);
            agregarReserva(nuevaReserva);
            return nuevaReserva.getCodigoReserva();
        } else {
            System.out.println("El libro no está disponible");
            return 0;
        }

    }

    /**
     * 
     * @param pNumReserva Un int con el código de reserva.
     */
    public void liberarReserva(int pNumReserva) {
        int indice = pNumReserva - 1;
        if (indice >= reservas.size() || indice < 0) {
            System.out.println("No existe el número de reserva.");
        }
        Reserva reserva = reservas.remove(indice);
        reserva.getLibro().setEstaDisponible(true);
    }

    /**
     * 
     * @param pLista La lista a comparar
     * @param pValor El valor que se desea coprobar que existe en la lista
     * @return Retorna la posición en la que se encuentra, si no se encuentra
     *         retorna -1.
     */
    public int contains(String[] pLista, String pValor) {
        for (int i = 0; i < pLista.length; i++) {
            if (pLista[i].equals(pValor)) {
                return i;
            }
        }
        return -1;
    }

    /**
     * 
     * @param pFecha1 La primer fecha a comparar.
     * @param pFecha2 La segunda fecha a comparar.
     * @return retorna true si la primera fecha es menor o igual a la segunda fecha.
     */
    public Boolean verificarFecha(String pFecha1, String pFecha2) {
        String[] meses = { "En", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ag", "Set", "Oct", "Nov", "Dic" };
        int numDia1 = Integer.valueOf(pFecha1.substring(0, 2));
        String mesFecha1 = pFecha1.substring(5);
        int numDia2 = Integer.valueOf(pFecha2.substring(0, 2));
        String mesFecha2 = pFecha1.substring(5);

        if (numDia1 <= numDia2 && (contains(meses, mesFecha1) <= contains(meses, mesFecha2))) {

            return true;
        }
        return false;

    }

    /**
     * 
     * @return Retorna un String con todos los libros disponibles
     */
    public String imprimirLibros() {
        String msj = "";
        msj += "\tLibros disponibles\n";
        for (int i = 0; i < libros.size(); i++) {
            if (libros.get(i).getEstaDisponible()) {
                msj += libros.get(i).getTitulo() + "\n";
            }
        }
        return msj;
    }

    /**
     * 
     * @param pFecha Fecha limite a imprimir.
     * @return Un String con todas las reservas a partir de una fecha.
     */
    public String imprimirReservas(String pFecha) {
        String msj = "";
        msj += "\tReservas\n";
        for (int i = 0; i < reservas.size(); i++) {
            if (verificarFecha(pFecha, reservas.get(i).getFechaEntrega())) {
                msj += reservas.get(i).toString() + "\n";
            }
        }

        if (msj.equals("")) {
            msj = "No se encontraron reservas vigentes para la fecha " + pFecha;
        }

        return msj;
    }

    /** Sección de getters y setters */

    /**
     * 
     * @param pLibro El libro a agregar a la biblioteca.
     */
    void agregarLibro(Libro pLibro) {
        libros.add(pLibro);
    }

    /**
     * @param pReserva Un objeto de tipo reserva a guardar en el ArrayList de
     *                 reservas.
     */
    void agregarReserva(Reserva pReserva) {
        reservas.add(pReserva);
    }

    /**
     * @param pBiblioteca the biblioteca to set
     */
    public void setBiblioteca(String pBiblioteca) {
        biblioteca = pBiblioteca;
    }

    /**
     * @param pCorreo Un String con el correo.
     */
    public void setCorreo(String pCorreo) {
        correo = pCorreo;
    }

    /**
     * @param pHorario Un String con el horario.
     */
    public void setHorarioBiblioteca(String pHorario) {
        horarioBiblioteca = pHorario;
    }

    /**
     * @param pTelefono Un int con el número de telefono.
     */
    public void setTelefono(int pTelefono) {
        telefono = pTelefono;
    }

    /**
     * @return Retorna un String con el nombre de la biblioteca.
     */
    public String getBiblioteca() {
        return biblioteca;
    }

    /**
     * @return Retorna un String con el correo de la biblioteca.
     */
    public String getCorreo() {
        return correo;
    }

    /**
     * @return Retorna un String con el horario de la biblioteca.
     */
    public String getHorarioBiblioteca() {
        return horarioBiblioteca;
    }

    /**
     * @return Retorna un ArrayList con los libros.
     */
    public ArrayList<Libro> getLibros() {
        return libros;
    }

    /**
     * @return Retorna ArrayList con las reservas que se realizaron en la
     *         biblioteca.
     */
    public ArrayList<Reserva> getReservas() {
        return reservas;
    }

    /**
     * @return Retorna un int con el número de la biblioteca.
     */
    public int getTelefono() {
        return telefono;
    }

}