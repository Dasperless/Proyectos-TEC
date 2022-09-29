/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package modelo;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

/**
 *
 * @author Paula Rubio
 */
public class Sesion {
    private final String directorio = "./src/main/java/usuarios/Usuarios.xml";
    private String contraseña; //Contraseña del usuario
    private String nombre; //Nombre del usuario
    private String apellido; //Apellido del usuario
    private String correo; //Correo del usuario
    private String partGanadas; //Partidas ganadas por el usuario
    private String partPerdidas; //Partidas perdidas por el usuario
    private String partEmpatadas; //Partidas empatadas por el usuario

    public Sesion() {

    }


    /**
     * Funcion que agrega los datos al XML
     *
     * @param pJugador // El jugador a guardar
     * @return Retorna true en el caso de que se haya registrado, false en el caso contrario
     */
    public boolean registrarJugador(Jugador pJugador) {
        try {
            getDatosJugador(pJugador);
            File dir = new File(directorio);
            DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
            Document documento = documentBuilder.parse(dir);
            documento.getDocumentElement().normalize();
            Element contraseña_in, nombre_in, apellido_in, correo_in, partGanadas_in, partEmpatadas_in, partPerdidas_in;
            if (correoValido(correo)) {
                
                NodeList lista = documento.getElementsByTagName("Usuarios");
                Element elemento;
                for (int i = 0; i < lista.getLength(); i++) {
                    elemento = (Element) lista.item(i);
                    Element usua = documento.createElement("Usuario");
//                    elemento.appendChild(usua);
                    
                    //Creamos los nodos necesario
                    contraseña_in = documento.createElement("Contraseña");
                    nombre_in = documento.createElement("Nombre");
                    apellido_in = documento.createElement("Apellido");
                    correo_in = documento.createElement("Correo");
                    partGanadas_in = documento.createElement("PartidasGanadas");
                    partEmpatadas_in = documento.createElement("PartidasEmpatadas");
                    partPerdidas_in = documento.createElement("PartidasPerdidas");
                    
                    //insertamos la información
                    contraseña_in.appendChild(documento.createTextNode(contraseña));
                    nombre_in.appendChild(documento.createTextNode(nombre));
                    apellido_in.appendChild(documento.createTextNode(apellido));
                    correo_in.appendChild(documento.createTextNode(correo));
                    partGanadas_in.appendChild(documento.createTextNode(partGanadas));
                    partEmpatadas_in.appendChild(documento.createTextNode(partEmpatadas));
                    partPerdidas_in.appendChild(documento.createTextNode(partPerdidas));
                    
                    //agrega los nodos al padre correspondiente
                    usua.appendChild(contraseña_in);
                    usua.appendChild(nombre_in);
                    usua.appendChild(apellido_in);
                    usua.appendChild(correo_in);
                    usua.appendChild(partGanadas_in);
                    usua.appendChild(partEmpatadas_in);
                    usua.appendChild(partPerdidas_in);
                    elemento.appendChild(usua);                    
                    
                }
                
            } else{
                return false;
            }
            documento.getDocumentElement().normalize();
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
            DOMSource source = new DOMSource(documento);
            StreamResult result = new StreamResult(dir);
            transformer.transform(source, result);
        } catch (ParserConfigurationException | SAXException | IOException | TransformerException ex) {
            Logger.getLogger(Sesion.class.getName()).log(Level.SEVERE, null, ex);
        }
        return true;    
    }
/**
    *valida que el correo ingresado sea valido returna true si el correo no existe, false si ya existe
     * @param pCorreo
     * @return boolean
    */
    public boolean correoValido(String pCorreo) {
        File dir = new File(directorio);
        if (dir.exists()){
            try {
                DocumentBuilderFactory documentBuilderFactory= DocumentBuilderFactory.newInstance();
                DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
                Document documento = documentBuilder.parse(dir);
                documento.getDocumentElement().normalize();
                NodeList list = documento.getElementsByTagName("Usuario");
                for (int i = 0; i<list.getLength();i++){
                    Element elemento = (Element) list.item(i);
                    String hijo = elemento.getElementsByTagName("Correo").item(0).getTextContent();
                    if (pCorreo.toLowerCase().equals(hijo.toLowerCase())){
                        return false;
                    }
                }
                return true;
            } catch (SAXException | IOException | ParserConfigurationException ex) {
                Logger.getLogger(Sesion.class.getName()).log(Level.SEVERE, null, ex);
            }
            
        }
        return true;
        
    }    
    
