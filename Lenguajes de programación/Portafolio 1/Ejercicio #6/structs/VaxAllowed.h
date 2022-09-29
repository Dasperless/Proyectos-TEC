
typedef struct VaxAllowed
{
	char name[100];
	char country[100];
	char organization[100];
	struct VaxAllowed *next;
} vaxAllowed;

void addVaxAllowed(char *name, char *country, char *organization, vaxAllowed **head)
{
	vaxAllowed *newVax = (vaxAllowed *)malloc(sizeof(vaxAllowed));
	vaxAllowed *current = (*head);

	strcpy(newVax->name, name);
	strcpy(newVax->country, country);
	strcpy(newVax->organization, organization);
	newVax->next = NULL;

   if (*head == NULL)
    {
       (*head) = newVax;
	   (*head)->next = NULL;
       return;
    } 
    while (current->next != NULL)
        current = current->next;
  
    current->next = newVax;
	
    return;   
}