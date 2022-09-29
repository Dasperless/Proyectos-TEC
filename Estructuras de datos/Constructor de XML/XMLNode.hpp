#ifndef XMLNODE_HPP
#define XMLNODE_HPP

#include "ListAttributes.hpp"
class XMLNode
{
private:
    ListAttributes *attributes;
    int id;
    char *name;
    char *content;
    int contentLocation;
    bool balanced;
    bool avlRoot;
    XMLNode *right;
    XMLNode *left;
    XMLNode *next;
    XMLNode *child;
    int height;
    int fe;

public:
    XMLNode(char *name, int id)
    {
        this->id = id;
        this->name = name;
        content = NULL;
        contentLocation = 0;
        attributes = new ListAttributes();
        balanced = false;
        avlRoot = false;
        right = nullptr;
        left = nullptr;
        child = nullptr;
        next = nullptr;
        height = 0;
    }

    void insertChild(XMLNode *node)
    {
        XMLNode *current = child;
        if (current == nullptr)
        {
            child = node;
            return;
        }
        while (current->getNext() != nullptr)
            current = current->getNext();
        current->setNext(node);
    }

    int max(int a, int b)
    {
        if (a > b)
            return a;
        return b;
    }

    int subTreeHeight(XMLNode *pNode)
    {
        if (pNode == nullptr)
            return 0;
        int leftHeigh = subTreeHeight(pNode->getLeft());
        int rightHeight = subTreeHeight(pNode->getRight());

        return 1 + max(leftHeigh, rightHeight);
    }
    void balanceFactor()
    {
        int leftBalance = subTreeHeight(left);
        int rightBalance = subTreeHeight(right);
        setBalanceFactor(leftBalance - rightBalance);
    }

    void setChild(XMLNode *newChild)
    {
        child->setNext(nullptr);
        child = newChild;
    }

    XMLNode *getChild()
    {
        return child;
    }

    void setAvlRoot(bool state)
    {
        avlRoot = state;
    }

    bool getAvlRoot()
    {
        return avlRoot;
    }

    ListAttributes *getAttributes()
    {
        return attributes;
    }

    char *getName()
    {
        return name;
    }

    char *getContent()
    {
        return content;
    }

    void setContent(char *newContent)
    {
        content = newContent;
    }

    int getID()
    {
        return id;
    }

    bool getBalanced()
    {
        return balanced;
    }

    void setBalanced()
    {
        balanced = true;
    }

    XMLNode *getRight()
    {
        return right;
    }

    XMLNode *getLeft()
    {
        return left;
    }

    XMLNode *getNext()
    {
        return next;
    }

    void setRight(XMLNode *newRight)
    {
        right = newRight;
    }

    void setLeft(XMLNode *newLeft)
    {
        left = newLeft;
    }

    void setNext(XMLNode *newNext)
    {
        next = newNext;
    }

    int getHeight()
    {
        return height;
    }

    void setBalanceFactor(int pBf)
    {
        fe = pBf;
    }

    int getBalanceFactor()
    {
        return fe;
    }

    bool switchContentLocation(int mode)
    {
        if (content == NULL)
            return false;
        else
            contentLocation = mode;
        return true;
    }

    int getContentLocation()
    {
        return contentLocation;
    }
};
#endif