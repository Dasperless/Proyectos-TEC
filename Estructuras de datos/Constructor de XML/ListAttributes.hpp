#ifndef LISTATTRIBUTES_HPP
#define LISTATTRIBUTES_HPP

#include "NodeAttribute.hpp"
class ListAttributes{
    private:
        int cuantity;
        NodeAttribute *first;

    public:
        ListAttributes(){
            cuantity=0;
            
            first=nullptr;
        }

        void insertFirst(NodeAttribute *node){
            if(first==nullptr){
                first=node;
            }
            else{
                node->setNext(first);
                first=node;
            }
            cuantity++;

        }

        void insertLast(NodeAttribute *node){
            if(first==nullptr)
                first=node;
            else{
                NodeAttribute *temp=first;
                while(temp->getNext()!=nullptr)
                    temp=temp->getNext();
                temp->setNext(node);
            }
            cuantity++;

        }

        bool compare(char *value1, char *value2){
            if (sizeof(value1) != sizeof(value2))
                return false;
            for (int i = 0; i < sizeof(value1); i++)
                if (value1[i] != value2[i])
                    return false;
            return true;
        }

        NodeAttribute *search(char *key){
            NodeAttribute *current = first;
            while(current!=nullptr){
                if(current->getKey()==key)
                    return current;
                current=current->getNext();
            }
            return nullptr;
        }

        NodeAttribute *getfirst(){
            return first;
        }

        int getCuantity(){
            return cuantity;
        }

        bool del(char *key){
            NodeAttribute *deleted=search(key);
            NodeAttribute *previus = first;
            while(previus->getNext()!=deleted)
                previus=previus->getNext();
            previus->setNext(deleted->getNext());
            deleted->setNext(nullptr);
            cuantity--;
        }
};
#endif