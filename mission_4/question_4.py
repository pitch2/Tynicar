# Demander à l'utilisateur la taille du panier
taille_panier = int(input("Veuillez entrer la taille du panier : "))

# Initialisation des tableaux pour noms et prixHT des accessoires du panier
noms_accessoires = []
prixHT_accessoires = []

# Saisie des noms et prix HT pour chaque accessoire et stockage dans les tableaux
print("Veuillez entrer les noms et prix HT pour chaque accessoire :")
for i in range(taille_panier):
    nom = input(f"Nom de l'accessoire {i + 1} : ")
    prix_HT = float(input(f"Prix HT pour {nom} : "))
    noms_accessoires.append(nom)
    prixHT_accessoires.append(prix_HT)

#
# Affichage des noms et prixHT des accessoires du panier
print("Noms et prix HT des accessoires du panier :")
for i in range(taille_panier):
    print(f"{noms_accessoires[i]} - Prix HT : {prixHT_accessoires[i]}")

# Calcul de la somme totale des achats
somme_totale = sum(prixHT_accessoires)
print(f"\nSomme totale des achats : {somme_totale} €")


# Cherche l'accessoire le moins cher
accessoire_moins_cher_index = prixHT_accessoires.index(min(prixHT_accessoires))
print(f"\nAccessoire le moins cher : {noms_accessoires[accessoire_moins_cher_index]} - Prix HT : {prixHT_accessoires[accessoire_moins_cher_index]} €")

# Cherche l'accessoire le plus cher
accessoire_plus_cher_index = prixHT_accessoires.index(max(prixHT_accessoires))
print(f"Accessoire le plus cher : {noms_accessoires[accessoire_plus_cher_index]} - Prix HT : {prixHT_accessoires[accessoire_plus_cher_index]} €")

# Calcul du prix moyen
prix_moyen = somme_totale / taille_panier
print(f"Prix moyen : {prix_moyen} €")
