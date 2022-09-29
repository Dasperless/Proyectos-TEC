
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
struct mascota
{
	char* especie;
	char* nombre;
	struct mascota *sig;
};


void mostrarTodo(struct mascota *lista){
    for ( int i = 0; lista->sig != NULL; lista= lista->sig, i++)
    {
        printf( "[    Mascota #%d    ]\n", i );
        printf( "Especie: %s\n", lista->especie );
        printf( "Nombre: %s\n", lista->nombre);
        printf( "Siguiente: %p\n", lista->sig);

    }
	printf( "\n\n");

}


void agregarMascota(char* especie, char* nombre, struct mascota** head){
	struct mascota* nuevaMascota = (struct mascota*) malloc(sizeof(struct mascota));
	nuevaMascota->especie = strdup(especie);
	nuevaMascota->nombre = strdup(nombre);
	nuevaMascota->sig =(*head);
	(*head) = nuevaMascota;
	printf("\n#############################################\n");
	printf("[Aviso]: Se agrego la siguiente mascota\n\n");
	printf("Especie: %s\n",especie);
	printf("Nombre: %s\n",nombre);
	printf("Siguiente: %p\n",nuevaMascota->sig);
	printf("#############################################\n\n");

}

int inputNumero(){
	printf(">> ");
	int numero;
	scanf("%d",&numero);
	return (numero);
}
int main(){
	int opcion;
	bool salir = false;
	struct mascota *lista = (struct mascota*) malloc(sizeof(struct mascota));
	lista->sig = NULL;
	do
	{
		printf("######### Menu #########\n\n");
		printf("1. Agregar mascota\n");
		printf("2. Mostrar todo\n");
		printf("3. Salir\n\n");
		opcion = inputNumero();
		switch (opcion)
		{
		case 1:
			printf("Ingrese las especie\n");
			char especie[100];
			printf(">> ");
			scanf(" %99[^\n]%*[^\n]",especie);

			printf("Ingrese el nombre\n");
			char nombre[100];
			printf(">> ");
			scanf(" %99[^\n]%*[^\n]",nombre);

			agregarMascota(especie,nombre,&lista);
			break;
		case 2:
			mostrarTodo(lista);
			break;
		case 3:
			salir = true;
			break;
		default:
			printf("No existe la opcion elegida./n");
			break;
		}
	} while (!salir);
	return 0;
}