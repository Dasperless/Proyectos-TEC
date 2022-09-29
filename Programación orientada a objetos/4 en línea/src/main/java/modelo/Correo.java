/**
 *
 * @author Darío Vargas Montoya
 */
package modelo;

import java.util.Properties;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class Correo {

    private String destinatario;
    private String asunto;
    private String contenido;
    private final String username = "equipocuatroenlinea@gmail.com";
    private final String password = "Equipo4EnLinea";

    public Correo(String destinatario, String asunto, String contenido) {
        this.destinatario = destinatario;
        this.asunto = asunto;
        this.contenido = contenido;
    }

    public void enviarEmail() {
        Properties props = new Properties();
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", "smtp.gmail.com");
        props.put("mail.smtp.ssl.trust", "smtp.gmail.com");
        props.put("mail.smtp.port", "587");

        Session session = Session.getInstance(props,
                new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });

        try {

            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(username));
            message.setRecipients(Message.RecipientType.TO,InternetAddress.parse(destinatario)); // Destinatario
            message.setSubject(asunto);
            message.setText(contenido);

            Transport.send(message);

        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
    }

}
