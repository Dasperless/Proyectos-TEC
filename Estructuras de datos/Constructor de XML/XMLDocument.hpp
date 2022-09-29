#ifndef XMLDOCUMENT_HPP
#define	XMLDOCUMENT_HPP

#include <iostream>
#include "XMLNode.hpp"
#include "MakeFile.hpp"
class XMLDocument {
    private:
	//Funtion operating modes
	const int ADD = 100;	// Mode addition, adds the value to the beginning of the set as allowed by the specific function (with or without repetition)
	const int OVR = 200;	// Mode overwrite, if it already exists, replaces the value, if not, just add it.
	const int APD = 300;	// Mode append, appends the value to the end of the set as allowed by the specific function (with or without repetition)
	const int DEL = 400;	// Mode delete, if the value exists, it is deleted instead
	//Node content location type
	const int BEG = 10;		// Content is displayed before children of node, just after the opening tag.
	const int END = 20;		// Content is displayed after children of node, just before the closing tag. 
	XMLNode *selected;
	XMLNode *apRoot;
	int ID;
	/*============== Private functions ==============*/

	// char *makePreview(XMLNode *start){	
	// 	char *preview = NULL;
	// 	if(start->getBalanced())
	// 		return makePreviewBalanced(start);
	// 	if(start->getChild()==nullptr){
	// 		preview->insert(start->getID()); //preguntar a dario
	// 		return preview;
	// 	}	
	// 	char tab='	';
	// 	char space= '\n';
	// 	else return makePreviewAux(start,start->getChild(),preview,tab,space,0);
	// }

	// char *makePreviewAux(XMLNode *start,XMLNode *currentChild,char *preview,char tab,char space,int tabs){
	// 	preview->insert(start->getID());
	// 	preview->insert(space);
	// 	tabs++;
	// 	while(currentChild!=nullptr){
	// 		tabs=1;
	// 		preview = addToPreview(currentChild,preview,tab,space,tabs);
	// 		currentChild = currentChild ->getNext();
	// 	}
	// 	return preview;
	// }

	// char *addToPreview(XMLNode *current,char *preview,char tab,char space,int tabs){
	// 	if(current->getChild()==nullptr || current->getLeft()==nullptr || current->getRight()==nullptr){
	// 		for(int i=0;i<tabs;i++)
	// 			preview->insert(tab);
	// 		preview->insert(current->getID);
	// 		preview->insert(space);
	// 	}
	// 	else{
	// 		tabs++;
	// 		XMLNode *temp=current->getChild();
	// 		while(temp!=nullptr){
	// 			if(temp->getBalanced()){
	// 				if(temp->getLeft()!=nullptr)
	// 					addToPreview(temp->getLeft(),preview,tab,space,tabs++);
	// 				if(temp->getRight()!=nullptr)
	// 					addToPreview(temp->getRight(),preview,tab,space,tabs++);

	// 			}
	// 			else addToPreview(temp->getNext(),preview,tab,space,tabs);
	// 		}
	// 	}
	// }


    void insertBalanced(XMLNode *parent, XMLNode *node){
		XMLNode *grandParent =  getPrevius(nullptr,apRoot,selected->getID());
        node->setBalanced();
		insertBalanced(grandParent,parent,node);
    }

