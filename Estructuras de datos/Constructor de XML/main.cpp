#include "MakeFile.hpp"
#include "XMLNode.hpp"
#include "XMLDocument.hpp"

#include <iostream>
using namespace std;
int pow(int a, int b)
{
    int result = 1;
    for (int i = 0; i < b; i++)
        result*=a;
    return result;
}
int main()
{
    XMLDocument *xmlDocument = new XMLDocument();
    xmlDocument->root("semestre");
    char n[5];
    int id = xmlDocument->getSelected()->getID();
    for (int i = 0; i < 4; i++)
    {
        n[i] = id /pow(10,3-i)%10 + '0';
        
        if (i == 5)
            n[i] = '0';
    }
    cout << n << endl;
}