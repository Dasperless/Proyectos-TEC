#Importante
Para ejecutar los ejercicios se debe utilizar la terminación `R` para recursivo y la terminación `I` para Iterativo.
Ejemplo:

```python
>>> procesa_listaI([84,42,33,42,84,11,11])`
[[84,42,33,11], [11,33,42,84]]
````

la solución de forma iterativa y recursiva.
1. Escriba una función en Python llamada procesa_lista(lista) que reciba como entrada una lista de números enteros positivos y retorna una lista con dos elementos sublista. Cada sublista debe contener lo siguiente (Utilice solamente recursividad):
 La primer sublista es la lista en el mismo orden sin números repetidos.
 La segunda sublista es la primer sublista modificada, donde los números aparecen ordenados ascendentemente.
Ejemplos del comportamiento de la función:
```python
>>> procesa_lista([84,42,33,42,84,11,11])`
[[84,42,33,11], [11,33,42,84]]
>>> procesa_lista([3,4,3,6,77,1,2,80,93,3,4,6,4])
[[3,4,6,77,1,2,80,93], [1,2,3,4,6,77,80,93]]
``` 
2. Escribir una función llamada matriz_identidad(matriz) que recibe una matriz cuadrada y retorne True si la matriz ingresada representa la matriz identidad y False en caso contrario. La matriz identidad es aquella donde los elementos de la diagonal está compuesta por unos (1) y el resto en ceros (0). Utilice iteración con FOR. Ejemplos del comportamiento de la función:
```python
>>> matriz_identidad([ [ 1, 0, 0 ], [ 0, 1 ,0 ], [ 0, 0, 1 ] ])
True
````
3. Escribir una función llamada sum_mat(matriz1, matriz2) que recibe dos matrices y retorne la multiplicación de ambas matrices. Asuma que ambas matrices son válidas. Ejemplos del comportamiento de la función:
```python	
>>> sum_mat ([[4, 1], [2, 5]], [[1, 2], [3, 7]])
[[5, 3], [5, 8]]
```
4. Escribir una función llamada mult_mat(matriz1, matriz2) que recibe dos matrices y retorne la multiplicación de ambas matrices. Asuma que ambas matrices son válidas. Ejemplos del comportamiento de la función:`
```python	
>>> mult_mat ([[4, 1], [2, 5]], [[1, 2], [3, 7]])
[[7, 15], [17, 39]]
```