	void insertBalanced(XMLNode *grandParent,XMLNode *parent,XMLNode *node){
		bool balancear = true;
        if (node->getID() >= parent->getID())//Si el nodo es mayor o igual que el padre
            if (parent->getRight() == nullptr)
                parent->setRight(node);
            else
                insertBalanced(parent, parent->getRight(),node);
        else if (node->getID() < parent->getID()) //Si el nodo es menor que el padre
            if (parent->getLeft() == nullptr)
                parent->setLeft(node);
            else
                insertBalanced(parent, parent->getLeft(),node);
        else //Se debe eliminar para que inserte repetidos
            balancear = false; // ya existía

        if (balancear)
        {
            parent->balanceFactor();
            if (parent->getBalanceFactor() > 1 || parent->getBalanceFactor() < -1)
            {
                if (node->getID() >= parent->getID()) //Si el nodo es mayor que el padre
                {
                    // el primer movimiento fue hacia la derecha
                    if (node->getID() >= parent->getRight()->getID()) //Si el hijo derecho del padre es mayor que el nodo
                        //El segundo movimiento fue a la derecha
                        simpleLeftRotation(grandParent, parent);
                    else
                        // El segundo movimiento fue hacia la izquierda
                        doubleLeftRotation(grandParent, parent);
                }
                else
                {
                    // el primer movimiento fue hacia la derecha
                    if (node->getID() >= parent->getRight()->getID()) //Si el nodo es mayor que el hijo derecho del padre
                        simpleRightRotation(grandParent, parent);
                    //El segundo movimiento fue a la derecha
                    else
                        // El segundo movimiento fue hacia la izquierda
                        doubleRightRotation(grandParent, parent);
                }
            }
        }
	}

    void simpleRightRotation(XMLNode *grandParent, XMLNode *parent)
    {
        XMLNode *temp = parent->getLeft();
        XMLNode *right = temp->getRight();
        parent->setLeft(right);
        temp->setRight(parent);
        if (parent == apRoot)
            apRoot = temp;
        if (parent == selected) // Si el padre es igual a a la raiz
            selected = temp;
        else if (grandParent != nullptr)
            grandParent->setLeft(temp);
    }

    void simpleLeftRotation(XMLNode *grandParent, XMLNode *parent)
    {
        XMLNode *temp = parent->getRight();
        XMLNode *left = temp->getLeft();
        parent->setRight(left);
        temp->setLeft(parent);
        if (parent == apRoot)
            apRoot = temp;
        if (parent == selected)
            selected = temp;
        else if (grandParent != nullptr)
            grandParent->setRight(temp);
    }

    void doubleRightRotation(XMLNode *grandParent, XMLNode *parent)
    {
        XMLNode *left = parent->getLeft();      //B
        XMLNode *right = left->getRight();      //E
        XMLNode *tempLeft = right->getLeft();   //F
        XMLNode *tempRight = right->getRight(); //G

        left->setRight(tempLeft);
        right->setLeft(left);
        parent->setLeft(tempRight);
        right->setRight(parent);
        if (parent == apRoot)
            apRoot = right;
        if (parent == selected)
            selected = right;
        else if (grandParent != nullptr)
            grandParent->setLeft(right);
    }

    void doubleLeftRotation(XMLNode *grandParent, XMLNode *parent)
    {
        XMLNode *right = parent->getRight();   //C
        XMLNode *left = right->getLeft();      //D
        XMLNode *tempRight = left->getRight(); //G
        XMLNode *tempLeft = left->getLeft();   //F

        right->setLeft(tempRight);
        left->setRight(right);
        parent->setRight(tempLeft);
        left->setLeft(parent);
        if (parent == apRoot)
            apRoot = left;
        if (parent == selected)
            selected = left;
        else if (grandParent != nullptr)
            grandParent->setRight(left);
    }	


	XMLNode *search(XMLNode *node,int value){
		if(node->getBalanced())
			return nullptr;//balancedSearch();
		else{
			if(node->getID()==value)
				return node;
			if(node->getChild()!=nullptr){
				XMLNode *temp = node->getChild();
				while(temp!=nullptr){
					XMLNode *r = search(temp,value);
					if (r != nullptr)
						return r;
					temp=temp->getNext();
				}
			}
			return nullptr;
		}
	}

	XMLNode *getPrevius(XMLNode *prev,XMLNode *node,int value){
		if(node->getID()==value)
			return prev;
		if(node->getChild()!=nullptr){
			XMLNode *temp = node->getChild();
			while(temp!=nullptr){
				XMLNode *r = getPrevius(node,temp,value);
				if (r != nullptr)
					return r;
				node=temp;
				temp=temp->getNext();
			}
		}
		return nullptr;
	}
	
    public:
	XMLDocument(){
		selected=nullptr;
		ID=1000;
	}

