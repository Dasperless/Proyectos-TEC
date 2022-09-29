#include "ClientQueue.hpp"
#include "Client.hpp"
#include <iostream>
#include "List.hpp"

using namespace std;

void init(){
    ClientQueue *clientQueue = new ClientQueue();
    Client *newClient = new Client();
    newClient->setName("Dario");
    clientQueue->push(newClient);

    List<ClientQueue> *list = new List<ClientQueue>();
    list->insertNode(clientQueue);

    cout << "nombre:" << list->getFirstNode()->getFirstNode()->getName()<< endl;


}


int main(){
    init();
}

