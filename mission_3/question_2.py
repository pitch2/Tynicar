n = int(input("Saisissez le nombre de produits à traiter : "))

for i in range(n):
    print(f"\nProduit {i + 1}:")
    marque = input("Marque du produit : ")
    modèle = input("Modèle du produit : ")
    prix_ht = float(input("Prix HT de l'unité : "))  # Demande de l'utilisateur

    prix_TTC = prix_ht + (prix_ht * 20 / 100)  # Calcul du prix avec une taxe de 20 %

    if prix_TTC >= 20000:
        prix_TTC = prix_TTC - (prix_TTC * 10 / 100)  # Réduction de - 10%

    print(f"Le {modèle} de la marque {marque} coûte {prix_TTC:.2f} €")  # Affichage

print("\nMerci de votre utilisation. Au revoir !")
