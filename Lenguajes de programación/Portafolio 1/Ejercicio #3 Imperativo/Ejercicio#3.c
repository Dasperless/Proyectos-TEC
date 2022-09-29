#include <stdio.h>
#include <string.h>

char* separaString(char* str){
    char* nuevoStr;
    nuevoStr= strtok(str, " ");
	return nuevoStr;
}

void imprimirString(char* str){
    while (str!= NULL)
    {
        printf("%s\n", str);
        str= strtok(NULL, " ");
    }	
}
int main()
{
    char str[] = "Hola mundo bonito";
	char* nuevoStr = separaString(str);
	imprimirString(nuevoStr);
    return 0;
}