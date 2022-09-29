package modelo;

import java.io.File;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Text;

/**
 *
 * @author Keylor Martinez
 */
public class XML{

    private static Document documento;
    private File archivoActual = null;
    private final String xmlPath = "./src/main/java/vista/xml/";

    /**
     * Constructor de la clase XML .El objetivo de este constructor es manipular
     * datos de un XML especifico.
     *
     * @param pNombre
     */
    public XML(String pNombre) {
        archivoActual = new File(xmlPath + pNombre);
        try {
            //Carga el documento XML que ya existe.
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            documento = db.parse(archivoActual);
            documento.getDocumentElement().normalize();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     *
     */
    public XML() {
    }

    /**
     *
     * @param pNombre
     */
    public void crearArchivo(String pNombre) {
        try {
            DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
            Document documento = docBuilder.newDocument();

            // Elemento raíz
            Element rootElement = documento.createElement("XML");
            documento.appendChild(rootElement);

            // Elemento Ciudad
            Element Ciudad = documento.createElement("Ciudad");
            rootElement.appendChild(Ciudad);

            // Elemento Heroe
            Element Heroe = documento.createElement("Heroes");
            rootElement.appendChild(Heroe);

            // Elemento Anti-heroe
            Element Antiheroe = documento.createElement("AntiHeroes");
            rootElement.appendChild(Antiheroe);

            // Elemento Villano
            Element Villano = documento.createElement("Villanos");
            rootElement.appendChild(Villano);

            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(documento);
            File file = new File(xmlPath + pNombre + ".xml");
            StreamResult result = new StreamResult(file);
            transformer.transform(source, result);
        } catch (ParserConfigurationException | TransformerConfigurationException ex) {
            Logger.getLogger(XML.class.getName()).log(Level.SEVERE, null, ex);
        } catch (TransformerException ex) {
            Logger.getLogger(XML.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    /**
     * *
     *
     * @param pRoot El nombre del padre al añadirle contenido
     * @param pHijo Un String que indica el nombre del nodo hijo que contendra
     * otros más.
     * @param pNombreContenido Un arreglo con el nombre de las etiquetas hijo
     * del nodo hijo
     * @param pContenido El contenido de las etiquetas creadas.
     * @return true en el caso de que se haya añadido exitosamente, false en el
     * caso contrario
     */
    public boolean añadir(String pRoot, String pHijo, ArrayList<String> pNombreContenido, ArrayList<String> pContenido) {
        try {
            NodeList lista = documento.getElementsByTagName(pRoot); //obtengo la lista de nodos buscado
            Node padre = lista.item(0);//el padre al añadirle un elemento
            Element hijo = documento.createElement(pHijo);//el hijo que se le añadirá al padre.
            for (int i = 0; i < pNombreContenido.size(); i++) {
                if (i < 3 && existElement(pNombreContenido.get(i), pContenido.get(i))) {
                    return false;
                }
                Element nodo = documento.createElement(pNombreContenido.get(i)); //se crea una etiqueta con un nombre
                Text contenido = documento.createTextNode(pContenido.get(i)); //se le añade el contenido a esta etiqueta creada anteriormente.
                nodo.appendChild(contenido);//se le agrega el contenido al nodo creado
                hijo.appendChild(nodo);//se le agrega al padre.
            }
            padre.appendChild(hijo);
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(documento);
            StreamResult result = new StreamResult(archivoActual);
            transformer.transform(source, result);
        } catch (TransformerConfigurationException ex) {
            Logger.getLogger(XML.class.getName()).log(Level.SEVERE, null, ex);
        } catch (TransformerException ex) {
            Logger.getLogger(XML.class.getName()).log(Level.SEVERE, null, ex);
        }
        return true;
    }

    public boolean añadir(String pRoot, String pHijo, String pContenido) {
        try {
            NodeList lista = documento.getElementsByTagName(pRoot); //obtengo la lista de nodos buscado
            Node padre = lista.item(0);//el padre al añadirle un elemento
            Element hijo = documento.createElement(pHijo);//el hijo que se le añadirá al padre.
            
            Text contenido = documento.createTextNode(pContenido); //se le añade el contenido a esta etiqueta creada anteriormente.
            hijo.appendChild(contenido);//se le agrega al padre.

            padre.appendChild(hijo);
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(documento);
            StreamResult result = new StreamResult(archivoActual);
            transformer.transform(source, result);
        } catch (TransformerConfigurationException ex) {
            Logger.getLogger(XML.class.getName()).log(Level.SEVERE, null, ex);
        } catch (TransformerException ex) {
            Logger.getLogger(XML.class.getName()).log(Level.SEVERE, null, ex);
        }
        return true;
    }
    

    public boolean existElement(String pNombreEtiqueta, String pContenido) {
        NodeList listaElementos = obtenerElementos(pNombreEtiqueta);
        for (int i = 0; i < listaElementos.getLength(); i++) {
            NodeList nodosHijos = listaElementos.item(i).getChildNodes();
            if (nodosHijos.item(i) != null) {
                if (nodosHijos.item(i).getTextContent().equals(pContenido)) {
                    return true;
                }
            }

        }
        return false;
    }

    public NodeList obtenerElementos(String pNombre) {
        return documento.getElementsByTagName(pNombre);
    }

    public Node buscarElemento(Node node, String name) {
        if (node == null) {
            node = documento.getFirstChild();
        }
        if (node.getNodeName().equals(name)) {
            return node;
        }
        if (node.hasChildNodes()) {
            NodeList list = node.getChildNodes();
            int size = list.getLength();
            for (int i = 0; i < size; i++) {
                Node found = buscarElemento(list.item(i), name);
                if (found != null) {
                    return found;
                }
            }
        }
        return null;
    }
}
