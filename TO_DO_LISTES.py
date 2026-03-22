print("=="*30)
print("Welcome Visitors !")


option1 = print("1: Ajouter une tâche")
option2 = print("2: Voir les tâches")
option3 = print("3: Supprimer une tâche")
option4 = print("4: Quitter")

while True:
    choice = input("Veuillez choisir une option (1-4) : ")

    if choice == "1":
        tâche = input("Entrez la tâche à ajouter : ")
        with open("tâches.txt", "a") as file:
            file.write(tâche + "\n")
        print("Tâche ajoutée avec succès !")
    elif choice == "2":
        print("voici les taches :")
        with open("tâches.txt", "r") as file:
            tâches = file.readlines()
            for tâche in tâches:
                print("- " + tâche.strip())
    elif choice == "3":
        tâche_à_supprimer = input("Entrez la tâche à supprimer : ")
        with open("tâches.txt", "w") as file:
            for tâche in tâches:
                if tâche.strip() != tâche_à_supprimer:
                    file.write(tâche)
        print("Tâche supprimée avec succès !")
    elif choice == "4":
        print("Merci d'avoir utilisé mon application de gestion de tâches.")
        break

print("=="*30)