#ifndef LIST_CPP
#define LIST_CPP  

#include "Client.hpp"

template <class T>
class List
{
private:
    T *firstNode;
    int num;

public:
    List (){
        firstNode = nullptr;
        num = 0;
    }

    void insertNode(T *node){
        if (firstNode == nullptr){
            firstNode = node;
        } else {
            T* actual = firstNode;
            while(actual->getNext == nullptr){
                actual = actual->getNext();
            }
            actual->setNext(actual) ;
        }
        num++;
    }

    T* getFirstNode(){
        return firstNode;
    }

    int getNum(){
        return num;
    }

};
#endif

