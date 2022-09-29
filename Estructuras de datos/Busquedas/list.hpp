#ifndef LIST_HPP
#define lIST_HPP
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <chrono>
#include "node.hpp"

using namespace std;
class list
{
private:
    node *apFirstNode;
    node *apLastNode;
    bool aSorted;
    int aCounter;

public:
    list()
    {
        apFirstNode = nullptr;
        apLastNode = nullptr;
        aSorted = false;
        aCounter = 0;
    }

    void insertNode(node *newNode)
    {
        aCounter++;
        if (apFirstNode == nullptr) // Si el primer nodo es nulo
        {
            setFirstNode(newNode);
            setLastNode(newNode);
        }
        else // Si el primer nodo no es nulo
        {
            newNode->setNext(apFirstNode);
            setFirstNode(newNode);
        }
    }

    void *randomNumList(int size)
    {
        srand(time(NULL)); //Semilla
        auto start = chrono::system_clock::now();
        for (int i = 0; i < size; i++)
        {
            int randNum = rand() % (100000);
            node *newNode = new node(randNum);
            this->insertNode(newNode);
        }
        auto end = chrono::system_clock::now();
        chrono::duration<float, milli> duration = end - start;
        cout << duration.count() << " milisegundos" << endl;
    }

    //Algoritmos de busqueda
    node *linealSearch(int searchValue)
    {
        auto start = chrono::system_clock::now();
        node *current = apFirstNode;
        while (current != nullptr)
        {
            if (searchValue == current->getValue())
                return current;
            current = current->getNext();
        }
        auto end = chrono::system_clock::now();
        chrono::duration<float, milli> duration = end - start;
        cout << duration.count() << " milisegundos" << endl;
        return nullptr;
    }

    node *binarySearch(int searchValue)
    {
        auto start = chrono::system_clock::now();
        node *current = apFirstNode;
        while (current != nullptr)
        {
            if (current->getValue() == searchValue)
            {
                return current;
            }
            else if(searchValue > current->getValue()){
                return nullptr;
            }
            current = current->getNext();
        }
        auto end = chrono::system_clock::now();
        chrono::duration<float, milli> duration = end - start;
        cout << duration.count() << " milisegundos" << endl;
        return nullptr;
    }
    
    node *linearInterpolation(int searchValue)
    {
    }

    //Algoritmos de ordenamiento quicksort
    void quickSort()
    {
        int nodeList[aCounter];
        auto start = chrono::system_clock::now();
        node *current = apFirstNode;
        for (int i = 0; i < aCounter; i++)
        {
            nodeList[i] = current->getValue();
            current = current->getNext();
        }
        quickSortAux(nodeList, 0, aCounter - 1);

        node *newNode;
        apFirstNode = nullptr;
        apLastNode = nullptr;
        int tempCounter = aCounter;
        aCounter = 0;
        for (int i = 0; i < tempCounter; i++)
        {
            newNode = new node(nodeList[i]);
            this->insertNode(newNode);
        }
        auto end = chrono::system_clock::now();
        chrono::duration<float, milli> duration = end - start;
        cout << "Duración quicksort: " << duration.count() << " milisegundos" << endl;
    }

    void quickSortAux(int *arr, int low, int high)
    {
        if (low < high)
        {
            int pi = partition(arr, low, high);
            quickSortAux(arr, low, pi - 1);
            quickSortAux(arr, pi + 1, high);
        }
    }

    int partition(int arr[], int low, int high)
    {
        int pivot = arr[high]; // pivot
        int i = (low - 1);     // Index of smaller element

        for (int j = low; j <= high - 1; j++)
        {
            // If current element is smaller than the pivot
            if (arr[j] > pivot)
            {
                i++; // increment index of smaller element
                swap(&arr[i], &arr[j]);
            }
        }
        swap(&arr[i + 1], &arr[high]);
        return (i + 1);
    }

    void swap(int *a, int *b)
    {
        int t = *a;
        *a = *b;
        *b = t;
    }

    list *binSort()
    {
    }

    //Algoritmo de ordenamiento burbuja
    list *bubbleSort()
    {
        bool sorted;
        node *prevNode = nullptr;
        node *currentNode = apFirstNode;
        node *nextNode = apFirstNode->getNext();

        auto start = chrono::system_clock::now();
        while (!sorted)
        {
            if (nextNode == nullptr)
            {
                prevNode = nullptr;
                currentNode = apFirstNode;
                nextNode = apFirstNode->getNext();
            }
            if (prevNode == nullptr)
            {
                if (currentNode->getValue() > nextNode->getValue())
                {
                    setFirstNode(nextNode);
                    currentNode->setNext(nextNode->getNext());
                    nextNode->setNext(currentNode);
                    node *temp1 = nextNode;
                    node *temp2 = currentNode;
                    currentNode = temp1;
                    nextNode = temp2;
                }
            }
            else
            {
                if (currentNode->getValue() > nextNode->getValue())
                {
                    prevNode->setNext(nextNode);
                    currentNode->setNext(nextNode->getNext());
                    nextNode->setNext(currentNode);
                    node *temp1 = nextNode;
                    node *temp2 = currentNode;
                    currentNode = temp1;
                    nextNode = temp2;
                }
            }
            prevNode = currentNode;
            currentNode = currentNode->getNext();
            nextNode = nextNode->getNext();
            sorted = isSorted();
        }
        auto end = chrono::system_clock::now();
        chrono::duration<float, milli> duration = end - start;
        cout << duration.count() << " milisegundos" << endl;
    }

    bool isSorted()
    {
        node *currentNode = apFirstNode;
        while (currentNode->getNext() != nullptr)
        {
            if (currentNode->getValue() > currentNode->getNext()->getValue())
                return false;
            currentNode = currentNode->getNext();
        }
        setLastNode(currentNode);
        return true;
    }

    //Impresion de los nodos
    void printNodes()
    {
        node *current = apFirstNode;
        for (int i = 0; i < aCounter; i++)
        {
            cout << "[" << current->getValue() << "]"
                 << "->";
            current = current->getNext();
        }
        cout << "\n";
    }

    // Setter y getters
    void setFirstNode(node *firstNode) { apFirstNode = firstNode; }
    void setLastNode(node *lastNode) { apLastNode = lastNode; }
    void setSorted(bool sorted) { aSorted = sorted; }
    node *getFirstNode() { return apFirstNode; }
    node *getLastNode() { return apLastNode; }
    bool getSorted() { return aSorted; }
    int getCounter() { return aCounter; }
};
#endif