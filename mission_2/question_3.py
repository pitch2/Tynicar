mdp_q = input("Saisir le mot de passe: ") #question du mdp
mdp = "Padawan" #bon mdp


def voiture():
    marque = input("Marque de la voiture: ")
    modèle = input("Modèle de la voiture: ")
    red = int(input("Saisir 1 si votre voiture est électrique, saisir 2 si votre voiture n'est pas électrique: "))
    prix_ht = int(input("Prix HT de l’unité: ")) #deamande de l'utilisateur

    prix_TTC = prix_ht + 20/100 #calcul du prix avec taxe de 20 %

    if red == 1:
        red = 5
    else:
        red = 20

    if prix_TTC >= 20000:
        prix_TTC = prix_TTC - (red/100) #reduction de - 10%

    print(f"Votre {modèle}, de la marque {marque}, coûte {prix_TTC} €") #affichage


if mdp_q == mdp: #condition du bon mdp
    voiture() #appelle de la fonction quand le mdp est correct
    
    
else:
    print("Mauvais mot de passe")#incorrect
