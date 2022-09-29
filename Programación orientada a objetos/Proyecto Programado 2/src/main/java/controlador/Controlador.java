/**
 * Clase que contiene las funciones del controlador de la interfaz
 *
 * @autor Dario Vargas
 * @version 1.0
 *
 */
package controlador;

import java.awt.Component;
import java.awt.Image;
import java.awt.event.MouseEvent;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.swing.DefaultComboBoxModel;
import javax.swing.DefaultListModel;
import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JComponent;
import javax.swing.JFileChooser;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.ListModel;
import javax.swing.Timer;
import modelo.Modelo;
import modelo.*;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import vista.Vista;

/**
 *
 * @author dario
 */
public class Controlador extends Vista {

    private Vista view;
    private Modelo model;

    /**
     * Variable global que contiene la musica que se reproudce actualmente.
     */
    protected Clip music;

    /**
     * Variable global que representa el personaje actual al cual se está
     * creando.
     */
    protected Persona personajeActual;

    /**
     * Variable global que representa el panel que se está mostrando
     * actualmente.
     */
    protected String currentPanel;

    /**
     * String que representa el nombre del archivo xml actual.
     */
    protected String xmlActual;

    /**
     * Conjunto de variables String que representan las direcciones relativas de
     * las imagenes por defecto
     */
    private final String imgDefHeroe = "./src/main/java/vista/recursos/sprites/ImgDefHeroe.png";
    private final String imgDefAtqHeroe = "./src/main/java/vista/recursos/sprites/ImgDefAtqHeroe.png";
    private final String imgDefAntiheroe = "./src/main/java/vista/recursos/sprites/ImgDefAntiheroe.png";
    private final String imgDefAtqAntiheroe = "./src/main/java/vista/recursos/sprites/ImgDefAtqAntiheroe.png";
    private final String imgDefVillano = "./src/main/java/vista/recursos/sprites/ImgDefVillano.png";
    private final String imgDefAtqVillano = "./src/main/java/vista/recursos/sprites/ImgDefAtqVillano.png";
    protected String pathCiudad = "./src/main/java/vista/recursos/Escenario/DefaultBackground.png"; //Imagen de la ciudad

    protected ArrayList<Persona> personajes = new ArrayList<>();
    private final String musicPath = "./src/main/java/vista/recursos/soundtrack/";
    private final String xmlPath = "./src/main/java/vista/xml/";
    private String nombreHeroeActual;
    private String nombreVillanoActual;

    /**
     * Constructor de la clase Controlador
     *
     * @param pVista Un objeto de tipo Vista que es la vista que se desea
     * implementar el controlador
     * @param pModel Un objeto de tipo Modelo que representa el modelo en el que
     * se almacenarán los datos
     */
    public Controlador(Vista pVista, Modelo pModel) {
        view = pVista;
        model = pModel;
    }

    /**
     * Función para inicializar los componentes de la interfaz.
     */
    public void iniciar() {
        init();
    }

    /**
     * Método que muestra un panel según su nombre y esconde los demás.
     *
     * @param name El nombre del panel.
     */
    private void showPanel(String name) {
        Component[] components = view.getContentPane().getComponents();
        for (Component component : components) {
            if (component.getName().equals(name)) {
                component.setVisible(true);
            } else {
                component.setVisible(false);
            }
        }

    }

    /**
     * Método que reproduce una canción dentro de la carpeta de Soundtracks
     *
     * @param song Un String con el nombre del archivo que se desea reproducir.
     * @param loop Un Boolean que difine si la canción se reproduce en bucle o
     * no.
     * @return
     */
    private Clip playMusic(String song, boolean loop) {
        Clip clip = null;
        try {
            String path = musicPath + song + ".wav";
            File musicPath = new File(path);
            if (musicPath.exists()) {
                AudioInputStream audioInput = AudioSystem.getAudioInputStream(musicPath);
                clip = AudioSystem.getClip();
                clip.open(audioInput);
                clip.start();
                if (loop) {
                    clip.loop(Clip.LOOP_CONTINUOUSLY);
                }
            } else {
                System.out.println("Not found");
            }
        } catch (IOException | LineUnavailableException | UnsupportedAudioFileException ex) {
            ex.printStackTrace();
        }
        return clip;
    }

