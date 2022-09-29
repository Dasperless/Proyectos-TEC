typedef struct VaxApplied
{
	char country[100];
	int population;
	int vaccinated;
	struct VaxApplied *next;
}vaxApplied;

void addVaxApplied(char* country, int population, int vaccined, vaxApplied **head){
	vaxApplied *newVax = (vaxApplied*) malloc(sizeof(vaxApplied));
	strcpy(newVax->country,country);
	newVax->population = population;
	newVax->vaccinated = vaccined;
	newVax->next = NULL;

	if((*head) == NULL){
		(*head) = newVax;
		return;
	}

	vaxApplied *current = (*head);
	while ((*head)->next!=NULL)
	{
		current = current->next;
	}

	current->next = newVax;
}