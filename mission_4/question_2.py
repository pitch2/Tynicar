# Initialisation du tableau des noms des accessoires avec des valeurs inventées
noms_accessoires =["4090 X TRIO GAMING RGB","I9 13900XE","WatherCooling NZXT", "Corsair Vengance RGB 35Go DDR5", "Alimentation 1500W Corsair"]
# Initialisation du tableau des prix HT (à remplir avec les saisies de l'utilisateur)
prixHT_accessoires = []

# Demande à l'utilisateur le prix HT de chaque accessoire et stockage dans le tableau des prix
print("Veuillez entrer le prix HT pour chaque accessoire :")
for i in range(len(noms_accessoires)):
    prix_HT = float(input(f"Prix HT pour {noms_accessoires[i]} : "))
    prixHT_accessoires.append(prix_HT)

# Affichage des noms et prixHT des accessoires à l'aide des deux tableaux
print("Noms et prix HT des accessoires :")
for i in range(len(noms_accessoires)):
    print(f"{noms_accessoires[i]} - Prix HT : {prixHT_accessoires[i]}")
