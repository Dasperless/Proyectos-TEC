#ifndef QUEUE_CPP
#define QUEUE_CPP  

#include "Client.hpp"

class ClientQueue
{
private:
    ClientQueue *next;
    Client *firstNode;
    int num;

public:
    ClientQueue(){
        next = nullptr;
        firstNode = nullptr;
        num = 0;
    }

    void push(Client *nuevoNodo){
        if (firstNode == nullptr){
          firstNode = nuevoNodo;
        } else {
            Client *actual = firstNode;
            while (actual->getNext() != nullptr)
            {
                actual = actual->getNext();
            }
            actual->setNext(nuevoNodo);
        }
        num++;
    }

    Client* pop(){
        if(firstNode != nullptr){
            return firstNode;
        } else {
            firstNode = firstNode->getNext();
            return firstNode;
        }num--;
    }

    Client* pop(int id){
        Client *searched = firstNode;
        while(searched != nullptr){
            if (searched->getId() == id){
                return searched;
            } else {
                searched = searched->getNext();
            }
        }
        num--;
        return searched;
    }

    ClientQueue* getNext(){
        return next;
    }

    Client* getFirstNode(){
        return firstNode;
    } 

    int getNum(){
        return num;
    }

    void setNext(ClientQueue *next){
        this->next = next;
    }

    void printClients(){
        Client *actual = firstNode;
        while(actual != nullptr){
            actual = actual->getNext();
            cout << actual->getName() << endl;
        }

    }
};
#endif

