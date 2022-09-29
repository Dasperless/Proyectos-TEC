#include <iostream>
#include "Tree.hpp"

Tree *tree = new Tree();

int strlen(char *str)
{
    int len = 0;
    for (int i = 0; str[i] != 0; i++)
    {
        len++;
    }
    return len;
}
bool strcmp(char *a, char *b)
{
    if (strlen(a) != strlen(b))
        return false;
    for (int i = 0; a[i] == 0 || b[i] == 0; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }
    }
    return true;
}
void insertNode()
{
    bool exit = false;
    while (!exit)
    {
        char *data = (char *)malloc(sizeof(char));
        std::cout << "Ingrese el \\exit para finalizar" << std::endl;
        std::cout << "Ingrese el dato: ";

        std::cin >> data;
        data = (char *)realloc(data, strlen(data) * sizeof(char));
        if (strcmp(data, "\\exit"))
            exit = true;
        if (!exit)
            tree->insertRecursive(data);
    }
}

void deleteNode()
{
    bool exit = false;
    while (!exit)
    {
        char *data = (char *)malloc(sizeof(char));
        std::cout << "Ingrese el \\exit para finalizar" << std::endl;
        std::cout << "Ingrese el nombre del nodo a eliminar: ";

        std::cin >> data;
        data = (char *)realloc(data, strlen(data) * sizeof(char));
        if (strcmp(data, "\\exit"))
            exit = true;
        if (!exit)
            tree->deleteNode(data);
    }    
}

int input()
{
    int option;
    while (!(std::cin >> option))
    {
        std::cin.clear();
        std::cin.ignore();
        std::cout << "[E]: Debe ingresar un número" << std::endl;
        std::cout << "[#]>";
        printf("\n");
    }
    printf("\n");
    return option;
}

void printTree()
{
    bool exit = false;
    while (!exit)
    {
        std::cout << "Imprimir Nodos" << std::endl;
        std::cout << "1. Prefijo " << std::endl;
        std::cout << "2. Infijo " << std::endl;
        std::cout << "3. Sufijo " << std::endl;
        std::cout << "4. Cancelar " << std::endl;
        std::cout << "[#]>";

        int option = input();

        switch (option)
        {
        case 1:
            tree->printPrefix();
            break;
        case 2:
            tree->printInfix();
            break;
        case 3:
            tree->printSuffix();
            break;
        case 4:
            exit = true;
            break;
        default:
            std::cout << "[E]: No existe la opción" << std::endl;
            break;
        }
    }
}

int main()
{
    bool exit = false;
    while (!exit)
    {
        std::cout << "1. Insertar nodo " << std::endl;
        std::cout << "2. Borrar nodo " << std::endl;
        std::cout << "3. Imprimir arbol " << std::endl;
        std::cout << "4. Salir " << std::endl;
        std::cout << "[#]>";

        int option = input();

        switch (option)
        {
        case 1:
            insertNode();
            break;
        case 2:
            deleteNode();
            break;
        case 3:
            printTree();
            break;
        case 4:
            exit = true;
            break;
        default:
            std::cout << "[E]: No existe la opción" << std::endl;
            break;
        }
    }
}