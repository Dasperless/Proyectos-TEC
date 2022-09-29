#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "structs/vaxAllowed.h"
#include "structs/VaxApplied.h"

char inputMenu();
void inputString(char* input);
int inputInt();
void addVaxAllowedMenu(vaxAllowed **head);
void addVaxAppliedMenu(vaxApplied **head);
void covPercentMenu(vaxApplied *head);
void covPercent(char* country,int population, int vaxApplied);


int main(){
	char opcion;
	bool salir = false;
	vaxAllowed *listVaxAllow = NULL;
	vaxApplied *listVaxApplied = NULL;
	do
	{
		printf("######### Menu #########\n\n");
		printf("A: Incluir vacunas admitidas por pais\n");
		printf("B: Incluir cantidad de vacunas aplicadas por poblacion pais\n");
		printf("C: Porcentaje de cobertura por pais\n\n");
		printf("[S]alir\n\n");
		opcion = inputMenu();
		switch (opcion)
		{
		case 'A':
			addVaxAllowedMenu(&listVaxAllow);
			break;
		case 'B':
			addVaxAppliedMenu(&listVaxApplied);
			break;
		case 'C':
			covPercentMenu(listVaxApplied);
			break;
		case 'S':
			salir = true;
			break;
		default:
			printf("No existe la opcion elegida.\n");
			break;
		}
	} while (!salir);	
}
char inputMenu(){
	printf(">> ");
	char opcionMenu;
	scanf(" %c",&opcionMenu);
	opcionMenu = toupper(opcionMenu);
	return (opcionMenu);
}

void inputString(char* input){
	printf(">> ");
	scanf(" %99[^\n]%*[^\n]",input);
}

int inputInt(){
	printf(">> ");
	int input;
	scanf("%d",&input);
	return input;
}

void addVaxAllowedMenu(vaxAllowed **head){
	char name[100];
	char country[100];
	char organization[100];
	printf("INGRESE EL NOMBRE DE LA VACUNA\n");
	inputString(name);
	printf("INGRESE EL PAIS\n");
	inputString(country);
	printf("INGRESE LA ORGANIZACION\n");
	inputString(organization);
	addVaxAllowed(name,country,organization,head);
}

void addVaxAppliedMenu(vaxApplied **head){
	char country[100];
	int population,vaccinated;
	printf("INGRESE EL PAIS\n");
	inputString(country);
	printf("INGRESE LA POBLACION\n");
	population = inputInt();
	printf("INGRESE LA CANTIDAD DE DOSIS APLICADAS\n");
	vaccinated = inputInt();
	addVaxApplied(country,population,vaccinated,head);
}

void printCountry(vaxApplied *head){
printf("+---------Lista de paises---------+\n");
for (int i = 0; head !=NULL;head =head->next)
{
	printf("[%d]: %s\n",i,head->country);
}
printf("\n");
}

void covPercentMenu(vaxApplied *head){
	printCountry(head);
	printf("Seleccione el indice del pais\n");
	int option = inputInt();
	int i = 0;
	for (; i < option || head->next!=NULL;head=head->next, i++);
	if (head!=NULL)
	{
		covPercent(head->country,head->population,head->vaccinated);
	}
}

void covPercent(char* country,int population, int vaxApplied){
	double percent = (((double)vaxApplied/2)/population)*100;
	printf("Pais:%s\nPoblacion: %d\nDosis aplicadas: %d\nPorcentaje: %f%%\n",country,population,vaxApplied,percent);
}

