/*****Datos administrativos************************
 * Nombre del archivo: Uno.hpp
 * Tipo de archivo:Encabezado
 * Proyecto: UNO distribuido
 * Autor:Dario Vargas, Daniel Villatoro, Daniel Calderon
 * Empresa:Tecnologico de Costa Rica
 *****Descripción**********************************
 * Clase que contiene los atributos y metodos de un
 * juego de UNO
 *****Versión**************************************
 * ##    | Fecha y hora | Autor
 * 1.0.0    25/08/2019    Dario Vargas
 **************************************************/
#ifndef UNO_HPP
#define UNO_HPP

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <string>

#include "Player.hpp"
#include "List.hpp"
#include "Deck.hpp"

using namespace std;

class Uno {
/*****Nombre***************************************
 * Uno.hpp
 *****Descripción**********************************
 * Clase con las reglas del UNo
 *****Atributos************************************
 * Player *aCurrentPlayer
 * Deck *aGameDeck
 * List<Player> *aPlayerList 
 *****Métodos**************************************
 * void setCurrentPlayer(Player *pCurrent)
 * void setGameDeck(Deck *pGameDeck)
 * void setPlayerList(List<Player> pPlayerList)
 * Player* getCurrentPlayer()
 * Deck* getGameDeck()
 * List<Player> getPlayerList()
 **************************************************/      
private:
    Player *aCurrentPlayer;
    Deck *aGameDeck;
    List<Player> *aPlayerList;
    bool aReverse;
public:
    Uno(){
        aCurrentPlayer = nullptr;
        aGameDeck = new Deck();
        aPlayerList = nullptr;
        aReverse = false;
    }

    Uno (List<Player> *pPlayerList){
        aCurrentPlayer = nullptr;
        aGameDeck = new Deck();
        aPlayerList = pPlayerList;
        aReverse = false;
    }

    void shuffle(){
        Player *current = aPlayerList->getFirstNode();
        while (current->getNext() != aPlayerList->getFirstNode()){
            for(int i = 0; i < 7; i++){
                cout << aGameDeck->takeCard()->getNumber() << endl;
                //current->addCard(aGameDeck->takeCard());
            }
            current = current->getNext();
        }
    }

    void startGame(){
        aCurrentPlayer = setFirstPlayer();
        shuffle();
        // while(aCurrentPlayer->getScore() != 500 || aCurrentPlayer->getPlayerDeck()->getNum() != 1){
        //     int cardIndex;
        //     do{
        //         // cin.clear();
        //         // cin.ignore();
        //         cout << aCurrentPlayer->getPlayerDeck() << endl;
        //         cin >> cardIndex;
        //     } while(cardIndex > aCurrentPlayer->getPlayerDeck()->getNum());
        //     discarCard(getCardByIndex(cardIndex));
            
        //     if(!aReverse){
        //         aCurrentPlayer = aCurrentPlayer->getNext();
        //     } else {
        //         aCurrentPlayer = aCurrentPlayer->getPrev();
        //     }
        // }
    }

    Card* getCardByIndex(int index){
        Card *currentCard = aCurrentPlayer->getPlayerDeck()->getFirstNode();

        for (int i = 1; i < aCurrentPlayer->getPlayerDeck()->getNum() + 1; i++){
            currentCard = currentCard->getNext();
        }
        return currentCard;
    }
    
