/*****Datos administrativos************************
 * Nombre del archivo: Deck.hpp
 * Tipo de archivo:Encabezado
 * Proyecto: UNO distribuido
 * Autor:Dario Vargas, Daniel Villatoro, Daniel Calderon
 * Empresa:Tecnologico de Costa Rica
 *****Descripción**********************************
 * Clase que contiene los atributos y metodos de
 * una mazo de cartas
 *****Versión**************************************
 * ##    | Fecha y hora | Autor
 * 1.0.0    24/08/2019    Dario Vargas
 **************************************************/
#ifndef DECK_HPP
#define DECK_HPP

#include "List.hpp"
#include "Card.hpp"
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;
class Deck {
/*****Nombre***************************************
 * Deck.hpp
 *****Descripción**********************************
 * Clase con las caracteristicas de un mazo de 
 * cartas de UNO
 *****Atributos************************************
 * int aCounter
 * List<Card> *aCardDeck
 * List<Card> *aDiscarDeck
 *****Métodos**************************************
 * void addToDeck(Card pCard)
 * void addToDiscDeck(Card pCard)
 * Card* takeCard()
 * void newDeck()
 * void fillDeck()
 **************************************************/    
private:
    int aCounter;
    List<Card> *aCardDeck;
    List<Card> *aDiscDeck;
public:
    Deck(){
        aCardDeck = new List<Card>() ;
        aDiscDeck = new List<Card>();
        newDeck();
    }

    void addToDeck(Card *pCard){
        aCardDeck->insertNode(pCard);
    }

    void addToDiscDeck(Card *pCard){
        aDiscDeck->insertNode(pCard);
    }

    Card* takeCard(){
        Card* dCard = aCardDeck->pop();
        addToDiscDeck(dCard);
        return dCard;
    }

    void showDeck(){
        Card *current = aCardDeck->getFirstNode();
        while(current != nullptr){
            cout << current->getNumber() << endl;
            current = current->getNext();
        }
    }

    void newDeck(){
        aCardDeck = new List<Card>();
        string colours[4] = {"Azul", "Verde", "Rojo", "Amarillo"}; 
        string specials[3] = {"+2", "Reversa", "Salta"}; 
        string wilds[2] = {"comodin", "+4" };

        for(int i = 0; i < 19; i++){
            for (int j = 0; j <= 9; j++){
                for (int k = 0; k < 4; k++){
                    Card *card = new Card(colours[k],to_string(j));    
                }
            }
            
        }

        for (int i = 0; i < 8; i++){
            for (int j = 0; i < 2; i++){
                for (int k = 0; k < 3; k++){
                    for (int l = 0; l < 4; l++){
                        Card *special = new Card(colours[l],specials[k]); 
                        aCardDeck->insertNode(special);      
                    }          
                }
            }
        }

        for (int i = 0; i < 4; i++){
            for(int j = 0; j < 2; j++){
                Card *wild = new Card("Multi",wilds[j]); 
                aCardDeck->insertNode(wild);   
            }
        }         
    }

    void fillDeck(){
        Card *current = aDiscDeck->getFirstNode();

        while (current != nullptr){
            aCardDeck->insertNode(current);
            current = current->getNext();
        }
        aDiscDeck = nullptr;
    }

    List<Card>* getDiscDeck(){
        return aDiscDeck;
    }

    List<Card>* getCardDeck(){
        return aCardDeck;
    }

};
#endif