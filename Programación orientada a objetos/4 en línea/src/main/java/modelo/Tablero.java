package modelo;

import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;
import sockets.Cliente;
import sockets.Servidor;

public class Tablero {

//    public static void main(String[] args) {
//        new ConnectFour();
//    }
    public Tablero(CuatroEnLinea logica) {

        EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                try {
                    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
                } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException ex) {
                    ex.printStackTrace();
                }

                JFrame frame = new JFrame("Cuatro en linea");
                frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                frame.add(new GamePane(logica));
                frame.pack();
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
                frame.setSize(1920, 1080);

                if (logica.getJugador1().getConexion() instanceof Servidor) {
                    popUpMessage.infoBox("Esperando Jugador 2", "Ganador");
                    Servidor servidor = (Servidor) logica.getJugador1().getConexion();
                    servidor.startServer();

                } else {
                    Cliente cliente = (Cliente) logica.getJugador1().getConexion();
                    cliente.startClient();
                }

            }

        });

    }

    public enum Player {

        RED, BLUE, NONE;
    }
}
