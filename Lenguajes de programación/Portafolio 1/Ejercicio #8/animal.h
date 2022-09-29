typedef struct
{
 char family[100];
 char order[100];
}tipoAnimal;

typedef struct 
{
	tipoAnimal *type;
	char nombre[100];
}animal;

void printAnimal(animal animalList[],int arrSize){
	for (int i =0; i<arrSize;i++){
		printf("familia: %s\n",animalList[i].type->family);
		printf("orden: %s\n",animalList[i].type->order);
		printf("nombre: %s\n\n",animalList[i].nombre);
	}
	
	
}

