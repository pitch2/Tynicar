#exo 4
marque = input("Marque de la voiture: ")
modèle = input("Modèle de la voiture: ")
prix_ht = int(input("Prix HT de l’unité: ")) #deamande de l'utilisateur

prix_TTC = prix_ht + 20/100 #calcul du prix avec taxe de 20 %

print(f"Votre{modèle}, de la marque {marque}, coûte {prix_TTC} €")

