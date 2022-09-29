
package sockets;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Servidor extends Conexion //Se hereda de conexión para hacer uso de los sockets y demás
{
    /**
     * 
     */
    
    public void mensajeError(){
        System.out.println("Este es un mensaje de error que será cambiado por otra acción");
    }
    /**
     * 
     * @throws IOException 
     */
    public Servidor() throws IOException{super("servidor");} //Se usa el constructor para servidor de Conexion

    public void startServer()//Método para iniciar el servidor
    {
        try
        {
            System.out.println("Esperando..."); //Esperando conexión

            cs = ss.accept(); //Accept comienza el socket y espera una conexión desde un cliente

            System.out.println("Cliente en línea");

            //Se obtiene el flujo de salida del cliente para enviarle mensajes
            entradaCliente = new DataInputStream(cs.getInputStream());

            //Se le envía un mensaje al cliente usando su flujo de salida

            switch(entradaCliente.readUTF()){
                case "XD":  
                    System.out.println("Hola mundo");
                    break;
                default:   
                    System.out.println("Hola mundo esto es un mensaje de error");
                    break;
            }
            BufferedReader entrada = new BufferedReader(new InputStreamReader(cs.getInputStream()));

            while((mensajeServidor = entrada.readLine()) != null) //Mientras haya mensajes desde el cliente
            {
                //Se muestra por pantalla el mensaje recibido
                System.out.println(mensajeServidor);
            }

            System.out.println("Fin de la conexión");

            ss.close();//Se finaliza la conexión con el cliente
        }
        catch (IOException e)
        {
            System.out.println(e.getMessage());
        }
    }
}