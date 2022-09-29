#ifndef TREE_HPP
#define TREE_HPP
#include "Node.hpp"
#include <iostream>

class Tree
{
private:
    Node *aRoot;

public:
    Tree()
    {
        aRoot = nullptr;
    }
    //Sección de métodos
    int strlen(char *str)
    {
        int len = 0;
        for (int i = 0; str[i] != 0; i++)
        {
            len++;
        }
        return len;
    }

    void printPrefix()
    {
        printPrefix("", aRoot);
    }
    void printPrefix(char *prefix, Node *current)
    {
        if (current != NULL)
        {
            int size = strlen(prefix);
            char lPrefix[size + 2];
            char rPrefix[size + 2];
            std::sprintf(lPrefix, "\t%sl", prefix);
            std::sprintf(rPrefix, "\t%sr", prefix);

            std::cout << prefix << current->getData() << std::endl;
            printPrefix(rPrefix, current->getRight());
            printPrefix(lPrefix, current->getLeft());
        }
    }

    void printInfix()
    {
        printInfix("", aRoot);
    }
    void printInfix(char *prefix, Node *current)
    {
        if (current != NULL)
        {
            int size = strlen(prefix);
            char lPrefix[size + 2];
            char rPrefix[size + 2];
            std::sprintf(lPrefix, prefix);
            std::sprintf(rPrefix, prefix);

            printInfix(rPrefix, current->getRight());
            std::cout << prefix << current->getData() << std::endl;
            printInfix(lPrefix, current->getLeft());
        }
    }

    void printSuffix()
    {
        printSuffix("", aRoot);
    }
    void printSuffix(char *prefix, Node *current)
    {
        if (current != NULL)
        {
            int size = strlen(prefix);
            char lPrefix[size + 2];
            char rPrefix[size + 2];
            std::sprintf(lPrefix, "\t%sl", prefix);
            std::sprintf(rPrefix, "\t%sr", prefix);

            printSuffix(rPrefix, current->getRight());
            printSuffix(lPrefix, current->getLeft());
            std::cout << prefix << current->getData() << std::endl;
        }
    }
    void insertRecursive(char *pData)
    {
        if (aRoot == nullptr)
            aRoot = new Node(pData);
        else
            insertRecursive(pData, aRoot, aRoot);
    }
    int strcmp(char *a, char *b)
    {
        for (int i = 0; a[i] != 0 || b[i] != 0; i++)
        {
            if (a[i] < b[i])
                return -1;
            else if (a[i] > b[i])
                return 1;
        }
        if (strlen(a) < strlen(b))
            return -1;
        else
            return 0;
    }

    void insertRecursive(char *pData, Node *grandParent, Node *parent)
    {
        bool balancear = true;
        if (strcmp(pData, parent->getData()) == 1)
            if (parent->getRight() == nullptr)
                parent->setRight(new Node(pData));
            else
                insertRecursive(pData, parent, parent->getRight());
        else if (strcmp(pData, parent->getData()) == -1)
            if (parent->getLeft() == nullptr)
                parent->setLeft(new Node(pData));
            else
                insertRecursive(pData, parent, parent->getLeft());
        else
            balancear = false; // ya existía

        if (balancear)
        {
            parent->balanceFactor();
            if (parent->getBalanceFactor() > 1 || parent->getBalanceFactor() < -1)
            {
                if (strcmp(pData, parent->getData()) == 1)
                {
                    // el primer movimiento fue hacia la derecha
                    if (strcmp(pData, parent->getRight()->getData()) == 1)
                        //El segundo movimiento fue a la derecha
                        simpleLeftRotation(grandParent, parent);
                    else
                        // El segundo movimiento fue hacia la izquierda
                        doubleLeftRotation(grandParent, parent);
                }
                else
                {
                    // el primer movimiento fue hacia la derecha
                    if (strcmp(pData, parent->getRight()->getData()) == 1)
                        simpleRightRotation(grandParent, parent);
                    //El segundo movimiento fue a la derecha
                    else
                        // El segundo movimiento fue hacia la izquierda
                        doubleRightRotation(grandParent, parent);
                }
            }
        }
    }

