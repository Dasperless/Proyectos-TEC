#include "Controller.hpp"

using namespace std;

int main(int argc, char *argv[]){
    if (argc != 3){
        cout << "[Error]: Los parametros son incorrectos"<< endl;
        cout << "Debe indicar:" << endl;
        cout << "\t 1) LA CANTIDAD DE ESCRITORIOS." << endl;
        cout << "\t 2) LA CANTIDAD DE TRAMITES LIMITE POR PERSONA." << endl;
    } else { 
        int numCounters = atoi(argv[1]);
        int transLimit = atoi(argv[2]);         
        if(numCounters == 0 || transLimit == 0) {
            cout << "[Error]: Se insertado un caracter" << endl;
            cout << "debe añadir dos valores numéricos" << endl;
            cout << "\t 1) LA CANTIDAD DE ESCRITORIOS." << endl;
            cout << "\t 2) LA CANTIDAD DE TRAMITES LIMITE POR PERSONA."<< endl;        
        } else {
            Controller *controller = new Controller(numCounters,transLimit);
            cout << "[Escritorios]: " << numCounters << endl;
            cout << "[Limite Tranacciones]: " << transLimit << endl;       
            
        }
    }
}
