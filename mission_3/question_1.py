while True:
    marque = input("Marque de la voiture: ")
    modèle = input("Modèle de la voiture: ")
    prix_ht = int(input("Prix HT de l’unité: "))  # Demande de l'utilisateur

    prix_TTC = prix_ht + 20 / 100  # Calcul du prix avec taxe de 20 %

    if prix_TTC >= 20000:
        prix_TTC = prix_TTC - (10 / 100)  # Réduction de - 10%

    print(f"Votre {modèle}, de la marque {marque}, coûte {prix_TTC} €")  # Affichage

    choix = input("Voulez-vous calculer le prix TTC d'un autre produit ? (1 pour continuer, 0 pour quitter): ")
    if choix == '0':
        print("Merci et au revoir !")
        break
    elif choix != '1':
        print("Choix invalide. Fin du programme.")
        break
