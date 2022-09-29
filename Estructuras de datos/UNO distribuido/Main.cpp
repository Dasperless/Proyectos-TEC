#include "Uno.hpp"
#include "List.hpp"
#include <iostream>
int main(){
    Player *dario = new Player("Dario");
    Player *daniel = new Player("Dario");
    List<Player> *playerList = new List<Player>();
    playerList->insertCircular(dario);
    playerList->insertCircular(daniel);

    Uno *newUno = new Uno(playerList);
    newUno->startGame();
}