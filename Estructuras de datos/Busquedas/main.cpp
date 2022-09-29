#include <iostream>
#include "node.hpp"
#include "list.hpp"

using namespace std;
list *newList = new list();

void randomList();
int validInput();
int validInput(int min, int max);
void makeListMenu();
void searchMenu();

int main()
{
    bool notBreak = true;
    while (notBreak)
    {
        cout << "\n -- Menu -- " << endl;
        cout << "1) Generar nueva lista" << endl;
        cout << "2) Buscar" << endl;
        cout << "3) Salir" << endl;

        int option = validInput();
        switch (option)
        {
        case 1:
            makeListMenu();
            break;
        case 2:
            if (newList->getFirstNode() == nullptr)
                cout << ">>>Error: La lista está vacia" << endl;
            else
                searchMenu();
            break;
        case 3:
            notBreak = false;
            break;
        default:
            cout << "\n>>>Error: la opción no existe" << endl;
            break;
        }
    }
}

void sortMenu()
{
    cout << "\n -- Menu de ordenamiento " << endl;
    cout << "1) Quicksort" << endl;
    cout << "2) Binsort" << endl;
    cout << "3) Burbuja" << endl;
    cout << "4) Salir" << endl;

    int size;
    bool notBreak = true;
    while (notBreak)
    {
        int option = validInput();
        switch (option)
        {
        case 1:
            newList->quickSort();
            notBreak = false;
            break;
        case 2:
            newList->binSort();
            notBreak = false;
            break;
        case 3:
            newList->bubbleSort();
            notBreak = false;
            break;
        case 4:
            notBreak = false;
            break;
        default:
            cout << ">>> Error: Opción incorrecta" << endl;
            break;
        }
    }
}
void makeListMenu()
{
    cout << "\n-- Crear nueva lista -- " << endl;
    cout << "¿Desea ordenar la lista? [1:Sí|2:No]" << endl;
    cout << "Presiona [3] para cancelar" << endl;

    int size;
    bool notBreak = true;
    while (notBreak)
    {
        int option = validInput();
        switch (option)
        {
        case 1:
            cout << "\nElija el tamaño" << endl;
            size = validInput();
            newList->randomNumList(size);
            sortMenu();
            notBreak = false;
            break;
        case 2:
            cout << "\nElija el tamaño" << endl;
            size = validInput();
            newList->randomNumList(size);
            notBreak = false;
            break;
        case 3:
            notBreak = false;
        default:
            cout << ">>> Error: Opción incorrecta" << endl;
            break;
        }
    }
}

void searchMenu()
{
    bool notBreak = true;
    int value;

    while (notBreak)
    {
        newList->printNodes();
        cout << "Dijite el nodo a buscar" << endl;
        value = validInput();

        cout << "\nTipos de búsqueda" << endl;
        cout << "1) Búsqueda lineal" << endl;
        cout << "2) Busqueda binarea" << endl;
        cout << "3) Busqueda por interpolacion" << endl;
        cout << "4) Cancelar" << endl;

        int option = validInput();
        node *searchedNode;
        switch (option)
        {
        case 1:
            searchedNode = newList->linealSearch(value);
            if (searchedNode != nullptr)
                cout << "[" << newList->linealSearch(value) << "]> " << searchedNode->getValue() << endl;
            else
                cout << "No se encontró el valor" << endl;
            notBreak = false;
            break;
        case 2:
            if (!newList->isSorted())
            {
                cout << "\n La lista no esta ordenada" << endl;
                sortMenu();
            }
            searchedNode = newList->binarySearch(value);
            if (searchedNode != nullptr)
                cout << "[" << searchedNode << "]> " << searchedNode->getValue() << endl;
            else
                cout << "No se encontró el valor" << endl;
            notBreak = false;
            break;
        case 3:
            cout << "Busqueda por interpolacion" << endl;
            notBreak = false;
            break;
        case 4:
            notBreak = false;
            break;
        default:
            cout << ">>> Error: Opción incorrecta" << endl;
            break;
        }
    }
}

int validInput(int min, int max)
{
    int option;
    do
    {
        cout << "[#]> ";
        cin.clear();
        cin.ignore();
    } while (!cin >> option || (option < min && option > max));
    return option;
}

int validInput()
{
    int option;
    cout << "[#]>";
    while (!(cin >> option))
    {
        cin.clear();
        cin.ignore();
        cout << "[#]>";
    }
    return option;
}