    void simpleRightRotation(Node *grandParent, Node *parent)
    {
        std::cout << "Rotación simple a la derecha" << std::endl;
        Node *temp = parent->getLeft();
        Node *right = temp->getRight();
        parent->setLeft(right);
        temp->setRight(parent);
        if (parent == aRoot)
            aRoot = temp;
        else if (grandParent != nullptr)
            grandParent->setLeft(temp);
    }

    void simpleLeftRotation(Node *grandParent, Node *parent)
    {
        std::cout << "Rotación simple a la izquierda" << std::endl;
        Node *temp = parent->getRight();
        Node *left = temp->getLeft();
        parent->setRight(left);
        parent->setRight(temp->getLeft());
        temp->setLeft(parent);
        if (parent == aRoot)
            aRoot = temp;
        else if (grandParent != nullptr)
            grandParent->setRight(temp);
    }

    void doubleRightRotation(Node *grandParent, Node *parent)
    {
        std::cout << "Rotación doble a la derecha " << std::endl;
        Node *left = parent->getLeft();      //B
        Node *right = left->getRight();      //E
        Node *tempLeft = right->getLeft();   //F
        Node *tempRight = right->getRight(); //G

        left->setRight(tempLeft);
        right->setLeft(left);
        parent->setLeft(tempRight);
        right->setRight(parent);

        if (parent == aRoot)
            aRoot = right;
        else if (grandParent != nullptr)
            grandParent->setLeft(right);
    }

    void doubleLeftRotation(Node *grandParent, Node *parent)
    {
        std::cout << "Rotación doble a la izquierda " << std::endl;
        Node *right = parent->getRight();   //C
        Node *left = right->getLeft();      //D
        Node *tempRight = left->getRight(); //G
        Node *tempLeft = left->getLeft();   //F

        right->setLeft(tempRight);
        left->setRight(right);
        parent->setRight(tempLeft);
        left->setLeft(parent);

        if (parent == aRoot)
            aRoot = left;
        else if (grandParent != nullptr)
            grandParent->setRight(left);
    }

    Node *greaterNode(Node *parent)
    {
        Node *current = parent;
        while (current->getRight() != nullptr)
        {
            current = current->getRight();
        }
        return current;
    }

    Node *deleteNode(char *pNode)
    {
        aRoot = deleteNode(pNode, nullptr, aRoot);
        return aRoot;
    }

    Node *deleteNode(char *pNode, Node *parent, Node *current)
    {
        if (current == nullptr)
            return nullptr;
        else if (strcmp(pNode, current->getData()) == 1)
            deleteNode(pNode, current, current->getRight());
        else if (strcmp(pNode, current->getData()) == -1)
            deleteNode(pNode, current, current->getLeft());
        else
        {

            if (current->getLeft() == nullptr) //Si el nodo solo tiene un hijo derecho
            {
                if (current == aRoot)
                    return current->getRight();
                else
                    parent->setRight(nullptr);
            }
            else if (current->getRight() == nullptr) //Si el nodo solo tiene un hijo izquierdo
            {
                if (current == aRoot)
                    return current->getLeft();
                else
                    parent->setLeft(nullptr);
            }
            else if (current->getLeft() == nullptr && current->getRight() == nullptr) //Nodo hoja
                if (strcmp(pNode, parent->getData()) == 1)
                    parent->setRight(nullptr);
                else
                    parent->setLeft(nullptr);
            else if (current->getRight() != nullptr && current->getLeft() != nullptr) //Si el nodo a eliminar tiene 2 hijos.
            {
                std::cout << "El nodo tiene 2 hijos" << std::endl;
                Node *leftNode = current->getLeft();
                Node *largest = greaterNode(leftNode);

                if (current == aRoot)
                {
                    aRoot->setData(largest->getData());
                }
                else
                {
                    if (strcmp(pNode, parent->getData()) == 1)
                        parent->setRight(greaterNode(current->getLeft()));
                    else
                        parent->setLeft(greaterNode(current->getLeft()));
                }
            }
        }
        return current;
    }

    //Sección de setters.
    void setRoot(Node *pRoot) { aRoot = pRoot; }

    //Sección de getters.
    Node *getRoot() { return aRoot; }
};
#endif