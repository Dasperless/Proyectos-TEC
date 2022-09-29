#include <stdio.h>

int main(){
	int nums  = 0;
	int num;
	printf("Escriba un numero: ");
	scanf("%d", &nums);
	int arr[nums];
	for(int i = 0; i < nums; i++){
		printf("Escriba el numero de la posicion %d: ", i);
		scanf("%d", &num);
		arr[i] = num;
	}

	for(int i = 0; i<nums; i++ ){
		printf("posicion #%d es %d \n", i,arr[i]);
	}
}