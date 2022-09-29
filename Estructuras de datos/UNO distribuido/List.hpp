#ifndef LIST_HPP
#define LIST_HPP
#include <iostream>

using namespace std;

template <class T>
class List
{
private:
    T *firstNode;
    T *lastNode;
    int num;

public:
    List (){
        firstNode = nullptr;
        lastNode = nullptr;
        num = 0;
    }

    void insertCircular(T *node){
        T* prevQueue = lastNode;
        T* currentQueue = firstNode;
        num++;
        if(firstNode == nullptr){
            firstNode = node;
            lastNode = node;
        } else {
            node->setNext(firstNode);
            lastNode->setNext(node);
        }
        
    }

    void insertNode(T *node){
        if (firstNode == nullptr){
            firstNode = node;
        } else {
            node->setNext(firstNode);
        }
        firstNode = node;
        num++;
    }

    T* getFirstNode(){
        return firstNode;
    }

    int getNum(){
        return num;
    }

    T* deleteNode(int index){
        T* deletedNote;
        T* prevNode = nullptr;
        T* actual = firstNode;
        if (index > num || index < 0){
            cout <<  "No existe el elemento que desea eliminar" << endl;
            return nullptr;
        } else if (firstNode == nullptr) {
            cout << "La lista esta vacia" << endl;
            return nullptr;
        } else {
            for(int i = 0; i < index; i++){
                prevNode = actual;
                actual = actual->getNext();
            }
            if (prevNode == nullptr){
                T* temp = firstNode;
                temp->setNext(nullptr);
                deletedNote = temp;
                firstNode = firstNode->getNext();
            } else if (actual->getNext() == lastNode){
                actual->setNext(nullptr);
                lastNode = actual;
            } else if(actual == firstNode){
                firstNode = nullptr;
            } else {
                deletedNote = actual->getNext();
                T* nextNode = deletedNote->getNext();
                actual->setNext(nextNode);

            }
        }
        return deletedNote;
        num--;
    }

    T* getLastNode(){
        return lastNode;
    }

    T* pop(){
        T* temp = firstNode;
        firstNode = firstNode->getNext();
        
        temp->setNext(nullptr);
        num--;
        return temp;
    }
};
#endif