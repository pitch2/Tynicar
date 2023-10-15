#include <iostream>
using namespace std;

int main() {
  // Les questions
  int ht;
  cout << "Entrez le prix HT : ";
  cin >> ht;

  string marque;
  cout << "Entrez la marque de la voiture : ";
  cin >> marque;

  string modele;
  cout << "Entrez le modèle de la voiture : ";
  cin >> modele;

  // Calcul du prix TTC
  float ttc = ht + (0.2 * ht);

  cout << "Le modele " << modele << " de la marque " << marque << " coutera " << ttc << " euros" << endl;

  return 0;
}
