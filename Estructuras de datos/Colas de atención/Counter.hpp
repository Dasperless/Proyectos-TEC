#ifndef Counter_CPP
#define Counter_CPP

#include <iostream>
#include <string>
#include "Queue.hpp"
 
using namespace std;

class Counter
{
private:
    Counter *next;
    int id;
    int procLimit;
    Queue <Client> clientQueue;

 
public: 
    Counter(int id, int procLimit){
        setId(id);
        setProcLimit(procLimit);
    }

    void setId(int id){
        this->id = id;
    }

    void setProcLimit(int procLimit){
        this->procLimit = procLimit;
    }

    void setNext(Counter *next){
        this->next = next;
    }

    void addClient(Client *newClient ){
        clientQueue.push(newClient);
    }

    Client* attendCostumer(){ // Se debe realizar las operaciones de matrices
        return clientQueue.pop();
    }

    Counter* getNext(){
        return next;
    }

    int getProcLimit(){
        return procLimit;
    }

    int getId(){
        return id;
    }


};
#endif