    public Jugador iniciarSesion(String pUsuario, String pContraseña){
        ArrayList<ArrayList<String>> usuarios = listaUsuarios();
        for(int i = 0 ; i< usuarios.size(); i++){
            Jugador jugador = getUsuario(usuarios.get(i));
            if(pUsuario.equals(jugador.getNombre()) && pContraseña.equals(jugador.getContraseña())){
                return jugador;
            }
        }
        return null;
    }
    
    public Jugador getUsuario(ArrayList<String> pDatosUsuario){
        Jugador jugador = new Jugador();
        for(int  i = 0; i< pDatosUsuario.size(); i++){
            String dato = pDatosUsuario.get(i);
            switch(i){
                case 0:
                    jugador.setContraseña(dato);
                    break;
                case 1:
                    jugador.setNombre(dato);
                    break;
                case 2:
                    jugador.setApellidos(dato);
                    break;
                case 3:
                    jugador.setCorreo(dato);
                    break;
                case 4:
                    jugador.setPartidasGanadas(dato);
                    break;
                case 5:
                    jugador.setPartidasEmpatadas(dato);
                    break;
                case 6:
                    jugador.setPartidasPerdidas(dato);
                    break;
                default:
                    System.out.println("No existe la opcion");
                    break;
                
            }
        }
        
        return jugador;
    }
    /**
     * Extrae todo los usuarios del XML
     *
     * @return un Arreglo con arreglos de Strings
     */
    public ArrayList<ArrayList<String>> listaUsuarios(){
        
        ArrayList<ArrayList<String>> res = new ArrayList<>();
        File dir = new File(directorio);
        if (dir.exists()) {
            try {
                DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
                DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
                Document documento = documentBuilder.parse(dir);
                documento.getDocumentElement().normalize();
                //Ciclo que recorre una lista con los vuelos registrados
                NodeList Familias = documento.getElementsByTagName("Usuario");
                for (int i = 0; i < Familias.getLength(); i++) {
                    Element elemento = (Element) Familias.item(i);
                    ArrayList<String> sub = new ArrayList<>();
                    //Sacando info de cada elemento del XML
                    String contraObt = elemento.getElementsByTagName("Contraseña").item(0).getTextContent();
                    String nombreObt = elemento.getElementsByTagName("Nombre").item(0).getTextContent();
                    String apellidoObt = elemento.getElementsByTagName("Apellido").item(0).getTextContent();
                    String correoObt = elemento.getElementsByTagName("Correo").item(0).getTextContent();
                    String ganadasObt = elemento.getElementsByTagName("PartidasGanadas").item(0).getTextContent();
                    String empatadasObt = elemento.getElementsByTagName("PartidasEmpatadas").item(0).getTextContent();
                    String perdidasObt = elemento.getElementsByTagName("PartidasPerdidas").item(0).getTextContent();
                    //lo agrega a la sublista
                    sub.add(contraObt);
                    sub.add(nombreObt);
                    sub.add(apellidoObt);
                    sub.add(correoObt);
                    sub.add(ganadasObt);
                    sub.add(empatadasObt);
                    sub.add(perdidasObt);
                    //se agrega la sublista en el arreglo
                    res.add(sub);
                }
            } catch (ParserConfigurationException | SAXException | IOException ex) {
                Logger.getLogger(Sesion.class.getName()).log(Level.SEVERE, null, ex);
            }

        }
        return res;
    }

