/*****Datos administrativos************************
 * Nombre del archivo: Player.hpp
 * Tipo de archivo:Encabezado
 * Proyecto: UNO distribuido
 * Autor:Dario Vargas, Daniel Villatoro, Daniel Calderon
 * Empresa:Tecnologico de Costa Rica
 *****Descripción**********************************
 * Clase que contiene los atributos y metodos de
 * un jugador
 *****Versión**************************************
 * ##    | Fecha y hora | Autor
 * 1.0.0    25/08/2019    Dario Vargas
 **************************************************/
#ifndef PLAYER_HPP
#define PLAYER_HPP

#include <string>
#include "List.hpp"
#include "Card.hpp"

using namespace std;

class Player {
/*****Nombre***************************************
 * Deck.hpp
 *****Descripción**********************************
 * Clase con las caracteristicas de un jugador
 *****Atributos************************************
 * string aName  
 * Player *aNext
 * Player *aPrev
 * List<Card> *aPlayerDeck
 *****Métodos**************************************
 * void setName(string pName)
 * void setNext(Player *pNext)
 * void setPrev(Player *pPrev)
 * void setPlayerDeck(List<Card>)
 * void setScore(int pScore)
 * void addCard(Card *pCards)
 * string* getName()
 * Player* getNext()
 * Player* getPrev()
 * List<Card>* getPlayerDeck()
 * int getScore(
 **************************************************/    
private:
    string aName;  
    Player *aNext;
    Player *aPrev;
    List<Card> *aPlayerDeck;    
    int aScore;
public:
    Player(string pName){
        setName(pName);
        setNext(nullptr);
        setPrev(nullptr);
        aPlayerDeck = nullptr;
    }

    void setName(string pName){
        aName = pName;
    }

    void setNext(Player *pNext){
        aNext = pNext;
    }

    void setPrev(Player *pPrev){
        aPrev = pPrev;
    }

    void setPlayerDeck(List<Card> *pPlayerDeck){
        aPlayerDeck = pPlayerDeck;
    }

    void setScore(int pScore){
        aScore = pScore;
    }

/*****Nombre***************************************
 * addCard
 *****Descripción**********************************
 * inserta una nueva carta a la baraja
 *****Retorno**************************************
 * No retorna ninguna valor 
 *****Entradas*************************************
 * un puntero a un objeto de tipo Card
 **************************************************/
    void addCard(Card *pCard){
       aPlayerDeck->insertNode(pCard);
    }

    string getName(){
        return aName;
    }

    Player* getNext(){
        return aNext;
    }

    Player* getPrev(){
        return aPrev;
    }

    List<Card>* getPlayerDeck(){
        return aPlayerDeck; 
    }

    int getScore(){
        return aScore;
    }

    string getCards(){
        string msg;
        Card *currentCard = aPlayerDeck->getFirstNode();
        for (int i = 0; currentCard!= nullptr; i++)
        {
            msg += "Carta #" + to_string(i) + "\n";
            msg += currentCard->getCardInfo() + "\n";
        }

        return msg;
        
    }


};
#endif