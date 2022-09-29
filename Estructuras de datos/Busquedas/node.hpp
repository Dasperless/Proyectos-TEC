#ifndef NODE_HPP
#define NODE_HPP
class node
{
private:
    node *apNext;
    int aValue;

public:
    node(){}
    node(int value)
    {
        apNext = nullptr;
        aValue = value;
    }

    // Setters y getters
    void setNext(node *next) { apNext = next; }
    void setValue(int value) { aValue = value; }
    node *getNext() { return apNext; }
    int getValue() { return aValue; }
};
#endif