    /**
     * Elimina un usuario registrado
     *
     * @param apContraseña
     * @throws SAXException
     * @throws ParserConfigurationException
     * @throws IOException
     * @throws XPathExpressionException
     * @throws TransformerConfigurationException
     * @throws TransformerException
     */
    public void eliminarJugador(String apContraseña) throws SAXException, ParserConfigurationException, IOException, XPathExpressionException, TransformerConfigurationException, TransformerException {
        File dir = new File(directorio);
        if (dir.exists()) {
            DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
            Document documento = documentBuilder.parse(dir);
            documento.getDocumentElement().normalize();
            Node Marcas = documento.getFirstChild();
            NodeList marcas = documento.getElementsByTagName("Usuario");
            for (int i = 0; i < marcas.getLength(); i++) {
                Element elemento = (Element) marcas.item(i);
                String hijo = elemento.getElementsByTagName("Contraseña").item(0).getTextContent();
                if (apContraseña.equals(hijo)) {

                    elemento.getParentNode().removeChild(elemento);
                }
            }
            //Este ciclo elimina toda linea vacías en el XML
            XPath xp = XPathFactory.newInstance().newXPath();
            NodeList nl = (NodeList) xp.evaluate("//text()[normalize-space(.)='']", documento, XPathConstants.NODESET);
            for (int y = 0; y < nl.getLength(); ++y) {
                Node node = nl.item(y);
                node.getParentNode().removeChild(node);
            }
            //Guarda el archivo XML
            documento.getDocumentElement().normalize();
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(documento);
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
            StreamResult result = new StreamResult(dir);
            transformer.transform(source, result);

        }

    }

    /**
     * Modifica segun numero que se le envie, 0=nombre, 1=apellido, 2=correo,
     * 3=PartidasGanadas, 4=Partidas Empatadas, 5=Partidas perdidas
     *
     * @param contraseña: String
     * @param campo: Arreglo de String
     * @param determinar: int
     * @throws javax.xml.parsers.ParserConfigurationException
     * @throws org.xml.sax.SAXException
     * @throws java.io.IOException
     * @throws javax.xml.transform.TransformerConfigurationException
     */
    public void modificar(String contraseña, ArrayList<String> campo, int determinar) throws ParserConfigurationException, SAXException, IOException, TransformerConfigurationException, TransformerException {
        File dir = new File(directorio);
        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
        Document documento = documentBuilder.parse(dir);
        documento.getDocumentElement().normalize();
        Node Inicio = documento.getFirstChild();

        NodeList list = documento.getElementsByTagName("Usuario");
        //recorre lista de productos
        for (int i = 0; i < list.getLength(); i++) {
            Element elemento = (Element) list.item(i);
            String hijo = elemento.getElementsByTagName("Contraseña").item(0).getTextContent();
            if (contraseña.toLowerCase().equals(hijo.toLowerCase())) {
                //Actualización aquí
                if (determinar == 0) {
                    elemento.getElementsByTagName("Nombre").item(0).setTextContent(campo.get(0));
                } else if (determinar == 1) {
                    elemento.getElementsByTagName("Apellido").item(0).setTextContent(campo.get(0));
                } else if (determinar == 2) {
                    elemento.getElementsByTagName("Correo").item(0).setTextContent(campo.get(0));
                } else if (determinar == 3) {
                    elemento.getElementsByTagName("PartidasGanadas").item(0).setTextContent(campo.get(0));
                } else if (determinar == 4) {
                    elemento.getElementsByTagName("PartidasEmpatadas").item(0).setTextContent(campo.get(0));
                } else {
                    elemento.getElementsByTagName("PartidasPerdidas").item(0).setTextContent(campo.get(0));

                }
            }
        }
        //Guarda la modificación en el XML
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
        DOMSource source = new DOMSource(documento);
        StreamResult result = new StreamResult(dir);
        transformer.transform(source, result);
    }

    private void getDatosJugador(Jugador pJugador) {
        nombre = pJugador.getNombre();
        apellido = pJugador.getApellidos();
        contraseña = pJugador.getContraseña();
        correo = pJugador.getCorreo();
        partGanadas = pJugador.getPartidasGanadas();
        partPerdidas = pJugador.getPartidasPerdidas();
        partEmpatadas = pJugador.getPartidasEmpatadas();
        System.out.println(nombre+apellido+contraseña+correo+partGanadas+partPerdidas+partEmpatadas);
        
    }
}