	/*XMLNode *getPrevius(XMLNode *prev,XMLNode *node,int value){
		if(node->getID()==value)
			return prev;
		if(node->getChild()!=nullptr){
			XMLNode *temp = node->getChild();
			while(temp!=nullptr){
				XMLNode *r = getPrevius(node,temp,value);
				if (r != nullptr)
					return r;
				node=temp;
				temp=temp->getNext();
			}
		}
		return nullptr;
	}*/

	void root(char *name){
		XMLNode *node= new XMLNode(name,ID);
		if(selected==nullptr){
			apRoot=node;
			selected=apRoot;
		}
		else{
			XMLNode *temp=apRoot;
			apRoot=node;
			apRoot->insertChild(temp);
			selected=apRoot;
		}
		ID++;
    }

	void  select(int id){
		selected=search(apRoot,id);
    }

	int child(char *name){
		XMLNode *node = new XMLNode(name,ID);
		if(selected->getBalanced())
			insertBalanced(selected,node);
		else selected->insertChild(node);
		int IDtemp=ID;
		ID++;
		return IDtemp;
    }

	bool  editattribute(char *key, char *value, int mode){
		if(mode==ADD){
			NodeAttribute *newAttribute=new NodeAttribute(key,value);
			selected->getAttributes()->insertFirst(newAttribute);
			return true;
		}
		else if(mode==APD){
			NodeAttribute *newAttribute=new NodeAttribute(key,value);
			selected->getAttributes()->insertLast(newAttribute);
			return true;
		}
		else if(mode==OVR){
			//busqueda del atribute con la llave que entra, y sobreescribe el valor
			ListAttributes *attributes=selected->getAttributes();
			NodeAttribute *attribute=attributes->search(key);
			if(attribute==nullptr){
				NodeAttribute *newAttribute=new NodeAttribute(key,value);
				selected->getAttributes()->insertFirst(newAttribute);
			}
			else attribute->setValue(value);
			return true;
		}
		else if(mode==DEL){
			ListAttributes *attributes=selected->getAttributes();
			if(attributes->search(key)!=nullptr){
				attributes->del(key);
				return true;
			}
			else return false;
		}
		else return false;
    }

	bool  editcontent(char *content, int mode){
		selected->setContent(content);
    }

	XMLNode *getSelected(){
		return selected;
	}

	bool  switchcontentposition(){
		if(selected->getContentLocation()==BEG)
			return selected->switchContentLocation(END);
		else return selected->switchContentLocation(BEG);
    }

	bool  setbalanced(int id){
		if(search(apRoot,id)!=nullptr){
			XMLNode *balancedNode =	search(apRoot, id);
			if(balancedNode->getChild()==nullptr){
				balancedNode->setBalanced();
				return true;
			}
			else return false;
		}
		else return false;
    }

	bool  Delete(int id){
		if(search(apRoot,id)!=nullptr){
			if(search(apRoot,id)==apRoot){
				XMLNode *temp = apRoot;
				XMLNode *tempChild =apRoot->getChild();
				apRoot=tempChild;
				apRoot->insertChild(apRoot->getNext());
				apRoot->setNext(nullptr);
				temp->setNext(nullptr);
				selected=apRoot;
				return true;
			}
			else{
				XMLNode *deleted = search(apRoot,id);
				XMLNode *prev = getPrevius(nullptr,apRoot,id);
				if(!deleted->getAvlRoot()){
					if(prev==apRoot){
						prev->setChild(deleted->getNext());
						return true;	
					}
					prev->setNext(deleted->getNext());
					deleted->setNext(nullptr);
					return true;
				}else return false;
			}
		}
		else return false;
    }

	bool  save(char *filename){
        if(apRoot == nullptr)
            return false;
        MakeFile *document = new MakeFile();
        document->newFile(apRoot,filename);
    }
	// /*char**/void visualize(){
	// 	printInfix(apRoot);
    // }

	/*char* visualize(int id){

    }

	char* preview(){

    }
*/
};
#endif