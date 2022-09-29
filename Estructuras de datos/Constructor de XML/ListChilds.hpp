#ifndef LISTCHILDS_HPP
#define LISTCHILDS_HPP

#include "XMLNode.hpp"
class ListChilds{
    private:
        int cuantity;
        XMLNode *first;

    public:
        ListChilds(){
            cuantity=0;
            first=nullptr;
        }

        void insert(XMLNode *node){
            if(first==nullptr)
                first=node;
            else{
                XMLNode *temp=first;
                while(temp->getNext()!=nullptr)
                    temp=temp->getNext();
                temp->setNext(node);
            }
            cuantity++;
        }


        XMLNode *getNodeIndex(int index){
            XMLNode *current=first;
            for(int i=0;i<index;i++){
                current=current->getNext();
            }
            return current;
        }

        XMLNode *interpolationSearch(int ID){
            int lowerIndex = 0;
            int biggerIndex = cuantity-1;
            int middle = 0;
            while((ID>=getNodeIndex(lowerIndex)->getID()) && (lowerIndex<=biggerIndex) && (ID<=getNodeIndex(biggerIndex)->getID())){
                middle=lowerIndex+(((double)(biggerIndex-lowerIndex)/(getNodeIndex(biggerIndex)->getID()-getNodeIndex(lowerIndex)->getID()))*(ID-getNodeIndex(lowerIndex)->getID()));
                if(getNodeIndex(middle)->getID()==ID){
                    return getNodeIndex(middle);
                }
                else if(getNodeIndex(middle)->getID()<ID){
                    lowerIndex=middle+1;
                }
                else biggerIndex=middle-1;
            }
            return nullptr;
        }

        XMLNode *getfirst(){
            return first;
        }

        int getCuantity(){
            return cuantity;
        }
};
#endif