#ifndef NODEATTRIBUTE_HPP
#define NODEATTRUBUTE_HPP

#include <cstdlib>
class NodeAttribute{
    private:
        char *key;
        char *value;
        NodeAttribute *next;
    public:
        NodeAttribute(char *key,char *value){
            this->key=key;
            this->value=value;
            next=nullptr;
        }

        char *getKey(){
            return key;
        }

        char *getValue(){
            return value;
        }

        NodeAttribute *getNext(){
            return next;
        }

        void setNext(NodeAttribute *newNext){
            next=newNext;
        }

        void setKey(char *newKey){
            key=NULL;
            key=newKey;
        }

        void setValue(char *newValue){
            value=NULL;
            value=newValue;
        }
};
#endif