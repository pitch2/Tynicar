#include <iostream>
using namespace std;

int main() {
  int ht;
  cout << "Entrez le prix HT : ";
  cin >> ht;

  cout << "Prix HT : " << ht << endl;

  // Calcul du prix TTC
  float ttc = ht + (0.2 * ht);

  cout << "Prix TTC : " << ttc << endl;

  return 0;
}
