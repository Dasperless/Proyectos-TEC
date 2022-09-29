package modelo;

import java.util.ArrayList;

/**
 *
 * @author Dario Vargas
 */
public class CuatroEnLinea {

    private int cantidadJugadores;
    private Jugador jugador1;
    private Jugador jugador2;
    private String colorJugador1;
    private String colorJugador2;
    private int filas;
    private int columnas;
    private int turno = 1; //El númeor de persona equivale al turno
    private String[][] tablero;
    private ArrayList<String[][]> movimientos = new ArrayList<>();

//    private String colorJugar3;
    //TODO 
    //El sistema de turno puede ser por la posición del array
    //Decidir si poner un numero o la posicion del array
    //Verificar Gane
    /**
     * Constructor del juego 4 en linea
     * @param pFilas                La cantidad de filas del tablero
     * @param pColumnas             La cantidad de columnas del tablero
     * @param pCantidadJugadores    La cantidad de jugadores del tablero
     * @param pColorJugador1        El color del jugador 1
     * @param pColorJugador2        El color del jugador 2
     */
    public CuatroEnLinea(int pFilas, int pColumnas, int pCantidadJugadores, String pColorJugador1, String pColorJugador2/*, String pColorJugador3, Jugador pJugador1, Jugador pJugador2,Jugador pJugador3*/) {
        this.filas = pFilas;
        this.columnas = pColumnas;
        this.cantidadJugadores = pCantidadJugadores;
        this.colorJugador1 = pColorJugador1;
        this.colorJugador2 = pColorJugador2;
//        this.colorJugador3 = pColorJugador3;
//        this.jugador1 = pJugador1;
//        this.jugador2 = pJugador3;
        tablero = new String[filas][columnas];
    }

    /**
     * Inserta una ficha en una columna seleccionada
     * @param columna Un entero con la columna en la que se desea colocar la ficha 
     * @return Retorna true en el caso de que se haya insertado la ficha, retorna false en el caso contrario.
     */
    public boolean insertarFicha(int columna) {
        String[][] movimiento = {{colorJugadorActual(),String.valueOf(columna)}};
        movimientos.add(movimiento);
        int i = 0;                              //indice donde se encuentra el final del tablero o una ficha
        for (i = 0; i < filas; i++) {           //Mientras el i sea menor a la cantidad de filas
            if (tablero[i][columna] != null) {  //Si en la posición i del tablero en la columna elegida hay una ficha
                break;                          //Se rompe el ciclo 
            }
        }
        if (i == 1) {                                   //Si Se llego al tope del tablero
            return false;                               //No se insertó ninguna ficha
        } else {                                        //Si el aún no se llegó al tope 
            tablero[i - 1][columna] = cambiarTurno();   //Se inserta el color de la ficha en el tablero una posición antes de encontrar una ficha
            return true;
        }
    }
    
