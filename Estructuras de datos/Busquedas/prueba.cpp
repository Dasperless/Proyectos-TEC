#include "list.hpp"
#include "node.hpp"
#include <iostream>

using namespace std;
int main(){
    list *firstList = new list();
    list *SecondList = new list();
    firstList->randomNumList(5,true);
    SecondList->randomNumList(5,false);
    //firstList->printNodes();
    SecondList->quickSort();
    SecondList->printNodes();
}