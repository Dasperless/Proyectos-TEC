#include <iostream>
int strlen(char *c)
{
    int size = 0;
    if (c != nullptr)
        for (int i = 0; c[i] != '\0'; i++)
            size++;
    return size;
}

int strlen(const char *c)
{
    int size = 0;
    if (c != nullptr)
        for (int i = 0; c[i] != '\0'; i++)
            size++;
    return size;
}

char *strcat(char *dest, char *src)
{
    int newStrSize = strlen(dest) + strlen(src);
    char *newStr = (char *)malloc(newStrSize * sizeof(char));
    int i = 0;
    int j = 0;
    int k = 0;
    while (i < newStrSize)
    {
        if (dest[j] != '\0')
        {
            newStr[i] = dest[j];
            j++;
        }
        else
        {
            newStr[i] = src[k];
            k++;
        }
        i++;
    }
    return newStr;
}

char *strcat(char *dest, const char *src)
{
    int newStrSize = strlen(dest) + strlen(src);
    char *newStr = (char *)malloc(newStrSize * sizeof(char));
    int i = 0;
    int j = 0;
    int k = 0;
    while (i < newStrSize)
    {
        if (dest[j] != '\0')
        {
            newStr[i] = dest[j];
            j++;
        }
        else
        {
            newStr[i] = src[k];
            k++;
        }
        i++;
    }
    return newStr;
}
// int main()
// {
//     char *c1 = "123";
//     char *c2 = "456";
//     std::cout << strcat(c1, c2) << std::endl;
// }