    public void imprimirTablero() {
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                System.out.print(tablero[i][j] + "\t");
            }
            System.out.print("\n");
        }
    }
    private String colorJugadorActual(){
        switch(turno){
            case 1:
                return colorJugador1;
            case 2:
                return  colorJugador2;
            default:
                System.out.println("No existe el jugador");
                break;
        }   
        return null;
    }
    /**
     * Cambia el turno y retorna el color de la ficha.
     * @return retorna un String con el color del jugador actual
     */
    private String cambiarTurno() {
        if(turno  > cantidadJugadores){
            turno = 1; //La coloco en cero porque en insertar fila siempre incrementa en 1
        }
        System.out.println(turno);
        switch(turno){
            case 1:
                turno++;
                return colorJugador1;
            case 2:
                turno ++;
                return  colorJugador2;
            default:
                System.out.println("No existe el jugador");
                break;
        }
        return null;
    }
    
    /**
     * Verifica si existe un ganador.
     * @param pTablero
     * @return Se Retorna true en el caos de que exista un ganador.
     */
    public boolean existeGanador(String[][] pTablero){
//        imprimirTablero();
        if(lineal(pTablero)){
            return true;
        }if(diagonal(pTablero)){
            return true;
        }
        return false;
    }
    
    /**
     * Metodo que verifica tanto la diagonal invertida como la diagonal inversa y establece si hay 4 en linea.
     * @param pTablero El tablero a verificar.
     * @return Retorna true en el caso que exista gane en las diagonales. Retorna false en el caso contrario.
     */
    public boolean diagonal(String[][] pTablero){
        for(int i = 0; i < filas;i++){
            for(int j = 0; j<columnas; j++ ){
               if(pTablero[i][j] != null && verificarDiagonal(pTablero,i,j)){
                    return true;
                } else if(pTablero[i][j] != null && verificarDiagonalInversa(pTablero,i,j)){
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Método que verifica si existe gane en la diagonal invertida.
     * @param pTablero Un String[][] que es el tablero de cuatro en linea.
     * @param i Un int con la fila actual del tablero a verificar.
     * @param j Un int con la columna actual a verificar.
     * @return Retorna true en el caso que exista gane en la diagonal invertida, false en el caso contrario.
     */
    private boolean verificarDiagonalInversa(String[][] pTablero, int i, int j) {
        return verificarDiagonalInversaAuxInversa(pTablero,i,j,pTablero[i][j],1);
    }    
    
    /**
     * Función que verifica la diagonal invertida de un String[][]-
     * @param pTablero Un String[][] que representa el tablero a verificar.
     * @param i Un int con la fila actual a verificar del tablero.
     * @param j Un int con la columna actual a verificar del tablero.
     * @param pColorRepite Un String con el color que se repite en el tablero.
     * @param pRepite Un int con la cantidad de veces que se repite pColorRepite.
     * @return 
     */
    private boolean verificarDiagonalInversaAuxInversa(String[][] pTablero, int i, int j,String pColorRepite,int pRepite) {
      
      if(i <0 || i >=filas  || j < 0 || pColorRepite != pTablero[i][j] && pRepite <= 4){ //Si  "i" o "j" son mayores que las filas y columnas o el color del tablero no es igual al que se repite y se ha repetido menos de 4 veces
          return false;
      } else if(pRepite == 4){
          return true;
      }else if(pColorRepite == pTablero[i][j]){
          return verificarDiagonalInversaAuxInversa(pTablero,i+1,j-1,pColorRepite,pRepite+1);
      }
      return false;
    } 
    
    public boolean existeEmpate(String[][] pTablero){
        for(int i = 0; i<filas;i++){
            for(int j = 0; j<columnas;j++){
                if(pTablero[i][j] == null){
                    return false;
                }
            }
        }
        return true;
    }
    
    /**
     * Función principal que verifica la digonal del tablero y establece si existe un gane.
     * @param pTablero Un String[][] con el tablero.
     * @param i Un int con la fila del tablero actual.
     * @param j Un int con la columna del tablero actual.
     * @return Retorna un true en el caso de que exista gane, retorna false en caso contrario.
     */
    private boolean verificarDiagonal(String[][] pTablero, int i, int j) {
        return verificarDiagonalAux(pTablero,i,j,pTablero[i][j],1);
    }    
    
    /**
     * Funcion auxiliar para verificar si hay gane en un String[][] en un tablero.
     * @param pTablero  Un String[][] que representa el tablero.
     * @param i Un int que representa el indice de las filas del tablero.
     * @param j Un int que representa las columnas del tablero.
     * @param pColorRepite Un String con el nombre del color que se repite.
     * @param pRepite Un int con la cantidad de veces que se repite pColorRepite.
     * @return Retorna un true en el caso que se repita 4 veces y false en el caso contrario.
     */
    private boolean verificarDiagonalAux(String[][] pTablero, int i, int j,String pColorRepite,int pRepite) {
//        System.out.println(filas +  " " + columnas);
      if(i >= filas || j >=columnas || pColorRepite != pTablero[i][j] && pRepite <= 4){ //Si  "i" o "j" son mayores que las filas y columnas o el color del tablero no es igual al que se repite y se ha repetido menos de 4 veces
          return false;
      } else if(pRepite == 4){
          return true;
      }else if(pColorRepite == pTablero[i][j]){
          return verificarDiagonalAux(pTablero,i+1,j+1,pColorRepite,pRepite+1);
      }
      return false;
    }        
    
    /**
     * Recibe una String[][] y verifica si hay un gane de manera lineal.
     * @param pTablero
     * @return Retorna un String[][] que representa el tablero donde se está jugando.
     */
    private boolean lineal(String[][] pTablero){
        if(vertical(pTablero) || horizontal(pTablero)){
            return true;
        }
        return false;
    }
    
    private boolean vertical(String[][] pTablero){
        int repite = 1; //Cantidad de veces que se repite una ficha
        String color = null; //El color que se repite;
        for (int i = 0; i < columnas; i++) {
            for (int j = 0; j < filas; j++) {
                if(repite == 4){
                    return true;
                }else if(repite < 4 && color!=pTablero[j][i]){
                       color = pTablero[j][i];
                       repite = 1;
                }else if((color == pTablero[j][i]) && (color != null) ){ //Si el color que se repite es igual al del tablero y el color es diferente de nulo
                    repite++;
                }
            }
        }        
        return false;
    }
    
    private boolean horizontal(String[][] pTablero){
        int repite = 1; //Cantidad de veces que se repite una ficha
        String color = null; //El color que se repite;
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if(repite == 4){
                    return true;
                }else if(repite < 4 && color!=pTablero[i][j]){
                       color = pTablero[i][j];
                       repite = 1;
                }else if((color == pTablero[i][j]) && (color != null) ){ //Si el color que se repite es igual al del tablero y el color es diferente de nulo
                    repite++;
                }
            }
        }
        return false;        
    }
    
    public String[][] getTablero(){
        return tablero;
    }
    
    public void setJugador1(Jugador pJugador1){
        this.jugador1 = pJugador1;
    }
    
    public void setJugador2(Jugador pJugador2){
        this.jugador2 = pJugador2;
    }   
    
    public Jugador getJugador1(){
        return jugador1;
    }
    
    public Jugador getJugador2(){
        return jugador2;
    }       
}

