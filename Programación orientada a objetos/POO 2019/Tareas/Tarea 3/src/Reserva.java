/**
 * Clase Reserva
 * 
 * @author Darío Vargas
 * @version 1.0.0
 */
public class Reserva {

    /** Número de cédula de la persona */
    public int cedula;

    /** Libro que desea reservar */
    public Libro libro;

    /** La fecha que se reservó el libro */
    public String fechaReserva;

    /** La fecha que se entregó el libro */
    public String fechaEntrega;

    /** El codigo con el que se reserva el libro */
    public int codigoReserva = 0;

    Reserva(int pCedula, Libro pLibro, String pFechaReserva, String pFechaEntrega) {
        setCedula(pCedula);
        setLibro(pLibro);
        setFechaEntrega(pFechaEntrega);
        setFechaReserva(pFechaReserva);
        codigoReserva++;
    }

    /**
     * @param pCedula Un int con el número de cédula de la persona.
     */
    public void setCedula(int pCedula) {
        cedula = pCedula;
    }

    /**
     * @param pLibro Un Libro que representa el libro que se va a reservar.
     */
    public void setLibro(Libro pLibro) {
        libro = pLibro;
    }

    /**
     * @param pfechaEntrega Un String con la fecha de entrega.
     */
    public void setFechaEntrega(String pfechaEntrega) {
        fechaEntrega = pfechaEntrega;
    }

    /**
     * @param pCodigoReserva Un int con codigo que reserva del libro
     */
    public void setCodigoReserva(int pCodigoReserva) {
        codigoReserva = pCodigoReserva;
    }

    /**
     * @param pFechaReserva
     */
    public void setFechaReserva(String pFechaReserva) {
        fechaReserva = pFechaReserva;
    }

    /**
     * @return Retorna un int con el número de cédula de quien reserva el libro.
     */
    public int getCedula() {
        return cedula;
    }

    /**
     * @return Retorna un int con el código de la reserva.
     */
    public int getCodigoReserva() {
        return codigoReserva;
    }

    /**
     * @return Retorna un String con la fecha de entrega.
     */
    public String getFechaEntrega() {
        return fechaEntrega;
    }

    /**
     * @return Retorna un String con la fecha de Reserva.
     */
    public String getFechaReserva() {
        return fechaReserva;
    }

    /**
     * @return Retorna un objeto de tipo Libro.
     */
    public Libro getLibro() {
        return libro;
    }

    public String toString() {
        String msj = "";
        msj += "\tReserva # " + getCodigoReserva() + "\n";
        msj += "Cedula de la persona:" + getCedula() + "\n";
        msj += "Libro: " + getLibro().getTitulo() + "\n";
        msj += "Fecha de reserva: " + getFechaReserva() + "\n";
        msj += "Fecha de entrega: " + getFechaEntrega() + "\n";
        return msj;
    }

}