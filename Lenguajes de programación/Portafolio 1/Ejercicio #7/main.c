#include <stdio.h>
int ValidateTime(int hh , int mm)
{
    int ret=0;
    
    if(hh>24||hh<0)   ret=1;
    if(mm>60||mm<0)   ret=1;
    
    return ret;
}
int main(int argc, char const *argv[])
{
	char buffer[100]={0};
	int ret,hour,min;
	printf("\nIngrese la hora de inicio \"hh:mm\": ");
	fgets(buffer,100,stdin);

	sscanf(buffer , "%d:%d:%d" , &hour,&min);

	ret = ValidateTime(hour,min);

	if (ret){
		printf("\nFormato del tiempo inválido.\n");
	}
    else
    {
        printf("\nThe Time is : %d:%d\n",hour,min);
    }	
	
}