    /**
     * Método que inicializa todos los componente que se les implementó
     * funcionalidad, define los eventos y las funciones que se le añadirán
     * según el método a un componente.
     */
    private void init() {
        showPanel("menuPrincipal");
        music = playMusic("menuPrincipal", true);
        view.setVisible(true);
        view.btnJugar.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnJugarMouseClicked(evt);
            }
        });

        view.btnAgregarPersonaje.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarPersonajeMouseClicked(evt);
            }
        });

        view.btnCargarCiudad.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnCargarCiudadMouseClicked(evt);
            }
        });

        view.btnImagenCiudad.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnImagenCiudad(evt);
            }

            private void btnImagenCiudad(MouseEvent evt) {
                int returnVal = view.seleccionarImagen.showOpenDialog(null);
                if (returnVal == JFileChooser.APPROVE_OPTION) {
                    pathCiudad = view.seleccionarImagen.getSelectedFile().getAbsolutePath();
                }
            }
        });

        view.btnGestionCiudad.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnGestionCiudadMouseClick(evt);
            }
        });

        view.btnAgregarImgHeroe.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarImgHeroe(evt);
            }
        });

        view.backBtnAC.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.btnNuevaCiudad.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnNuevaCiudad(evt);
            }

            private void btnNuevaCiudad(MouseEvent evt) {
                showPanel(agregarNuevaCiudad.getName());
            }
        });

        view.btnCrearCiudad.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                crearCiudad(evt);
            }

            private void crearCiudad(MouseEvent evt) {
                XML nuevaCiudad = new XML();
                String nombreCiudad = view.nombreCiudad.getText();
                nuevaCiudad.crearArchivo(nombreCiudad);
                nuevaCiudad = new XML(nombreCiudad + ".xml");
                nuevaCiudad.añadir("Ciudad", "Fondo", pathCiudad);
            }
        });

        view.btnAgregarImgAtaqueH.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarImgAtaqueH(evt);
            }
        });

        view.btnAgregarImgAntiheroe.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarImgAntiheroe(evt);
            }
        });

        view.btnAgregarImgAtaqueAH.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarImgAtaqueAH(evt);
            }
        });

        view.btnAgregarImgVillano.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarImgVillano(evt);
            }
        });

        view.btnAgregarImgAtaqueV.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarImgAtaqueV(evt);
            }
        });

        view.btnAgregarImgAtaqueV.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarImgAtaqueV(evt);
            }
        });

        view.btnFight.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                JLabel btn = (JLabel) evt.getSource();
                if (!btn.isEnabled()) {
                    return;
                }
                btnClickSound(evt);
                btnFightMouseClicked(evt);
            }
        });

        view.exitButton.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                exitButtonMouseClicked(evt);
            }
        });

        view.btnAgregarVillano.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarVillano(evt);
            }
        });

        view.btnAgregarAntiheroe.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarAntiheroeMouseClick(evt);
            }
        });

        view.btnAgregarHeroe.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnAgregarHeroeMouseClicked(evt);
            }
        });

        view.backBtnC.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnGC.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnAP.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnAH.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnAAH.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnAV.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnSC.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnSP.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.backBtnB.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                backButtonMouseClicked(evt);
            }
        });

        view.btnConsultas.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnConsultasMouseClick(evt);
            }
        });

        view.listaCiudades.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnlistaCiudadesMouseClicked();
            }
        });

        view.btnCrearHeroe.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnCrearHeroe(evt);
            }
        });

        view.btnCrearAntiheroe.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnCrearAntiheroe(evt);
            }
        });

        view.btnCrearVillano.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnCrearVillano(evt);
            }
        });

        view.btnSeleccionarPersonaje.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnSeleccionarPersonajeMouseClicked(evt);
            }
        });

        view.btnEmpezarBatalla.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnClickSound(evt);
                btnEmpezarBatallaMouseClicked(evt);
            }
        });

        view.pestañaEfectividad.addComponentListener(new java.awt.event.ComponentAdapter() {
            public void componentShown(java.awt.event.ComponentEvent evt) {
                pestañaEfectividadComponentShown(evt);
            }
        });

    }

    /**
     * Método que reproduce el sonido al clickear
     *
     * @param evt
     */
    private void btnClickSound(java.awt.event.MouseEvent evt) {
        JLabel btn = null;
        JPanel btn1 = null;
        String componentName = "";
        if (evt.getSource() instanceof JLabel) {
            btn = (JLabel) evt.getSource();
            componentName = btn.getName();
        } else {
            btn1 = (JPanel) evt.getSource();
            componentName = btn1.getName();
        }

        playMusic(componentName, false);
    }

    /**
     * Metodo que muestra el panel de agregar personaje.
     *
     * @param evt El evento que se realiza.
     */
    private void btnAgregarPersonajeMouseClicked(java.awt.event.MouseEvent evt) {
        showPanel("agregarPersonaje");
    }

    /**
     * Método para agregar la imágen del Heroe.
     *
     * @param evt El evento que se recibe.
     */
    private void btnAgregarImgHeroe(MouseEvent evt) {
        int returnVal = view.seleccionarImagen.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            String source = view.seleccionarImagen.getSelectedFile().getAbsolutePath();
            view.imgHeroe.setIcon(new ImageIcon(resizeImage(source, 342, 320)));
            personajeActual.setImagen(source);
        }
    }

    /**
     * Método del botón de crear Heroe.
     *
     * @param evt El evento que se recibe.
     */
    private void btnCrearHeroe(MouseEvent evt) {
        String identidadSecreta = view.idSecretaHeroe.getText();
        String nombreDeHeroe = view.nombreHeroe.getText();

        if (verificarCampos(identidadSecreta, nombreDeHeroe)) {
            crearHeroe();
        } else {
            System.out.println("No se rellenaron todos los campos necesarios");
        }
    }

    /**
     * Método para crear un personaje y guardarlo en el xml.
     */
    private void crearHeroe() {
        XML archivo = new XML(view.comboboxSelecHeroeXML.getSelectedItem().toString());
        System.out.println(view.comboboxSelecHeroeXML.getSelectedItem().toString());
        String identidadSecreta = view.idSecretaHeroe.getText();
        String nombreDeHeroe = view.nombreHeroe.getText();
        String archienemigo = (String) view.comboboxArchienemigoH.getSelectedItem();

        Heroe heroe = null;
        if (personajeActual.getImagen() != null && personajeActual.getImagenAtq() != null) {
            heroe = new Heroe(identidadSecreta, nombreDeHeroe, archienemigo, personajeActual.getImagen(), personajeActual.getImagenAtq());
        } else {
            heroe = new Heroe(identidadSecreta, nombreDeHeroe, archienemigo, imgDefHeroe, imgDefAtqHeroe);
        }
        ArrayList<String> nombreNodo = new ArrayList<>(Arrays.asList("IdentidadSecreta", "NombreDeHeroe", "Archienemigo", "Imagen", "ImagenDeAtaque", "EventosGanados", "EventosPerdidos"));
        ArrayList<String> contenidoNodo = new ArrayList<>(Arrays.asList(heroe.getNombre(), heroe.getNombreHeroe(), heroe.getArchienemigo(), heroe.getImagen(), heroe.getImagenAtq(), "0", "0"));
        archivo.añadir("Heroes", "Heroe", nombreNodo, contenidoNodo);
    }

    /**
     * Método del botón de crear antiheroe.
     *
     * @param evt
     */
    private void btnCrearAntiheroe(MouseEvent evt) {
        String identidadSecreta = view.idSecretaAntiheroe.getText();
        String nombreDeHeroe = view.nombreAntiheroe.getText();
        if (verificarCampos(identidadSecreta, nombreDeHeroe)) {
            crearAntiheroe();
        } else {
            System.out.println("No se rellenaron todos los campos necesarios");
        }
    }

    /**
     * Método para crear un antiheroe y guardarlo en el xml.
     */
    private void crearAntiheroe() {
        XML archivo = new XML(view.comboboxSelecAntiheroeXML.getSelectedItem().toString());
        String identidadSecreta = view.idSecretaAntiheroe.getText();
        String nombreDeAntiheroe = view.nombreAntiheroe.getText();
        String archienemigo = (String) view.comboboxArchienemigoAH.getSelectedItem();

        AntiHeroe antiheroe = null;
        if (personajeActual.getImagen() != null && personajeActual.getImagenAtq() != null) {
            antiheroe = new AntiHeroe(identidadSecreta, nombreDeAntiheroe, archienemigo, personajeActual.getImagen(), personajeActual.getImagenAtq());
        } else {
            antiheroe = new AntiHeroe(identidadSecreta, nombreDeAntiheroe, archienemigo, imgDefAntiheroe, imgDefAtqAntiheroe);
        }
        ArrayList<String> nombreNodo = new ArrayList<>(Arrays.asList("IdentidadSecreta", "NombreDeAntiheroe", "Archienemigo", "Imagen", "ImagenDeAtaque", "EventosGanados", "EventosPerdidos"));
        ArrayList<String> contenidoNodo = new ArrayList<>(Arrays.asList(antiheroe.getNombre(), antiheroe.getNombreAntiHeroe(), antiheroe.getArchienemigo(), antiheroe.getImagen(), antiheroe.getImagenAtq(), "0", "0"));
        archivo.añadir("AntiHeroes", "AntiHeroe", nombreNodo, contenidoNodo);
    }

    /**
     * Método del boton crear villano.
     *
     * @param evt
     */
    private void btnCrearVillano(MouseEvent evt) {
        String identidadSecreta = view.idSecretaVillano.getText();
        String nombreDeHeroe = view.nombreVillano.getText();
        if (verificarCampos(identidadSecreta, nombreDeHeroe)) {
            crearVillano();
        } else {
            System.out.println("No se rellenaron todos los campos necesarios");
        }
    }

    /**
     * copia los valores del XML y crea los objetos Persona.
     *
     * @param pArchivo El archivo XML que contiene los personajes
     * @return un ArrayList con los personajes.
     */
    private ArrayList<Persona> cargarPersonajes(String pArchivo) {
        ArrayList<Persona> listaPersonajes = new ArrayList<>();
        XML leer = new XML(pArchivo);
        NodeList heroes = leer.obtenerElementos("Heroe");
        NodeList antiheroes = leer.obtenerElementos("AntiHeroe");
        NodeList villanos = leer.obtenerElementos("Villano");
        listaPersonajes.addAll(crearHeroes(heroes));
        listaPersonajes.addAll(crearVillanos(villanos));
        listaPersonajes.addAll(crearAntiheroes(antiheroes));

        return listaPersonajes;
    }

    /**
     * Crea una lista con objetos de tipo Antiheroe.
     *
     * @param listaVillanos
     * @return Un ArrayList con objetos de tipo persona
     */
    private ArrayList<Persona> crearVillanos(NodeList listaVillanos) {
        ArrayList<Persona> listaPersonajes = new ArrayList<>();
        for (int i = 0; i < listaVillanos.getLength(); i++) {
            NodeList atributos = listaVillanos.item(i).getChildNodes();
            Villano villano = new Villano();
            for (int j = 0; j < atributos.getLength(); j++) {
                Node atributo = atributos.item(j);
                if (!atributo.getNodeName().equals("#text")) {
                    switch (atributo.getNodeName()) {
                        case "IdentidadSecreta":
                            villano.setNombre(atributo.getTextContent());
                            break;
                        case "NombreDeVillano":
                            villano.setNombreVillano(atributo.getTextContent());
                            break;
                        case "TipoVillano":
                            villano.setTipo(atributo.getTextContent());
                            break;
                        default:
                            break;
                    }

                }

            }
            listaPersonajes.add(villano);

        }
        return listaPersonajes;
    }

    /**
     * Crea una lista con objetos de tipo Antiheroe.
     *
     * @param listaAntiheroe
     * @return Un ArrayList con objetos de tipo persona
     */
    private ArrayList<Persona> crearAntiheroes(NodeList listaAntiheroe) {
        ArrayList<Persona> listaPersonajes = new ArrayList<>();
        for (int i = 0; i < listaAntiheroe.getLength(); i++) {
            NodeList atributos = listaAntiheroe.item(i).getChildNodes();
            AntiHeroe antiheroe = new AntiHeroe();
            for (int j = 0; j < atributos.getLength(); j++) {
                Node atributo = atributos.item(j);
                if (!atributo.getNodeName().equals("#text")) {
                    switch (atributo.getNodeName()) {
                        case "IdentidadSecreta":
                            antiheroe.setNombre(atributo.getTextContent());
                            break;
                        case "NombreDeHeroe":
                            antiheroe.setNombreAntiHeroe(atributo.getTextContent());
                            break;
                        case "Archienemigo":
                            antiheroe.setArchienemigo(atributo.getTextContent());
                            break;
                        default:
                            break;
                    }

                }

            }
            listaPersonajes.add(antiheroe);

        }
        return listaPersonajes;
    }

    /**
     * Crea una lista con objetos de tipo Heroe.
     *
     * @param listaHeroes
     * @return Un ArrayList con objetos de tipo persona
     */
    private ArrayList<Persona> crearHeroes(NodeList listaHeroes) {
        ArrayList<Persona> listaPersonajes = new ArrayList<>();
        for (int i = 0; i < listaHeroes.getLength(); i++) {
            NodeList atributos = listaHeroes.item(i).getChildNodes();
            Heroe nuevoHeroe = new Heroe();
            for (int j = 0; j < atributos.getLength(); j++) {
                Node atributo = atributos.item(j);
                if (!atributo.getNodeName().equals("#text")) {
                    switch (atributo.getNodeName()) {
                        case "IdentidadSecreta":
                            nuevoHeroe.setNombre(atributo.getTextContent());
                            break;
                        case "NombreDeHeroe":
                            nuevoHeroe.setNombreHeroe(atributo.getTextContent());
                            break;
                        case "Archienemigo":
                            nuevoHeroe.setArchienemigo(atributo.getTextContent());
                            break;
                        default:
                            break;
                    }

                }

            }
            listaPersonajes.add(nuevoHeroe);

        }
        return listaPersonajes;
    }

    /**
     * Método para crear un Villano y guardarlo en el xml.
     */
    private void crearVillano() {
        XML archivo = new XML(view.comboboxSelecVillanoXML.getSelectedItem().toString());
        String identidadSecreta = view.idSecretaVillano.getText();
        String nombreDeVillano = view.nombreVillano.getText();
        String tipoVillano = (String) view.comboboxTipoVillano.getSelectedItem();

        Villano villano = null;
        if (personajeActual.getImagen() != null && personajeActual.getImagenAtq() != null) {
            villano = new Villano(identidadSecreta, nombreDeVillano, tipoVillano, personajeActual.getImagen(), personajeActual.getImagenAtq());
        } else {
            villano = new Villano(identidadSecreta, nombreDeVillano, tipoVillano, imgDefVillano, imgDefAtqVillano);
        }

        ArrayList<String> nombreNodo = new ArrayList<>(Arrays.asList("IdentidadSecreta", "NombreDeVillano", "TipoVillano", "Imagen", "ImagenDeAtaque", "EventosGanados", "EventosPerdidos"));
        ArrayList<String> contenidoNodo = new ArrayList<>(Arrays.asList(villano.getNombre(), villano.getNombreVillano(), villano.getTipo(), villano.getImagen(), villano.getImagenAtq(), "0", "0"));
        archivo.añadir("Villanos", "Villano", nombreNodo, contenidoNodo);
    }

    /**
     * Método para verificar los campos ingresados al agregar un personaje y que
     * se hayan agregado sus respectivas imágenes.
     *
     * @param campo1 El primer campo que se desea verificar si está vacio.
     * @param campo2 El segundo campo que se desa verificar si está vacío.
     * @return Un boolean que es true en caso de que los campos no estén vacío y
     * que no se haya seleccionado una imágen para el personaje o que se haya
     * seleccionado ambas imágenes. retorna un false en caso contrario.
     */
    private boolean verificarCampos(String campo1, String campo2) {

        if (campo1.equals("") || campo2.equals("")) {
            return false;
        }
        if (!(personajeActual.getImagen() != null && personajeActual.getImagenAtq() != null || personajeActual.getImagen() == null & personajeActual.getImagenAtq() == null)) {
            return false;
        }

        return true;
    }

    /**
     * Método para agregar una imagen de ataque al Heroe
     *
     * @param evt El evento que se recibe del botón.
     */
    private void btnAgregarImgAtaqueH(MouseEvent evt) {
        int returnVal = view.seleccionarImagen.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            String source = view.seleccionarImagen.getSelectedFile().getAbsolutePath();
            view.imgAtqHeroe.setIcon(new ImageIcon(resizeImage(source, 577, 269)));
            personajeActual.setImagenAtq(source);
        }
    }

    /**
     * Método que agrega una imagen de un Antihéroe.
     *
     * @param evt El evento que se recibe del botón.
     */
    private void btnAgregarImgAntiheroe(MouseEvent evt) {
        int returnVal = view.seleccionarImagen.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            String source = view.seleccionarImagen.getSelectedFile().getAbsolutePath();
            view.imgAntiheroe.setIcon(new ImageIcon(resizeImage(source, 342, 320)));
        }
    }

    /**
     * Método que agrega una imagen de ataque de un antiheroe.
     *
     * @param evt El evento que se recibe del botón.
     */
    private void btnAgregarImgAtaqueAH(MouseEvent evt) {
        int returnVal = view.seleccionarImagen.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            String source = view.seleccionarImagen.getSelectedFile().getAbsolutePath();
            view.imgAtqAntiheroe.setIcon(new ImageIcon(resizeImage(source, 577, 269)));
        }
    }

    /**
     * Método para agregar una imagen de un villano.
     *
     * @param evt El evento que se recibe del botón.
     */
    private void btnAgregarImgVillano(MouseEvent evt) {
        int returnVal = view.seleccionarImagen.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            String source = view.seleccionarImagen.getSelectedFile().getAbsolutePath();
            view.imgVillano.setIcon(new ImageIcon(resizeImage(source, 342, 320)));
        }
    }

    /**
     * Método que agrega una imagen de ataque de un villano.
     *
     * @param evt El evento que se recibe de un botón.
     */
    private void btnAgregarImgAtaqueV(MouseEvent evt) {
        int returnVal = view.seleccionarImagen.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            String source = view.seleccionarImagen.getSelectedFile().getAbsolutePath();
            view.imgAtqVillano.setIcon(new ImageIcon(resizeImage(source, 577, 269)));
        }
    }

    /**
     * Botón que reproduce el sonido al luchar.
     *
     * @param evt
     */
    private void btnFightMouseClicked(MouseEvent evt) {
        if (!view.rondas.getText().equals("0")) {
            playMusic("SonidoBatalla", false);
            animacion();
        }
        gane();
    }

    public void gane() {
        int numRondas = Integer.valueOf(view.rondas.getText());
        if (numRondas == 0) {
            int numRondasGanadasHeroe = Integer.valueOf(view.rondasGanadasHeroe.getText());
            int numRondasGanadasVillano = Integer.valueOf(view.rondasGanadasVillano.getText());
            if (numRondasGanadasHeroe > numRondasGanadasVillano) {
                infoBox("Ganó el Héroe/Antiheroe " + nombreHeroeActual, "Ganó el bien");
            } else {
                infoBox("Ganó el Villano " + nombreVillanoActual, "Ganó el mal");
            }
            showPanel("menuPrincipal");
        }
    }

    public void infoBox(String infoMessage, String titleBar) {
        JOptionPane.showMessageDialog(null, infoMessage, "InfoBox: " + titleBar, JOptionPane.INFORMATION_MESSAGE);
    }

    /**
     *
     */
    private void animacion() {
        ArrayList<JComponent> listaComponentes = new ArrayList<>(Arrays.asList(view.imgHeroeAntiheroe, view.imgAtqHeroeAntiheroe, view.imgAtaqueVillano, view.imgBatallaVillano));
        switchLabelVisible(listaComponentes);
        int SEC = 6;
        view.btnFight.setEnabled(false);
        Timer timer = new Timer(SEC * 1000, new AnimationListener(view.btnFight, listaComponentes, view.rondasGanadasHeroe, view.rondasGanadasVillano, view.rondas, view.barraProbabilidad, getPersonaje(nombreHeroeActual), getPersonaje(nombreVillanoActual)));
        timer.start();
        timer.setRepeats(false);

    }

    /**
     *
     * @param listaComponentes
     */
    private void switchLabelVisible(ArrayList<JComponent> listaComponentes) {
        for (int i = 0; i < listaComponentes.size(); i++) {
            JComponent componente = listaComponentes.get(i);
            componente.setVisible(!componente.isVisible());
        }
    }

    /**
     * Botón que obtiene la lista de ficheros de una dirección.
     *
     * @return Un arreglo estático de tipo File.
     */
    private File[] getFileListFromFolder(String pPath) {
        File folder = new File(pPath);
        File[] listOfFiles = folder.listFiles();
        return listOfFiles;

    }

    /**
     *
     * @param pComponente
     * @param listaXML
     */
    private void setComponentModel(javax.swing.JComponent pComponente, File[] listaXML) {
        JList lista = null;
        JComboBox combobox = null;
        DefaultListModel modeloLista = crearModeloLista(listaXML);
        DefaultComboBoxModel modeloCombobox = crearModeloCombobox(listaXML);
        if (pComponente instanceof JList) {
            lista = (JList) pComponente;
            lista.removeAll();
            lista.setModel(modeloLista);
        } else if (pComponente instanceof JComboBox) {
            combobox = (JComboBox) pComponente;
            combobox.removeAllItems();
            combobox.setModel(modeloCombobox);
        }
    }

    /**
     *
     * @param listaXML
     * @return
     */
    private DefaultListModel crearModeloLista(File[] listaXML) {
        DefaultListModel modelo = new DefaultListModel();
        for (int i = 0; i < listaXML.length; i++) {
            modelo.addElement(listaXML[i].getName());
        }
        return modelo;
    }

    /**
     *
     * @param listaXML
     * @return
     */
    private DefaultListModel crearModeloLista(NodeList listaXML) {
        DefaultListModel modelo = new DefaultListModel();
        for (int i = 0; i < listaXML.getLength(); i++) {
            NodeList nodeChilds = listaXML.item(i).getChildNodes();
            for (int j = 0; j < nodeChilds.getLength(); j++) {
                if (nodeChilds.item(j).getNodeName().contains("NombreDe")) {
                    modelo.addElement(nodeChilds.item(j).getTextContent());
                }

            }

        }
        return modelo;
    }

    /**
     *
     * @param listaXML
     * @return
     */
    private DefaultComboBoxModel crearModeloCombobox(File[] listaXML) {
        DefaultComboBoxModel modelo = new DefaultComboBoxModel();
        for (int i = 0; i < listaXML.length; i++) {
            modelo.addElement(listaXML[i].getName());
        }
        return modelo;
    }

    /**
     * Método que muestra el panel de agregar heroes. además establece las
     * imágenes por defecto
     *
     * @param evt
     */
    private void btnAgregarHeroeMouseClicked(java.awt.event.MouseEvent evt) {
        showPanel("agregarHeroe");
        File[] listaArchivos = getFileListFromFolder(xmlPath);
        setComponentModel(view.comboboxSelecHeroeXML, listaArchivos);
        XML xml = new XML((String) view.comboboxSelecHeroeXML.getSelectedItem());
        NodeList listaVillano = xml.obtenerElementos("Villano");
        DefaultComboBoxModel modeloArchienemigo = crearModeloCombobox(listaVillano);
        view.comboboxArchienemigoH.setModel(modeloArchienemigo);
        personajeActual = new Heroe();
        view.imgAtqHeroe.setIcon(new ImageIcon(resizeImage(imgDefAtqHeroe, 577, 269)));
        view.imgHeroe.setIcon(new ImageIcon(resizeImage(imgDefHeroe, 342, 320)));
    }

    /**
     * Método muestra el panel de mostrar antiheroes y establece las imágenes
     * por defecto
     *
     * @param evt
     */
    private void btnAgregarAntiheroeMouseClick(java.awt.event.MouseEvent evt) {
        showPanel("agregarAntiheroe");
        File[] listaArchivos = getFileListFromFolder(xmlPath);
        setComponentModel(view.comboboxSelecAntiheroeXML, listaArchivos);
        XML xml = new XML((String) view.comboboxSelecAntiheroeXML.getSelectedItem());
        NodeList listaVillano = xml.obtenerElementos("Villano");
        DefaultComboBoxModel modeloArchienemigo = crearModeloCombobox(listaVillano);
        view.comboboxArchienemigoAH.setModel(modeloArchienemigo);        
        personajeActual = new AntiHeroe();
        view.imgAtqAntiheroe.setIcon(new ImageIcon(resizeImage(imgDefAtqAntiheroe, 577, 269)));
        view.imgAntiheroe.setIcon(new ImageIcon(resizeImage(imgDefAntiheroe, 342, 320)));
    }

    /**
     * Método que muestra el panel de agregar villanos y establece las imágenes
     * por defecto.
     *
     * @param evt
     */
    private void btnAgregarVillano(java.awt.event.MouseEvent evt) {
        showPanel("agregarVillano");
        File[] listaArchivos = getFileListFromFolder(xmlPath);
        setComponentModel(view.comboboxSelecVillanoXML, listaArchivos);
        personajeActual = new Villano();
        view.imgAtqVillano.setIcon(new ImageIcon(resizeImage(imgDefAtqVillano, 577, 269)));
        view.imgVillano.setIcon(new ImageIcon(resizeImage(imgDefVillano, 342, 320)));
    }

    /**
     * Método que muestra el panel de seleccionar ciudad y cambia la música de
     * fondo, además establece la imágen de la ciudad.
     *
     * @param evt
     */
    private void btnJugarMouseClicked(java.awt.event.MouseEvent evt) {
        showPanel("seleccionarCiudad");
        changeMusic("seleccionarCiudad", true);
        File[] listaArchivos = getFileListFromFolder(xmlPath);
        if (listaArchivos.length > 0) {
            setComponentModel(view.listaCiudades, listaArchivos);
        }
        view.previewImage.setIcon(new ImageIcon(resizeImage(pathCiudad, 1080, 720)));
    }

    /**
     * Método que muestra el panel de gestión de la ciudad.
     *
     * @param evt
     */
    private void btnGestionCiudadMouseClick(MouseEvent evt) {
        showPanel("gestionCiudad");
    }

    /**
     * método que muestra el panel de consultas.
     *
     * @param evt
     */
    private void btnConsultasMouseClick(MouseEvent evt) {
        showPanel("consultas");
    }

    /**
     * Método que muestra el panel de selecionar personaje.
     *
     * @param evt
     */
    private void btnSeleccionarPersonajeMouseClicked(java.awt.event.MouseEvent evt) {
        showPanel("seleccionarPersonaje");
        xmlActual = view.listaCiudades.getSelectedValue();
        cargarPersonajes();
    }

    /**
     *
     */
    public void cargarPersonajes() {
        XML xml = new XML(xmlActual);
        NodeList listaHeroes = xml.obtenerElementos("Heroe");
        NodeList listaAntiheroes = xml.obtenerElementos("AntiHeroe");
        NodeList listaVillano = xml.obtenerElementos("Villano");
        DefaultListModel modeloHeroes = crearModeloLista(listaHeroes);
        DefaultListModel modeloAntiheroes = crearModeloLista(listaAntiheroes);
        DefaultListModel modeloVillanos = crearModeloLista(listaVillano);
        DefaultListModel modeloHeroesAntiheroes = new DefaultListModel();
        addTo(modeloHeroes, modeloHeroesAntiheroes);
        addTo(modeloAntiheroes, modeloHeroesAntiheroes);
        view.listaHeroesAntiheroes.setModel(modeloHeroesAntiheroes);
        view.listaVillanos.setModel(modeloVillanos);
    }

    /**
     *
     * @param <T>
     * @param from
     * @param to
     */
    protected static <T> void addTo(ListModel<T> from, DefaultListModel<T> to) {
        for (int index = 0; index < from.getSize(); index++) {
            to.addElement(from.getElementAt(index));
        }
    }

    /**
     *
     * @param listaXML
     * @return
     */
    private DefaultComboBoxModel crearModeloCombobox(NodeList listaXML) {
        DefaultComboBoxModel modelo = new DefaultComboBoxModel();
        for (int i = 0; i < listaXML.getLength(); i++) {
            NodeList childs = listaXML.item(i).getChildNodes();
            for (int j = 0; j < childs.getLength(); j++) {
                Node atributo= childs.item(j);
                if(!atributo.getNodeName().equals("#text") && atributo.getNodeName().contains("NombreDeVillano")){
                    modelo.addElement(atributo.getTextContent());
                }
            }
            
        }
        return modelo;
    }

    /**
     * Método que muestra el panel de batalla y establece la música de batalla.
     *
     * @param evt
     */
    private void btnEmpezarBatallaMouseClicked(java.awt.event.MouseEvent evt) {
        if (view.listaHeroesAntiheroes.getSelectedValue() == null || view.listaVillanos.getSelectedValue() == null) {
            System.out.println("Debe seleccionar un heroe o antiheroe y un villano");
            return;
        }
        showPanel("batalla");
        changeMusic("Batalla", true);
        XML xml = new XML(xmlActual);
        Node fondo = xml.buscarElemento(null, "Fondo");
        view.escenarioBg.setIcon(new ImageIcon(resizeImage(fondo.getTextContent(), 1920, 1080)));
        nombreHeroeActual = view.listaHeroesAntiheroes.getSelectedValue();
        nombreVillanoActual = view.listaVillanos.getSelectedValue();
        setLabelImg(nombreHeroeActual);
        setLabelImg(nombreVillanoActual);
        personajes = cargarPersonajes(xmlActual);
        setCantidadRondas(getPersonaje(nombreVillanoActual));
    }

    private void setCantidadRondas(Persona pVillano) {
        Villano villano = (Villano) pVillano;
        Heroe heroe = (Heroe) getPersonaje(nombreHeroeActual);
        if (villano.getNombreVillano().equals(heroe.getArchienemigo())) {
            view.rondas.setText("7");
            return;
        }
        switch (villano.getTipo()) {
            case "Social":
                view.rondas.setText("5");
                break;
            case "Económico":
                view.rondas.setText("3");
                break;
            default:
                break;
        }
    }

    /**
     * Verifica si el nombre de un personaje es igual y retorna el objeto
     *
     * @param pNombre
     * @return
     */
    private Persona getPersonaje(String pNombre) {
        Heroe heroe;
        Villano villano;
        AntiHeroe antiheroe;
        for (int i = 0; i < personajes.size(); i++) {
            if (personajes.get(i) instanceof Heroe) {
                heroe = (Heroe) personajes.get(i);
                if (heroe.getNombreHeroe().equals(pNombre)) {
                    return heroe;
                }
            } else if (personajes.get(i) instanceof Villano) {
                villano = (Villano) personajes.get(i);
                System.out.println(villano.getNombreVillano() + " " + pNombre);
                if (villano.getNombreVillano().equals(pNombre)) {
                    return villano;
                }
            } else if (personajes.get(i) instanceof AntiHeroe) {
                antiheroe = (AntiHeroe) personajes.get(i);
                if (antiheroe.getNombreAntiHeroe().equals(pNombre)) {
                    return antiheroe;
                }
            }
        }
        return null;
    }

    /**
     *
     * @param pNombre
     */
    private void setLabelImg(String pNombre) {
        XML xml = new XML(xmlActual);
        Node nodoHeroes = xml.buscarElemento(null, "Heroes");
        Node nodoAntiheroes = xml.buscarElemento(null, "AntiHeroes");
        Node nodoVillanos = xml.buscarElemento(null, "Villanos");
        if (personajeExiste(nodoHeroes.getChildNodes(), pNombre) != null) {
            Node nodo = personajeExiste(nodoHeroes.getChildNodes(), pNombre);
            Node nodoImagen = xml.buscarElemento(nodo, "Imagen");
            Node nodoImagenAtq = xml.buscarElemento(nodo, "ImagenDeAtaque");
            view.imgHeroeAntiheroe.setIcon(new ImageIcon(resizeImage(nodoImagen.getTextContent(), 420, 360)));
            view.imgAtqHeroeAntiheroe.setIcon(new ImageIcon(resizeImage(nodoImagenAtq.getTextContent(), 750, 410)));
        } else if (personajeExiste(nodoAntiheroes.getChildNodes(), pNombre) != null) {
            Node nodo = personajeExiste(nodoAntiheroes.getChildNodes(), pNombre);
            Node nodoImagen = xml.buscarElemento(nodo, "Imagen");
            Node nodoImagenAtq = xml.buscarElemento(nodo, "ImagenDeAtaque");
            view.imgHeroeAntiheroe.setIcon(new ImageIcon(resizeImage(nodoImagen.getTextContent(), 420, 360)));
            view.imgAtqHeroeAntiheroe.setIcon(new ImageIcon(resizeImage(nodoImagenAtq.getTextContent(), 420, 360)));
        } else {
            Node nodo = personajeExiste(nodoVillanos.getChildNodes(), pNombre);
            Node nodoImagen = xml.buscarElemento(nodo, "Imagen");
            Node nodoImagenAtq = xml.buscarElemento(nodo, "ImagenDeAtaque");
            view.imgBatallaVillano.setIcon(new ImageIcon(resizeImage(nodoImagen.getTextContent(), 420, 360)));
            view.imgAtaqueVillano.setIcon(new ImageIcon(resizeImage(nodoImagenAtq.getTextContent(), 750, 410)));
        }

    }

    /**
     *
     * @param pListaNodos
     * @param pNombre
     * @return
     */
    private Node personajeExiste(NodeList pListaNodos, String pNombre) {
        for (int i = 0; i < pListaNodos.getLength(); i++) {
            NodeList nodosHijo = pListaNodos.item(i).getChildNodes();
            if (!pListaNodos.item(i).getNodeName().equals("#text")) {
                for (int j = 0; j < nodosHijo.getLength(); j++) {
                    Node nodo = nodosHijo.item(j);
                    if (nodo.getNodeName().contains("NombreDe")) {
                        if (nodo.getTextContent().equals(pNombre)) {
                            return pListaNodos.item(i);
                        }
                    }
                }
            }
        }

        return null;
    }

    /**
     *
     * @param evt
     */
    private void pestañaEfectividadComponentShown(java.awt.event.ComponentEvent evt) {
        System.out.println("Mostrar efectividad");
    }

    /**
     * Método que cierra el programa.
     *
     * @param evt
     */
    private void exitButtonMouseClicked(java.awt.event.MouseEvent evt) {
        System.exit(0);
    }

    /**
     * Método que regresa a la pantalla anterior.Es necesario ingresarle un
     * nombre a cada uno de los panels y ademas establecer el padre del label.
     *
     * @param evt
     */
    private void backButtonMouseClicked(java.awt.event.MouseEvent evt) {
        JLabel backBtn = (JLabel) evt.getSource();
        JPanel parent = (JPanel) backBtn.getAccessibleContext().getAccessibleParent();
        playMusic(backBtn.getName(), false);
        showPanel(parent.getName());
        changeMusic(parent.getName(), true);
    }

    /**
     * Método que muestra un JFileChooser donde se selecciona un archivo xml
     * para posteriormente copiarlo en una carpeta
     *
     * @param evt
     */
    private void btnCargarCiudadMouseClicked(java.awt.event.MouseEvent evt) {
        int returnVal = view.seleccionarArchivoXML.showOpenDialog(null);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            Path source = view.seleccionarArchivoXML.getSelectedFile().toPath();
            String sourceName = view.seleccionarArchivoXML.getSelectedFile().getName();
            Path dest = new File(xmlPath + sourceName).toPath();
            try {
                Files.copy(source, dest, StandardCopyOption.REPLACE_EXISTING);
            } catch (IOException ex) {
                Logger.getLogger(Controlador.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }

    /**
     * Método que cambia la musica que se reproduce actualmente.
     *
     * @param pMusic El nombre del archivo que se desea reproducir.
     * @param pLoop Valor booleano que establece una reproducción en bucle en
     * caso de que se seleccione true, de lo contrario, se reproduce una vez.
     */
    private void changeMusic(String pMusic, boolean pLoop) {
        String path = musicPath + pMusic + ".wav";
        File musicFile = new File(path);
        if (musicFile.exists()) {
            music.stop();
            music = playMusic(pMusic, pLoop);
        }
    }

    /**
     * Método que redimenciona una imagen,
     *
     * @param path La dirección de la imagen.
     * @param width El ancho de la imagen que se desea.
     * @param height El largo de la imagen que sea desea.
     * @return image que es un objeto de tipo Image.
     */
    private Image resizeImage(String path, int width, int height) {
        Image image = null;
        try {
            image = ImageIO.read(new File(path));//Puede cambiarse por la dirección absoluta
            image = image.getScaledInstance(width, height, Image.SCALE_SMOOTH);
        } catch (IOException e) {
            System.out.println("Something went wrong.");
        }
        return image;
    }

    /**
     *
     */
    public void btnlistaCiudadesMouseClicked() {
        String nombreArchivo = view.listaCiudades.getSelectedValue();
        XML readXML = new XML(nombreArchivo);
        Node nodo = readXML.buscarElemento(null, "Fondo");
        String imagePath = nodo.getTextContent();
        view.previewImage.setIcon(new ImageIcon(resizeImage(imagePath, 640, 420)));
    }
}
