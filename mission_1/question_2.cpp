#include <iostream>
using namespace std;

int main() {
  int ht = 10;   /*On défini le prix HT*/
  int ttc = ht + (0.2*ht); /*On calcul le prix TTC*/
  cout << "Le prix TTC est " << ttc << endl;
  return 0;
}
