
/*****Datos administrativos************************
 * Nombre del archivo: Card.hpp
 * Tipo de archivo:Encabezado
 * Proyecto: UNO distribuido
 * Autor:Dario Vargas, Daniel Villatoro, Daniel Calderon
 * Empresa:Tecnologico de Costa Rica
 *****Descripción**********************************
 * Clase que contiene los atributos y metodos de
 * una carta de UNO.
 *****Versión**************************************
 * ##    | Fecha y hora | Autor
 * 1.0.0    24/08/2019    Dario Vargas
 **************************************************/

#ifndef CARD_HPP
#define CARD_HPP 
#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

class Card {
/*****Nombre***************************************
 * Card.hpp
 *****Descripción**********************************
 * Clase con las caracteristicas de una carta 
 * de UNO
 *****Atributos************************************
 * string aColour
 * string aNumber
 * Card *aNext
 *****Métodos**************************************
 * string getColour()
 * string getNumber()
 * Card* getNext()
 * void setColour(string pColour)
 * void setNumber(string pNumber)
 * void setNext(Card *pNext)
 * string getCardInfo()
 **************************************************/
private:
    string aColour;
    string aNumber;
    bool aWild;
    Card *aNext;
public:
    Card(string pColour, string pNumber){
        setColour(pColour);
        setNumber(pNumber);
        setNext(nullptr);
    }

    void setColour(string pColour){
        aColour = pColour;
    }

    void setNumber(string pNumber){
        aNumber = pNumber;
    }

    void setNext(Card *pNext){
        aNext = pNext;
    }

    string getColour(){
        return aColour;
    }

    string getNumber(){
        return aNumber;
    }

    Card* getNext(){
        return aNext;
    }

/*****Nombre***************************************
 * getCardInfo()
 *****Descripción**********************************
 * retorna los atributos de la clase Carta
 *****Retorno**************************************
 * Un string 
 *****Entradas*************************************
 * No tiene entradas
 **************************************************/

    string getCardInfo(){
        int isWild = atoi(aNumber.c_str());
        string info;

        info += "[Color] : " + getColour() + "\n";
        if (isWild != 0){
            info += "[Numero] : " + getNumber() + "\n";
        } else {
            info += "[Comodin] : " + getNumber() + "\n";
        }
        return info;
    } 
};
#endif
