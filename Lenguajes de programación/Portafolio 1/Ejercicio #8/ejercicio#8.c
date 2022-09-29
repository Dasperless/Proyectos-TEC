#include <stdio.h>
#include "animal.h"

int main(int argc, char const *argv[])
{
	tipoAnimal tipo_animal1 = {"Felidae","Carnivora"};
	tipoAnimal tipo_animal2 = {"Canidae","Carnivora"};

	animal arr[2] = {{&tipo_animal1,"gato"},{&tipo_animal2,"perro"}};
	printAnimal(arr,2);

}
