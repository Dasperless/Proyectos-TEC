#ifndef CONTROLLER_HPP
#define CONTROLLER_HPP

#include <iostream>
#include <cstdlib>
#include "Counter.hpp"
#include "Client.hpp"
#include "List.hpp"
class Controller
{
private:
    List<Counter> *counters;
    Queue< Queue<Client> > queues;
public:
    Controller(int numCounters, int transLimit){
        for(int i = 0; i != numCounters; i++){
            Counter *newCounter = new Counter(i,transLimit);
            counters->insertNode(newCounter);
        }
    }
    void startQueue(string name, int numClient, int priority ){

    }

    void deleteQueue(){
        
    }

    void addClient(){
        printQueues();
    }

    void attendTrans(){

    }

    void nextClient(){
        
    }

    void visualizeQueue(){

    }

    void visualizeSpecQ(){
        
    }

    void visualizeCounter(){

    }

    void printQueues(){
        Queue<Queue<Client>> actual = queues.getFirstNode();
        while(actual.getNext() != nullptr){
            cout << actual.getNum() << endl;
            actual = actual.getNext();
        }
    }

    void printClientQ(){
        Queue<Queue<Client>> actual = queues.getFirstNode();
        while(actual.getNext() != nullptr){
            cout << actual.getNext << endl;
            actual->printClients();
            actual = actual.getNext();
        }        
    }

    void menu(){
        bool start = true;
        while(start){
            cout << "########### Menu ###########" << endl;
            cout << "[1] Iniciar cola de espera" << endl;
            cout << "[2] Eliminar cola de espera" << endl;
            cout << "[3] Agregar cliente a una cola" << endl;
            cout << "[4] Atender trasaccion" << endl;
            cout << "[5] Pasar al siguiente cliente" << endl;
            cout << "[6] Visualizar colas de espera" << endl;
            cout << "[7] Visualizar cola de espera especifica" << endl;
            cout << "[8] Visualizar escritorios" << endl;
            cout << "[9] Salir" << endl;
            cout << "[#]>";

            int key;
            switch (key)
            {
            case 1:
                startQueue();
                break;
            case 2:
                deleteQueue();
                break;
            case 3:
                addClient();
                break;
            case 4:
                attendTrans();
                break;
            case 5:
                nextClient();
                break;
            case 6:
                visualizeQueue();
                break;
            case 7:
                visualizeSpecQ();
                break;
            case 8:
                visualizeCounter();
                break;
            case 9:
                start = false;
                break;
            default:
                break;
            }
        }

    }    
};
#endif