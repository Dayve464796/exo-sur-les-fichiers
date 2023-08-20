
#exercice1

#elements de la liste

liste_elements = ["mangue", "pomme", "papaye", "banane", "coco"]

    # Demander à l'utilisateur de saisir le nom du fichier
nom_fichier = input("Entrez le nom du fichier  ")

# Ajouter chaque élément de la liste dans le fichier

with open(f"{nom_fichier}.txt", "w") as fichier:
        for element in liste_elements:
            fichier.write(element.strip() + "\n")
    
print(f"Contenu de la liste enregistré dans le fichier {nom_fichier}.txt")
