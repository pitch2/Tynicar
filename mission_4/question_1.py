# Initialisation des tableaux pour noms et prixHT des accessoires   
tableau_accessoires =["4090 X TRIO GAMING RGB","I9 13900XE","WatherCooling NZXT", "Corsair Vengance RGB 35Go DDR5", "Alimentation 1500W Corsair"] #-> str
tableau_prix_HT = [1900, 800, 346, 180, 600] # -> int


# Affichage des noms et prixHT des accessoires à l'aide des deux tableaux
for n in range(len(tableau_accessoires)):
    print(f"{tableau_accessoires[n]} à {tableau_prix_HT[n]}€")
