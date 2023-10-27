# Demander à l'utilisateur la taille du panier
taille_panier = int(input("Veuillez entrer la taille du panier :"))

# Initialisation des tableaux pour noms, prixHT et prixTTC des accessoires du panier
noms_accessoires = []
prixHT_accessoires = []
prixTTC_accessoires = []

# Fonction pour calculer le prix TTC en fonction du prix HT (TVA à 20%)
def calculer_prixTTC(prixHT):
    tva = 0.20  # Taux de TVA (20%)
    prixTTC = prixHT * (1 + tva)  # Calcul du prix TTC
    return prixTTC

# Saisie des noms et prix HT pour chaque accessoire et calcul du prix TTC
def saisie_accessoires(taille_panier):
    print("Veuillez entrer les noms et prix HT pour chaque accessoire :")
    for i in range(taille_panier):
        nom = input(f"Nom de l'accessoire {i + 1} : ")
        prix_HT = float(input(f"Prix HT pour {nom} : "))
        noms_accessoires.append(nom)
        prixHT_accessoires.append(prix_HT)
        prixTTC_accessoires.append(calculer_prixTTC(prix_HT))

# Nouvelle procédure pour afficher les éléments des tableaux
def afficher_elements_des_tableaux(noms, prixHT, prixTTC):
    print("Noms, prix HT, et prix TTC des accessoires du panier :")
    for i in range(len(noms)):
        print(f"{noms[i]} - Prix HT : {prixHT[i]} € - Prix TTC : {prixTTC[i]} €")

# Fonction pour calculer la moyenne des prix HT
def calculer_moyenne_prixHT(prixHT):
    if len(prixHT) == 0:
        return 0.0  # En cas de liste vide, la moyenne est 0
    else:
        return sum(prixHT) / len(prixHT)

# Fonction pour trouver le prix HT minimal
def trouver_prixHT_minimal(prixHT):
    if len(prixHT) == 0:
        return None  # En cas de liste vide, il n'y a pas de prix minimal
    else:
        return min(prixHT)

# Fonction pour trouver le prix HT maximal
def trouver_prixHT_maximal(prixHT):
    if len(prixHT) == 0:
        return None  # En cas de liste vide, il n'y a pas de prix maximal
    else:
        return max(prixHT)

# Appel de la procédure de saisie des accessoires
saisie_accessoires(taille_panier)

# Affichage des éléments des tableaux
afficher_elements_des_tableaux(noms_accessoires, prixHT_accessoires, prixTTC_accessoires)

# Calcul de la somme totale des achats (HT et TTC)
somme_totale_HT = sum(prixHT_accessoires)
somme_totale_TTC = sum(prixTTC_accessoires)
print(f"\nSomme totale des achats (HT) : {somme_totale_HT} €")
print(f"Somme totale des achats (TTC) : {somme_totale_TTC} €")

# Cherche l'accessoire le moins cher (HT et TTC)
accessoire_moins_cher_index_HT = prixHT_accessoires.index(min(prixHT_accessoires))
accessoire_moins_cher_index_TTC = prixTTC_accessoires.index(min(prixTTC_accessoires))
print(f"\nAccessoire le moins cher (HT) : {noms_accessoires[accessoire_moins_cher_index_HT]} - Prix HT : {prixHT_accessoires[accessoire_moins_cher_index_HT]} €")
print(f"Accessoire le moins cher (TTC) : {noms_accessoires[accessoire_moins_cher_index_TTC]} - Prix TTC : {prixTTC_accessoires[accessoire_moins_cher_index_TTC]} €")

# Cherche l'accessoire le plus cher (HT et TTC)
accessoire_plus_cher_index_HT = prixHT_accessoires.index(max(prixHT_accessoires))
accessoire_plus_cher_index_TTC = prixTTC_accessoires.index(max(prixTTC_accessoires))
print(f"Accessoire le plus cher (HT) : {noms_accessoires[accessoire_plus_cher_index_HT]} - Prix HT : {prixHT_accessoires[accessoire_plus_cher_index_HT]} €")
print(f"Accessoire le plus cher (TTC) : {noms_accessoires[accessoire_plus_cher_index_TTC]} - Prix TTC : {prixTTC_accessoires[accessoire_plus_cher_index_TTC]} €")

# Calcul du prix moyen (HT et TTC)
prix_moyen_HT = calculer_moyenne_prixHT(prixHT_accessoires)
prix_moyen_TTC = calculer_moyenne_prixHT(prixTTC_accessoires)
print(f"Prix moyen (HT) : {prix_moyen_HT} €")
print(f"Prix moyen (TTC) : {prix_moyen_TTC} €")

# Calcul du prix HT minimal et maximal
prixHT_minimal = trouver_prixHT_minimal(prixHT_accessoires)
prixHT_maximal = trouver_prixHT_maximal(prixHT_accessoires)

if prixHT_minimal is not None:
    print(f"Prix HT minimal : {prixHT_minimal} €")
else:
    print("Aucun accessoire dans le panier.")

if prixHT_maximal is not None:
    print(f"Prix HT maximal : {prixHT_maximal} €")
else:
    print("Aucun accessoire dans le panier.")
