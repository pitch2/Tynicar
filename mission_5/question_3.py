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

# Appel de la procédure de saisie des accessoires
saisie_accessoires(taille_panier)

# Affichage des éléments des tableaux
afficher_elements_des_tableaux(noms_accessoires, prixHT_accessoires, prixTTC_accessoires)

# Calcul de la somme totale des achats (HT et TTC)
somme_totale_HT = sum(prixHT_accessoires)
somme_totale_TTC = sum(prixTTC_accessoires)
print(f"\nSomme totale des achats (HT) : {somme_totale_HT} €")
print(f"Somme totale des achats (TTC) : {somme_totale_TTC} €")

# Cherche l'accessoire le moins cher (HT)
accessoire_moins_cher_index_HT = prixHT_accessoires.index(min(prixHT_accessoires))
print(f"\nAccessoire le moins cher (HT) : {noms_accessoires[accessoire_moins_cher_index_HT]} - Prix HT : {prixHT_accessoires[accessoire_moins_cher_index_HT]} €")

# Cherche l'accessoire le moins cher (TTC)
accessoire_moins_cher_index_TTC = prixTTC_accessoires.index(min(prixTTC_accessoires))
print(f"Accessoire le moins cher (TTC) : {noms_accessoires[accessoire_moins_cher_index_TTC]} - Prix TTC : {prixTTC_accessoires[accessoire_moins_cher_index_TTC]} €")

# Cherche l'accessoire le plus cher (HT)
accessoire_plus_cher_index_HT = prixHT_accessoires.index(max(prixHT_accessoires))
print(f"Accessoire le plus cher (HT) : {noms_accessoires[accessoire_plus_cher_index_HT]} - Prix HT : {prixHT_accessoires[accessoire_plus_cher_index_HT]} €")

# Cherche l'accessoire le plus cher (TTC)
accessoire_plus_cher_index_TTC = prixTTC_accessoires.index(max(prixTTC_accessoires))
print(f"Accessoire le plus cher (TTC) : {noms_accessoires[accessoire_plus_cher_index_TTC]} - Prix TTC : {prixTTC_accessoires[accessoire_plus_cher_index_TTC]} €")

# Calcul du prix moyen (HT)
prix_moyen_HT = somme_totale_HT / taille_panier
print(f"Prix moyen (HT) : {prix_moyen_HT} €")

# Calcul du prix moyen (TTC)
prix_moyen_TTC = somme_totale_TTC / taille_panier
print(f"Prix moyen (TTC) : {prix_moyen_TTC} €")
