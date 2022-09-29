package modelo;
import java.awt.BorderLayout;
import java.awt.Color;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

    public class GamePane extends JPanel {

        private BoardPane boardPane;
        private JLabel label;
        private CuatroEnLinea logica;
        private Tablero.Player player = null;

        public GamePane(CuatroEnLinea logica) {
            this.logica = logica;
            setLayout(new BorderLayout());
            boardPane = new BoardPane(logica);
            add(boardPane);

            label = new JLabel("...");
            label.setHorizontalAlignment(JLabel.CENTER);
            label.setForeground(Color.WHITE);
            label.setOpaque(true);
            label.setBorder(new EmptyBorder(10, 10, 10, 10));

            add(label, BorderLayout.NORTH);

            updatePlayer();

            boardPane.addChangeListener(new ChangeListener() {
                @Override
                public void stateChanged(ChangeEvent e) {
                    updatePlayer();
                }
            });
        }

        protected void updatePlayer() {
            String text = "...";
            Color color = null;
            if (player == null || player.equals(Tablero.Player.BLUE)) {
                player = Tablero.Player.RED;
                text = "Red";
                color = Color.RED;
            } else if (player.equals(Tablero.Player.RED)) {
                player = Tablero.Player.BLUE;
                text = "Blue";
                color = Color.BLUE;
            }

            label.setText(text);
            label.setBackground(color);
            boardPane.setPlayer(player);
            boardPane.setLogica(logica);
        }

    }