#ifndef CLIENT_CPP
#define CLIENT_CPP

#include <iostream>
#include <string>
 
using namespace std;

class Client
{
private:
    Client *next;
    int id;
    string name;
    string transType;
    int numTransaction;
 
public:
    Client(){
        next = nullptr;
        id = 0;
        name = "";
        transType = "";
        numTransaction = 0;
    }

    Client(int id, string name, string transType, int numTransaction){
        next = nullptr;
        setName(name);
        setTransType(transType);
        setNumTrans(numTransaction);
        setId(id);
    }

    void setId(int id){
        this->id = id;
    }

    void setName(string name){
        this->name = name;
    }

    void setTransType(string transType){
        this->transType = transType;
    }

    void setNumTrans(int numTransaction){
        this->numTransaction = numTransaction;
    }

    void setNext(Client *next){
        this->next = next;
    }

    Client* getNext(){
        return next;
    }

    int getId(){
        return id;
    }

    string getName(){
        return name;
    }

    string getTransType(){
        return transType;
    }

    int getNumTrans(){
        return numTransaction;
    }
};
#endif