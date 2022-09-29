/**
 * Clase Libro
 * 
 * @author Darío Vargas
 * @version 1.0.0
 */
public class Libro {

    /** Un número único y consecutivo que identifica al libro. */
    private int id = 0;
    /** El ISBN del libro. */
    public String isbn;
    /** El título del libro. */
    public String titulo;
    /** El autor del libro. */
    public String autor;
    /** La cantidad de páginas del libro. */
    public int numPaginas;
    /** Un valor booleano que indica si está disponible o no. */
    public boolean estaDisponible;

    Libro(String pIsbn, String pTitulo, String pAutor, int pNumPaginas, boolean pDisponible) {
        setIsbn(pIsbn);
        setTitulo(pTitulo);
        setAutor(pAutor);
        setNumPaginas(pNumPaginas);
        setEstaDisponible(pDisponible);
        id++;
    }

    /**
     * 
     * @param pIsbn El ISBN del libro.
     */
    public void setIsbn(String pIsbn) {
        isbn = pIsbn;
    }

    /**
     * 
     * @param pTitulo El titulo del libro.
     */
    public void setTitulo(String pTitulo) {
        titulo = pTitulo;
    }

    /**
     * 
     * @param pAutor El autor del libro.
     */
    public void setAutor(String pAutor) {
        autor = pAutor;
    }

    /**
     * 
     * @param pNumPaginas El número de páginas que posee el libro.
     */
    public void setNumPaginas(int pNumPaginas) {
        numPaginas = pNumPaginas;
    }

    /**
     * 
     * @param pDisponible Un valor booleano si el libro esta disponible o no.
     */
    public void setEstaDisponible(Boolean pDisponible) {
        estaDisponible = pDisponible;
    }

    /**
     * @return El código consecutivo del libro.
     */
    public int getId() {
        return id;
    }

    /**
     * @return Un entero con el ISBN del libro.
     */
    public String getIsbn() {
        return isbn;
    }

    /**
     * @return Un String con el titulo del libro.
     */
    public String getTitulo() {
        return titulo;
    }

    /**
     * @return Un String con el autor del libro.
     */
    public String getAutor() {
        return autor;
    }

    /**
     * @return Un entero con el número de paginas del libro.
     */
    public int getNumPaginas() {
        return numPaginas;
    }

    /**
     * 
     * @return Retorna true si está disponible, false en el caso contrario.
     */
    public Boolean getEstaDisponible() {
        return estaDisponible;
    }

    /**
     * @return Un string con los datos del libro.
     */
    public String toString() {
        String msj = "";
        msj = "El libro " + getTitulo() + "con el id " + getId() + " y con el ISBN " + getIsbn()
                + ", creado por el autor " + getAutor() + " tiene " + getNumPaginas() + " páginas y ";
        if (getEstaDisponible()) {
            msj += "Está disponible.";
        } else {
            msj += "No está disponible.";
        }
        return msj;
    }

}