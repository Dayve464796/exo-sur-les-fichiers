
#exercice2

# Demander à l'utilisateur de saisir le nom du fichier d'origine
nom_fichier_origine = input("Entrez le nom du fichier d'origine  ")

# Lire le contenu du fichier d'origine

with open(f"{nom_fichier_origine}.txt", "r") as fichier_origine:
            contenu_origine = fichier_origine.read()

 # Créer le nom du fichier de destination
nom_fichier_destination = f"copie-{nom_fichier_origine}"


    # Convertir le contenu en majuscules
contenu_majuscules = contenu_origine.upper()

    # Écrire le contenu en majuscules dans le fichier de destination
with open(f"{nom_fichier_destination}.txt", "w") as fichier_destination:
        fichier_destination.write(contenu_majuscules)

print(f"Contenu du fichier d'origine copié en majuscules dans {nom_fichier_destination}.txt")