    string discarCard(Card *pCard){
        Card *discCard = aGameDeck->getDiscDeck()->getFirstNode(); //Primera carta de la pila
        string cardNum = pCard->getNumber();
        string cardColour = pCard->getColour();
        string playerName = aCurrentPlayer->getName();
        Player *nextPlayer;
        string msg;

        if(cardColour== discCard->getColour() || pCard->getNumber() == discCard->getNumber() || cardColour== "Multi"){                   
            int card = stoi(cardNum);
            if (card >= 0 || card <= 9) {
                aGameDeck->addToDiscDeck(pCard);
                aCurrentPlayer->setScore(stoi(pCard->getNumber()));
                msg += "Se coloco la carta " + cardNum + " de color "  + cardColour +"\n";
                msg += "Se añaden " + cardNum + " puntos al jugador " + playerName  + "\n";
                
            } else if(pCard->getNumber() == "+2"){
                if (!aReverse){
                    nextPlayer = aCurrentPlayer->getNext();
                } else {
                    nextPlayer = aCurrentPlayer->getPrev();
                }

                for(int i = 0; i < 2; i++){
                    nextPlayer->addCard(aGameDeck->takeCard());
                }
                aCurrentPlayer->setScore(20);
                msg += "Se coloco la carta " + cardNum + " de color "  + cardColour +"\n";
                msg += "Se añaden 20 puntos al jugador " + playerName + "\n";
                msg += "El jugador " + nextPlayer->getName() + " come 2 cartas " + "\n";

            } else if (pCard->getNumber() == "+4"){
                if (!aReverse){
                    nextPlayer = aCurrentPlayer->getNext();
                } else {
                    nextPlayer = aCurrentPlayer->getPrev();   
                }

                for(int i = 0; i < 4; i++){
                    nextPlayer->addCard(aGameDeck->takeCard());
                }                
                msg += "Se coloco la carta " + cardNum + " de color "  + cardColour +"\n";
                msg += "Se añaden 50 puntos al jugador " + playerName + "\n";
                msg += "El jugador " + nextPlayer->getName() + " come 4 cartas " + "\n";                
                aCurrentPlayer->setScore(50);

            } else if (pCard->getNumber() == "Reversa"){
                // bandera de reversa
                if (!aReverse){
                    nextPlayer = aCurrentPlayer->getNext();
                } else {
                    nextPlayer = aCurrentPlayer->getPrev();
                }                
                aReverse = !aReverse;
                aCurrentPlayer->setScore(20);
                msg += "Se coloco la carta " + cardNum + " de color "  + cardColour+"\n";
                msg += "Se añaden 20 puntos al jugador " + playerName + "\n";
                msg += "Se cambio el sentido, ahora el siguiente jugador sera " + nextPlayer->getName() + "\n";

            } else if (pCard->getNumber() == "Salta"){
                
                Player *nextPlayer;
                
                msg += "Se coloco la carta " + cardNum + " de color "  +  +"\n";
                msg += "Se añaden 20 puntos al jugador " + playerName + "\n";
                if(!aReverse){
                    nextPlayer = aCurrentPlayer->getNext()->getNext();
                    msg += "Se cambio el sentido de, ahora el siguiente jugador sera " + nextPlayer->getName() + "\n";
                    aCurrentPlayer = aCurrentPlayer->getNext();
                } else {
                    nextPlayer = aCurrentPlayer->getPrev()->getPrev();
                    msg += "Se cambio el sentido de, ahora el siguiente jugador sera " + nextPlayer->getName() + "\n";
                    aCurrentPlayer = aCurrentPlayer->getNext();                    
                }
                aCurrentPlayer->setScore(20);

            } else if (pCard->getNumber() == "Comodin"){
                // pedir al jugador que cambie que coloque una carta de otro
                // Mostrar las cartas del jugador actual
                aCurrentPlayer->setScore(50);
            }
        } else {
            msg += "La carta debe ser del mismo color o numero.";
        }
           return msg;
        
    }

    Player* setFirstPlayer(){
        srand(time(NULL));
        int num = rand() % (aPlayerList->getNum());
      //  cout << num << endl;
        Player *current = aPlayerList->getFirstNode();
        for(int i = 0; i < num; i++){
            current = current->getNext();
        }
        return current;
    }

    void setFirstDiscard(){
        Card *discardDeck = aGameDeck->getDiscDeck()->getFirstNode();
        List<Card> *cardsPile = aGameDeck->getCardDeck();
        if (discardDeck == nullptr) {
            aGameDeck->addToDiscDeck(cardsPile->pop());
        } 
        
    }

    void setCurrentPlayer(Player *pCurrent){
        aCurrentPlayer = pCurrent;
    }
    
    void setGameDeck(Deck *pGameDeck){
        aGameDeck = pGameDeck;
    }

    void setPlayerList(List<Player> *pPlayerList){
        aPlayerList = pPlayerList;
    }

    Player* getCurrentPlayer(){
        return aCurrentPlayer;
    }

    Deck* getGameDeck(){
        return aGameDeck;
    }

    List<Player>* getPlayerList(){
        return  aPlayerList;
    }

};

#endif