/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package intefaz;

/**
 *
 * @author dario
 */
public class Main extends javax.swing.JFrame {

    /**
     * Creates new form Main
     */
    public Main() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        bg = new javax.swing.JPanel();
        sidePanel = new javax.swing.JPanel();
        configMarcas = new javax.swing.JPanel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        configModelos = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        registroEmpleados = new javax.swing.JPanel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        registroClientes = new javax.swing.JPanel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        registroVehiculoCliente = new javax.swing.JPanel();
        jLabel9 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        registroServiciosTaller = new javax.swing.JPanel();
        jLabel11 = new javax.swing.JLabel();
        jLabel12 = new javax.swing.JLabel();
        consultaServicios = new javax.swing.JPanel();
        jLabel13 = new javax.swing.JLabel();
        jLabel14 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        bg.setBackground(new java.awt.Color(255, 255, 255));
        bg.setForeground(new java.awt.Color(255, 255, 255));

        sidePanel.setBackground(new java.awt.Color(38, 109, 211));
        sidePanel.setForeground(new java.awt.Color(57, 160, 237));
        sidePanel.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        configMarcas.setBackground(new java.awt.Color(38, 109, 211));
        configMarcas.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                configMarcasMouseClicked(evt);
            }
        });

        jLabel3.setIcon(new javax.swing.ImageIcon(getClass().getResource("/intefaz/icons/icons8-bmw-96 (1).png"))); // NOI18N

        jLabel4.setFont(new java.awt.Font("Noto Sans", 0, 24)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(255, 255, 255));
        jLabel4.setText("Configuración de marcas");

        javax.swing.GroupLayout configMarcasLayout = new javax.swing.GroupLayout(configMarcas);
        configMarcas.setLayout(configMarcasLayout);
        configMarcasLayout.setHorizontalGroup(
            configMarcasLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(configMarcasLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel3)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel4)
                .addContainerGap())
        );
        configMarcasLayout.setVerticalGroup(
            configMarcasLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jLabel3)
            .addGroup(configMarcasLayout.createSequentialGroup()
                .addGap(29, 29, 29)
                .addComponent(jLabel4))
        );

        sidePanel.add(configMarcas, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, -1, -1));

        configModelos.setBackground(new java.awt.Color(38, 109, 211));
        configModelos.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/intefaz/icons/icons8-tesla-model-x-configure-96.png"))); // NOI18N
        configModelos.add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(12, 12, -1, -1));

        jLabel2.setFont(new java.awt.Font("Noto Sans", 0, 24)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(255, 255, 255));
        jLabel2.setText("Configuración de modelos");
        configModelos.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(114, 40, -1, -1));

        sidePanel.add(configModelos, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 98, -1, 110));

        registroEmpleados.setBackground(new java.awt.Color(38, 109, 211));

        jLabel7.setIcon(new javax.swing.ImageIcon(getClass().getResource("/intefaz/icons/icons8-businessman-96.png"))); // NOI18N

        jLabel8.setFont(new java.awt.Font("Noto Sans", 0, 24)); // NOI18N
        jLabel8.setForeground(new java.awt.Color(255, 255, 255));
        jLabel8.setText("Registro de empleados");

        javax.swing.GroupLayout registroEmpleadosLayout = new javax.swing.GroupLayout(registroEmpleados);
        registroEmpleados.setLayout(registroEmpleadosLayout);
        registroEmpleadosLayout.setHorizontalGroup(
            registroEmpleadosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroEmpleadosLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel7)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel8))
        );
        registroEmpleadosLayout.setVerticalGroup(
            registroEmpleadosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroEmpleadosLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(registroEmpleadosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, registroEmpleadosLayout.createSequentialGroup()
                        .addComponent(jLabel7)
                        .addContainerGap())
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, registroEmpleadosLayout.createSequentialGroup()
                        .addComponent(jLabel8)
                        .addGap(41, 41, 41))))
        );

        sidePanel.add(registroEmpleados, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 210, -1, -1));

        registroClientes.setBackground(new java.awt.Color(38, 109, 211));

        jLabel5.setIcon(new javax.swing.ImageIcon(getClass().getResource("/intefaz/icons/icons8-user-96.png"))); // NOI18N

        jLabel6.setFont(new java.awt.Font("Noto Sans", 0, 24)); // NOI18N
        jLabel6.setForeground(new java.awt.Color(255, 255, 255));
        jLabel6.setText("Registro de clientes");

        javax.swing.GroupLayout registroClientesLayout = new javax.swing.GroupLayout(registroClientes);
        registroClientes.setLayout(registroClientesLayout);
        registroClientesLayout.setHorizontalGroup(
            registroClientesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroClientesLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel5)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel6))
        );
        registroClientesLayout.setVerticalGroup(
            registroClientesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroClientesLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel5)
                .addContainerGap())
            .addGroup(registroClientesLayout.createSequentialGroup()
                .addGap(43, 43, 43)
                .addComponent(jLabel6)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        sidePanel.add(registroClientes, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 320, -1, -1));

        registroVehiculoCliente.setBackground(new java.awt.Color(38, 109, 211));

        jLabel9.setIcon(new javax.swing.ImageIcon(getClass().getResource("/intefaz/icons/icons8-carpool-96.png"))); // NOI18N

        jLabel10.setFont(new java.awt.Font("Noto Sans", 0, 24)); // NOI18N
        jLabel10.setForeground(new java.awt.Color(255, 255, 255));
        jLabel10.setText("Registro del vehículo del cliente");

        javax.swing.GroupLayout registroVehiculoClienteLayout = new javax.swing.GroupLayout(registroVehiculoCliente);
        registroVehiculoCliente.setLayout(registroVehiculoClienteLayout);
        registroVehiculoClienteLayout.setHorizontalGroup(
            registroVehiculoClienteLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroVehiculoClienteLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel9)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel10)
                .addContainerGap(24, Short.MAX_VALUE))
        );
        registroVehiculoClienteLayout.setVerticalGroup(
            registroVehiculoClienteLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroVehiculoClienteLayout.createSequentialGroup()
                .addComponent(jLabel9)
                .addGap(0, 10, Short.MAX_VALUE))
            .addGroup(registroVehiculoClienteLayout.createSequentialGroup()
                .addGap(29, 29, 29)
                .addComponent(jLabel10)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        sidePanel.add(registroVehiculoCliente, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 430, -1, 106));

        registroServiciosTaller.setBackground(new java.awt.Color(38, 109, 211));

        jLabel11.setIcon(new javax.swing.ImageIcon(getClass().getResource("/intefaz/icons/icons8-car-service-96.png"))); // NOI18N

        jLabel12.setFont(new java.awt.Font("Noto Sans", 0, 24)); // NOI18N
        jLabel12.setForeground(new java.awt.Color(255, 255, 255));
        jLabel12.setText("Registro de servicios de taller");

        javax.swing.GroupLayout registroServiciosTallerLayout = new javax.swing.GroupLayout(registroServiciosTaller);
        registroServiciosTaller.setLayout(registroServiciosTallerLayout);
        registroServiciosTallerLayout.setHorizontalGroup(
            registroServiciosTallerLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroServiciosTallerLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel11)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel12))
        );
        registroServiciosTallerLayout.setVerticalGroup(
            registroServiciosTallerLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(registroServiciosTallerLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(registroServiciosTallerLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, registroServiciosTallerLayout.createSequentialGroup()
                        .addComponent(jLabel11)
                        .addContainerGap())
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, registroServiciosTallerLayout.createSequentialGroup()
                        .addComponent(jLabel12)
                        .addGap(47, 47, 47))))
        );

        sidePanel.add(registroServiciosTaller, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 530, -1, 114));

        consultaServicios.setBackground(new java.awt.Color(38, 109, 211));

        jLabel13.setIcon(new javax.swing.ImageIcon(getClass().getResource("/intefaz/icons/icons8-search-96.png"))); // NOI18N

        jLabel14.setFont(new java.awt.Font("Noto Sans", 0, 24)); // NOI18N
        jLabel14.setForeground(new java.awt.Color(255, 255, 255));
        jLabel14.setText("Consulta de servicio");

        javax.swing.GroupLayout consultaServiciosLayout = new javax.swing.GroupLayout(consultaServicios);
        consultaServicios.setLayout(consultaServiciosLayout);
        consultaServiciosLayout.setHorizontalGroup(
            consultaServiciosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(consultaServiciosLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel13)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel14))
        );
        consultaServiciosLayout.setVerticalGroup(
            consultaServiciosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(consultaServiciosLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(consultaServiciosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, consultaServiciosLayout.createSequentialGroup()
                        .addComponent(jLabel13)
                        .addContainerGap())
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, consultaServiciosLayout.createSequentialGroup()
                        .addComponent(jLabel14)
                        .addGap(47, 47, 47))))
        );

        sidePanel.add(consultaServicios, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 640, -1, 114));

        javax.swing.GroupLayout bgLayout = new javax.swing.GroupLayout(bg);
        bg.setLayout(bgLayout);
        bgLayout.setHorizontalGroup(
            bgLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(bgLayout.createSequentialGroup()
                .addComponent(sidePanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(789, Short.MAX_VALUE))
        );
        bgLayout.setVerticalGroup(
            bgLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(sidePanel, javax.swing.GroupLayout.PREFERRED_SIZE, 760, javax.swing.GroupLayout.PREFERRED_SIZE)
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(bg, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(bg, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void configMarcasMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_configMarcasMouseClicked
        // TODO add your handling code here:
    }//GEN-LAST:event_configMarcasMouseClicked

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Main().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel bg;
    private javax.swing.JPanel configMarcas;
    private javax.swing.JPanel configModelos;
    private javax.swing.JPanel consultaServicios;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel14;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel registroClientes;
    private javax.swing.JPanel registroEmpleados;
    private javax.swing.JPanel registroServiciosTaller;
    private javax.swing.JPanel registroVehiculoCliente;
    private javax.swing.JPanel sidePanel;
    // End of variables declaration//GEN-END:variables
}
