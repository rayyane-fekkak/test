# Créez une liste pour stocker les tâches
tasks = []

# Fonction pour ajouter une tâche
def ajouter_tache():
    tache = input("Nom de la tâche : ")
    tasks.append(tache)

# Fonction pour voir les tâches
def voir_la_tache():
    print("Liste des tâches :", tasks)

while True:
    print("Options :")
    print("1. Ajouter une tâche")
    print("2. Voir les tâches")

    choix = input("Choisissez une option (ou appuyez sur Entrée pour quitter) : ")

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        voir_la_tache()
    else:
        break

# Afficher la liste des tâches à la fin
print("Liste des tâches :", tasks)
