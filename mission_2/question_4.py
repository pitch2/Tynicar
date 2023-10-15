mdp_q = input("Saisir le mot de passe: ") #question du mdp
mdp = "Padawan" #bon mdp

choix_carte = int(input("1- Sans carte \n2- avec carte gold \n 3- avec carte platinium"))




def voiture():
    marque = input("Marque de la voiture: ")
    modèle = input("Modèle de la voiture: ")
    red = int(input("Saisir 1 si votre voiture est électrique, saisir 2 si votre voiture n'est pas électrique: "))
    if choix_carte == 3:
        red2 = 15/100
    elif choix_carte == 2:
        red2 = 20/100
    elif choix_carte == 2 and red ==1:
        red2 = 30/100
    
    else:
        red2 = 0
        print("Aucune réduction avec votre carte")
        
        
    prix_ht = int(input("Prix HT de l’unité: ")) #demande de l'utilisateur

    prix_TTC = prix_ht + 20/100 #calcul du prix avec taxe de 20 %

    if red == 1:
        red = 5
    else:
        red = 20

    if prix_TTC >= 20000:
        prix_TTC = prix_TTC - (red/100) - red2 #reduction de - 10% 

    print(f"Votre {modèle}, de la marque {marque}, coûte {prix_TTC} €") #affichage


if mdp_q == mdp: #condition du bon mdp
    voiture() #appelle de la fonction quand le mdp est correct
    
    
else:
    print("Mauvais mot de passe")#incorrect
