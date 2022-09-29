void shellsort(int pArray[], int pArraySize) { //<>//
  if ( gap > 0) { 
    for (int i = gap; i < pArraySize; i++) { 
      int temp = pArray[i]; 
      int j; 
      for (j = i; j >= gap && pArray[j - gap] > temp; j -= gap) { 
        pArray[j] = pArray[j - gap];
      }
      pArray[j] = temp;
    }
    if (gap == 1) {
      float sortedNumbers = countSorted(pArray);                // Cantidad total de números contados
      float sortedNumsNotCounted = sortedNumbers - countShell;  // Cantidad de números no contados
      for (int n = 0; n <  sortedNumsNotCounted/k; n++)         // Cantidad de veces que debe crecer el árbol Shell.
        treeGrowS++;                                            // Aumenta el crecimiento del árbol Shell.
      countShell+= sortedNumsNotCounted;                        // Aúmenta la de números ordenados por ShellSort.
    }    
    gap /= 2;
  }
}
