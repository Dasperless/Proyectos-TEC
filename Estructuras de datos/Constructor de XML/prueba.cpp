#include "MakeFile.hpp"
#include "XMLNode.hpp"
#include "XMLDocument.hpp"

#include <iostream>
int main()
{
    XMLDocument *xmlDocument = new  XMLDocument();
    xmlDocument->root("semestre");
    xmlDocument->setbalanced(1000);
    xmlDocument->child("Materias");
    xmlDocument->child("Cursos");
    xmlDocument->child("Cursos2");
    xmlDocument->child("Cursos3");
    xmlDocument->child("Cursos4");
    xmlDocument->save("semestre.xml");


    // MakeFile *newMakeFile = new MakeFile();
    // NodeAttribute *atributo1 = new NodeAttribute("carnet", "2018123226");
    // NodeAttribute *atributo2 = new NodeAttribute("id", "1234");
    // XMLNode *estudiantes = new XMLNode("Estudiates", 1);
    // XMLNode *nodoEstudiante = new XMLNode("Dario", 2);
    // XMLNode *curso1 = new XMLNode("POO", 4);
    // XMLNode *curso2 = new XMLNode("Datos", 3);
    

    // estudiantes->insertChild(nodoEstudiante);
    // nodoEstudiante->insertChild(curso2);
    // nodoEstudiante->insertChild(curso1);
    
    // nodoEstudiante->getAttributes()->insertFirst(atributo1);
    // newMakeFile->newFile(estudiantes, "nuevo.xml");
}
