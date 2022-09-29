#ifndef NODE_HPP
#define NODE_HPP
class Node
{
private:
    char *aData;
    Node *aLeft;
    Node *aRight;
    int aBf;

public:
    Node(char *pData)
    {
        setData(pData);
        aLeft = nullptr;
        aRight = nullptr;
        aBf = 0;
    }

    //Sección de métodos

    int max(int a, int b)
    {
        if (a > b)
            return a;
        return b;
    }

    int height(Node *pNode)
    {
        if (pNode == nullptr)
            return 0;
        int leftHeigh = height(pNode->getLeft());
        int rightHeight = height(pNode->getRight());

        return 1 + max(leftHeigh, rightHeight);
    }
    void balanceFactor()
    {
        int leftBalance = height(aLeft);
        int rightBalance = height(aRight);

        setBalanceFactor(leftBalance - rightBalance);
    }

    //Sección de setters.
    void setData(char *pData) { aData = pData; }
    void setRight(Node *pNode) { aRight = pNode; }
    void setBalanceFactor(int pBf) { aBf = pBf; }
    void setLeft(Node *pNode) { aLeft = pNode; }

    //Sección de getters.
    Node *getLeft() { return aLeft; }
    Node *getRight() { return aRight; }
    int getBalanceFactor() { return aBf; }
    char *getData() { return aData; }
};
#endif