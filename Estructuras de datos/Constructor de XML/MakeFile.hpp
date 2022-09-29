#ifndef MAKEFILE_HPP
#define MAKEFILE_HPP
#include "XMLNode.hpp"
#include <iostream>
#include <fstream>
#include "string.hpp"
class MakeFile
{
private:
    char *string;
    char initSymbol[2] = "<";
    char endSymbol[2] = ">";

public:
    MakeFile()
    {
        string = nullptr;
    }

    void concatenate(char *dest, const char *src)
    {
        int newStringSize = strlen(src) + strlen(dest);                 //Tamaño de la concatenación
        char *newStr = (char *)malloc(newStringSize * sizeof(char *));  //Variable temporal para almacenar el nuevo string
        for (int i = 0; i < newStringSize; i++)                         //Copia el char* por posiciones.
            newStr[i] = strcat(dest, src)[i];

        string = (char *)malloc(newStringSize * sizeof(char *));        //Almacena el tamaño para string
        for (int i = 0; newStr[i] != '\0'; i++)                         //Copia el newStr en  string
            string[i] = newStr[i];
        // int newStringSize = sizeof(src) + sizeof(dest); //Tamaño de la concatenación
        // char *newString = (char *)malloc(newStringSize * sizeof(char *)); //Guardo el espacio suficiente para almacenar dest y src
        // string = (char *)malloc(newStringSize * sizeof(char *));
    }

    void newFile(XMLNode *root, char *filename)
    {
        char *xmlFile = makeTag(root);
        std::cout << xmlFile << std::endl;
        std::ofstream outfile(filename);
        outfile << xmlFile << std::endl;
        outfile.close();
    }

    void initTag(XMLNode *node)
    {
        if (string == nullptr)
            string = (char *)malloc(sizeof(node->getName()) * sizeof(char));
        concatenate(string, initSymbol);
        concatenate(string, node->getName());

        NodeAttribute *attributes = node->getAttributes()->getfirst();
        for (int i = 0; i < node->getAttributes()->getCuantity(); i++) //Se le concatena los atributos
        {
            concatenate(string, " ");                    // Se le concatena un espacio para los atributos
            concatenate(string, attributes->getKey());   // Se le concatena el nombre del atributo
            concatenate(string, "=");                    // Se concatena el igual
            concatenate(string, "\"");                   // Se concatenan las  comillas
            concatenate(string, attributes->getValue()); // Se concatena el valor
            concatenate(string, "\"");                   // Se concatena las comillas de cierre
            attributes = attributes->getNext();
        }
        concatenate(string, endSymbol);
    }

    char *makeBalancedTag(XMLNode *node)
    {
        initTag(node);

        if (node->getContentLocation() == 10 && node->getContent() != nullptr) // Se concatena el contenido al inicio
            concatenate(string, node->getContent());

        if (node->getLeft() != nullptr)
            makeBalancedTag(node->getLeft());
        if (node->getRight() != nullptr)
            makeBalancedTag(node->getRight());

        if (node->getContentLocation() == 20 && node->getContent() != nullptr) // Se concatena el contenido al inicio
            concatenate(string, node->getContent());
        endTag(node);
        return string;
    }

    char *makeTag(XMLNode *node)
    {
        if (node->getBalanced())
            return makeBalancedTag(node);
        initTag(node);
        if (node->getContentLocation() == 10 && node->getContent() != nullptr) // Se concatena el contenido al inicio
            concatenate(string, node->getContent());

        if (node->getChild() != nullptr)
            makeChilds(node->getChild());

        else if (node->getContentLocation() == 20 && node->getContent() != nullptr) // Se concatena el contenido al final
            concatenate(string, node->getContent());

        endTag(node);

        if (node->getNext() != nullptr)
            makeBrotherNode(node->getNext());
        return string;
    }

    /**
     * Crea la etiquta de cierra
     * 
     */
    void endTag(XMLNode *node)
    {
        concatenate(string, initSymbol);
        concatenate(string, "/");
        concatenate(string, node->getName());
        concatenate(string, endSymbol);
    }

    void makeBrotherNode(XMLNode *node)
    {
        XMLNode *current = node;
        while (current != nullptr)
        {
            makeTag(node);
            current = current->getNext();
        }
    }

    void makeChilds(XMLNode *child)
    {
        makeTag(child);
        XMLNode *childs = child;
        while (childs == nullptr)
        {
            makeChilds(childs);
            childs = childs->getChild();
        }
    }
};

#endif