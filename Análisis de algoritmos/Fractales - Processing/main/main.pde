import java.lang.Math.*; //<>//
import java.util.*;

int ARRAY_SIZE = 10;              //Tamaño del arreglo.
float MAX_BRANCH  = 1000;         //Tamaño máximo del arbol.
float k = ARRAY_SIZE/MAX_BRANCH;  //Cantidad de números que deben estar ordenados para pintar una rama.
int treeGrowS = 0;                //Crecimiento del árbol ShellSort.
int treeGrowR = 0;                //Crecimiento del árbol RadixSort.
int countRadix = 0;               //Cantidad de elementos ordenados en el RadixSort.
int countShell = 0;               //Cantidad de elementos ordenados en el ShellSort.

//Instancias de los árboles.
FractalTree arbolRadix = new FractalTree();
FractalTree arbolShell = new FractalTree();

//Arreglos a ordenar
int arr[] = new int[ARRAY_SIZE];
int arr2[] = new int[ARRAY_SIZE];

//Variables de los algoritmos de ordenamientos
int gap = ARRAY_SIZE/2;            //Valor del gap del ShellSort
int m = getMax(arr2, ARRAY_SIZE);  //El mayor número del RadixSort.
int exp = 1;                       //Exponente del RadixSort.

void setup() {
  size(1000, 700);

  //Se generan numeros random para ingresar en los arreglos.
  int random;
  for (int i = 0; i < ARRAY_SIZE; i++) {
    random = (int)(Math.random() * ARRAY_SIZE + 1);
    arr[i] = random;
  }

  arr2 = arr; //Dos arreglos con los mismo números.
}

void draw() {
  background(0);
  frameRate(2);
  stroke(255);

  if (treeGrowS == MAX_BRANCH && treeGrowR == MAX_BRANCH) {
    System.out.println("Finish");
    noLoop();
  }

  // Ángulo con respecto a la cantida de elementos ordenados.
  float a = (treeGrowR / (float) width) * 90f;
  float b = (treeGrowS / (float) width) * 90f;

  // Lo convierte a radianes.
  float o = radians(a);
  float p = radians(b);

  if (treeGrowR < MAX_BRANCH )
    radixsort(arr, ARRAY_SIZE);   // RadixSort

  pushMatrix();                   // Guarda el estado actual de la matriz.
  translate(width/4, height);
  line(0, 0, 0, -120);            // Dibuja una línea de 120 pixeles.
  translate(0, -120);             // Se mueve al final de la línea.
  arbolRadix.branch(a, o);        // Dibuja el árbol fractal con respecto los números ordenados por RadixSort.
  popMatrix();                    // Recupera el estado de la matriz.

  if (treeGrowS < MAX_BRANCH)
    shellsort(arr2, ARRAY_SIZE);

  pushMatrix();                   // Guarda el estado actual de la matriz.
  translate((width/4)*3, height);
  line(0, 0, 0, -120);            // Dibuja una línea de 120 pixeles.
  translate(0, -120);             // Se mueve al final de la línea.
  arbolShell.branch(b, p);        // Dibuja el árbol fractal con respecto los números ordenados por ShellSort.
  popMatrix();                    // Recupera el estado de la matriz.
}

// Cuenta la cantidad de elementos que estan ordenados
int countSorted(int pArray[]) {
  int count = 0;
  for (int i = 0; i < pArray.length; i++) {
    if (isLeftSorted(pArray, i, pArray[i]) && isRightSorted(pArray, i, pArray[i] ))
      count++;
  }
  return count;
}

// Verifica si el lado derecho está ordenado.
boolean isRightSorted(int pArray[], int pIndex, int pNumber) {
  for (; pIndex < pArray.length; pIndex++) {
    if (pArray[pIndex] < pNumber)
      return false;
  }

  return true;
}

// Verifica si el lado izquierdo está ordenado.
boolean isLeftSorted(int pArray[], int pIndex, int pNumber) {
  for (; pIndex > 0; pIndex--) {
    if (pArray[pIndex] > pNumber)
      return false;
  }
  return true;
}

void print(int pArray[]) {
  for (int i = 0; i < pArray.length; i++)
    System.out.print(pArray[i]+ " ");
  System.out.print("\n\n\n\n");
}
