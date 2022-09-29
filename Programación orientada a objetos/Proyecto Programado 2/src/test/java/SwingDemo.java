import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import javax.swing.Timer;

public class SwingDemo extends JPanel {
    private final JButton button;
    private final Timer stopwatch;
    private final int SEC = 10;

    public SwingDemo() {
        button = new JButton("Click me to disable for " + SEC + " secs");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JButton toDisable = (JButton) e.getSource();
                toDisable.setEnabled(false);
                stopwatch.start();
            }
        });
        add(button);
        stopwatch = new Timer(SEC * 1000, new MyTimerListener(button));
        stopwatch.setRepeats(false);
    }

    static class MyTimerListener implements ActionListener {
        JComponent target;

        public MyTimerListener(JComponent target) {
            this.target = target;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            target.setEnabled(true);
        }

    }

    public static void main(String[] args) {
        final JFrame myApp = new JFrame();
        myApp.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myApp.setContentPane(new SwingDemo());
        myApp.pack();
        SwingUtilities.invokeLater(new Runnable() {

            @Override
            public void run() {
                myApp.setVisible(true);
            }
        });
    }
}
