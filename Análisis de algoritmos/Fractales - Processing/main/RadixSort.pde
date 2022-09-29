void radixsort(int pArray[], int pArraySize) { //<>//
  if (m / exp >= 0) {
    countSort(pArray, pArraySize, exp);
    float sortedNumbers = countSorted(pArray);             // Cantidad total de números contados.
    float sortedNumsNotCounted = 0;                        // Cantidad total de números NO contados. //<>//
    if (sortedNumbers - countRadix > 0)                    
      sortedNumsNotCounted = sortedNumbers - countRadix;   
    for (int n = 0; n <  sortedNumsNotCounted/k; n++)      // Cantidad de veces que debe crecer el árbol Radix.
      treeGrowR++;                                         // Aumenta el crecimiento del árbol. 
    countRadix += sortedNumsNotCounted;                    // Aumenta la cantidad de números ordenados. 
    exp *= 10;                                                      
  }
}

//Obtiene el numero mayor de un arreglo
int getMax(int pArray[], int pArraySize) {
  int mx = pArray[0];
  for (int i = 1; i < pArraySize; i++)
    if (pArray[i] > mx)
      mx = pArray[i];
  return mx;
}


void countSort(int pArray[], int pArraySize, int exp) {
  int output[] = new int[pArraySize]; // Array de salida
  int i;
  int count[] = new int[10];
  Arrays.fill(count, 0);

  for (i = 0; i < pArraySize; i++)
    count[(pArray[i] / exp) % 10]++;


  for (i = 1; i < 10; i++)
    count[i] += count[i - 1];

  for (i = pArraySize - 1; i >= 0; i--) {
    output[count[(pArray[i] / exp) % 10] - 1] = pArray[i];
    count[(pArray[i] / exp) % 10]--;
  }

  for (i = 0; i < pArraySize; i++)
    pArray[i] = output[i];
}
