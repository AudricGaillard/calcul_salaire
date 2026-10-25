# Fichier principal pour la partie obligatoire

import json
import sys
import csv
from fonctions.salary_functions import calculate_monthly, company_stats
# Importations des modules suivants :

# json --> pour lire le fichier JSON et récupérer les données
# sys --> module permettant d'accéder à des variables utilisées par l'interpréteur Python
# csv --> pour écrire des données dans un fichier CSV, utilisable avec Excel

# from fonctions.salary_functions import calculate_monthly, company_stats 
# --> (Voir salary_functions.py dans le dossier fonctions) on importe nos fonctions définies pour
# calculer les données

try:
    # Le try va tenter d'ouvrir le fichier JSON indiqué par le chemin relatif

    with open("data/faker.json", "r", encoding="utf-8") as fichier_json:
        # "r" --> signifiant read, on lit seulement le fichier JSON
        # encoding="utf-8" --> pour gérer les accents
        # CHEMIN A CHANGER SI ON TESTE D'AUTRES FICHIER JSON!!!!!

        donnees_json=json.load(fichier_json)
        # json.load va convertir le fichier JSON en un objet Python

        max_global = 0
        min_global = sys.float_info.max
        moy_global = 0
        # Ces variables vont servir à la gestion des statistiques globales de toutes les entreprises
        # plus tard dans le code

        # min_global = sys.float_info.max --> sys.float_info est un objet fourni par le module sys.
        # Il contient des informations sur les floats utilisé par l'interpréteur Python.
        # Le .max va récupérer le plus grand float possible dans Python pour l'assigner à la variable

        #moy_global et max_global restent à 0 pour le moment

        company_dictionnary={}
        # Ce dictionnaire servira plus tard dans le code pour écrire les statistiques des entreprises
        # dans le CSV

        csv_path="data/data.csv"
        # Un string contenant le chemin relatif vers le fichier CSV, afin de ne pas retaper tout
        # à chaque fois
        
        # A NOTER!!! Les parties du code concernant l'écriture dans le fichier CSV vont être
        # écrites à plusieurs reprises, afin bien de découper le processus étape par étape,
        # plutôt que de tout faire en une seul fois
        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            # "w" --> write, on va écrire dans le fichier indiqué

            # NOTES IMPORTANTES :
            # - Si le fichier n'existe pas, Python va le créer automatiquement vers le chemin
            # indiqué avec le nom du fichier indiqué également, contrairement au mode read ("r")
            # pour le JSON qui a besoin que le fichier existe avant la lecture (pas besoin
            # également d'un try/except pour vérifier l'existence du fichier)

            # - En mode "w" (write), Python va écraser les données déjà écrite dans le fichier
            # à l'écriture de nouvelles données.

            writer = csv.writer(csv_file, delimiter=";")
            # On initialise la classe writer qui va écrire les données dans le CSV sur 
            # Le paramètre delimiter=";" va servir à séparer les données par le caractère indiqué
            # lorsqu'on va écrire dans le fichier, ce qui va permettre aux logiciels comme Excel
            # de détecter comment les données sont séparées à l'ouverture du fichier

            # writerow sert à écrire une ligne dans le CSV, Excel va alors l'interpréter comme une
            # valeur dans une cellule
            # Les virgules indiquent que les valeurs sont séparées dans plusieurs cellules dans
            # la ligne

            writer.writerow(["Stats des employés"])

            # Entêtes de colonnes "Nom", "Job", "Salaire mensuel" et "Entreprise" pour séparer
            # les différentes données
            writer.writerow(["Nom", "Job", "Salaire mensuel", "Entreprise"])
            

        for entreprise, employees in donnees_json.items():
        # On parcours la liste des données de l'objet JSON
        # Pour chaque entreprise et sa liste d'employés
            print(f"\nEntreprise : {entreprise}\n")
            employees_tuples=[]
            # Cette liste va contenir des tuples, avec à l'intérieur les infos des employés de
            # l'entreprise actuelle dans la boucle. Elle est remise à zéro lorsqu'on passe à
            # l'entreprise suivante

            for employee in employees:
            # Pour chaque employé dans la liste d'employés de l'entreprise

                new_infos=(employee['name'], employee['job'], calculate_monthly(employee))
                # On crée un tuple avec les infos suivante :
                # - employee['name'] : le nom de l'employé(e)
                # - employee['name'] : le nom de son poste
                # - calculate_monthly(employee) : son salaire mensuel calculé avec la fonction
                # calculate_monthly() (voir le fichier salary_functions.py)

                employees_tuples.append(new_infos)
                # On ajoute le tuple à la liste des employés de l'entreprise actuel dans la boucle

            sorted_list=sorted(employees_tuples, key=lambda employee:employee[2], reverse=True)
            # Une fois la liste des employés parcouru avec la boucle, on créer une liste trié à
            # partir de la liste des tuples grâce à la fonction sorted.

            # key=lambda employee:employee[2] --> on utilise l'indice du salaire dans chaque tuple
            # en tant que clef pour le tri (la fonction va se baser sur le salaire pour trier la liste)
            
            # Exemple avec deux tuples :
            # - ("Helen", "Manager", 2345.00)
            # - ("Nicolas", "Testeur", 5432.00)

            # La fonction va comparer les valeurs 2345.00 et 5432.00 pour ensuite mettre ces tuples
            # dans l'ordre

            #reverse=True --> ordonne la liste de manière décroissante

            for element in sorted_list:
            # Pour chaque élement de la liste ordonnée

                print(f"{element[0]:<17}| {element[1]:<45}| Salaire mensuel : {element[2]:.2f} €")
                # On affiche les infos de l'élément :
                # - element[0] : le nom de l'employé(e)
                # - element[1] : le nom de son poste
                # - element[2] : son salaire mensuel

                # :<17 --> sert à ajouter un certain nombre d'espace après la chaîne de caractère
                # :.2f --> arrondi un chiffre à virgule à 2 décimales

                # Ecriture d'une nouvelle ligne d'infos dans le CSV
                with open(csv_path, "a", newline="", encoding="utf-8") as csv_file:
                    # ATTENTION!!! Nous utilisons ici le mode "a" pour add (ajouter).
                    # Comme mentionné plus haut, nous écrasons les données existantes dans
                    # le CSV si on utilise le mode "w" (write)

                    writer = csv.writer(csv_file, delimiter=";")
                    writer.writerow([element[0], element[1], f"{element[2]:.2f}", entreprise])
                    #entreprise --> le nom de l'entreprise actuelle dans la boucle
            
            print("\n=================================================================")
            print(f"\nStatistics de l'entreprise {entreprise} :\n")
            stats=company_stats(sorted_list)
            # On appelle company_stats avec notre liste ordonnée pour avoir :
            # - le salaire moyen
            # - le salaire le plus élevé
            # - le salaire le plus bas
            # stats sera égal à un tuple reprenant ces trois résulats dans l'ordre

            # Voir salary_functions.py pour savoir comment sont calculés les stats
            

            company_dictionnary[entreprise]=[stats[0], stats[1], stats[2]]
            # Rappel : ce dictionnaire sera utilisé pour écrire les stats des entreprises
            # dans le CSV. On ajoute une nouvelle clé (le nom de l'entreprise) avec comme
            # valeur une liste des trois résultats obtenus avec company_stats

            print(f"Salaire moyen : {stats[0]:.2f}€")
            print(f"Salaire le plus élevé : {stats[1]:.2f}€")
            print(f"Salaire le plus bas : {stats[2]:.2f}€")
            print("\n=================================================================")
            # Affichage des valeurs de company_stats

            # Modification des valeurs pour les statistiques globales

            moy_global+=stats[0]
            # Ajout du salaire moyen au total global

            if max_global<stats[1]:
                # Rappel : max_global vaut 0 au départ
                # On vérifie à chaque fois si cette variable est plus petite que le salaire
                # le plus élevé de l'entreprise actuel dans la boucle
                # Si c'est le cas, on affecte la variable

                max_global=stats[1]
            if min_global>stats[2]:
                # Rappel n°2 : min_global vaut 1.7976931348623157e+308 (le plus gros float possible)
                # en Python au départ
                # On vérifie à chaque fois si cette variable est plus grande que le salaire
                # le plus bas de l'entreprise actuel dans la boucle
                # Si c'est le cas, on affecte la variable

                min_global=stats[2]

        print(f"\nStatistiques globales :\n")
        print(f"Moyenne des salaires des entreprises : {(moy_global/len(donnees_json)):.2f}€")
        print(f"Salaire le plus élevé : {max_global:.2f}€")
        print(f"Salaire le plus bas : {min_global:.2f}€")
        print("\n=================================================================")
        # Affichage des statistiques globals
        # len(donnees_json) --> le nombre de clefs dans le JSON (= le nombre d'entreprise)
        # La moyenne globale est divisé par le nombre d'entreprises

        # Ecriture des statistiques des entreprises et des statistiques globales dans le CSV
        with open(csv_path, "a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerow([])
            # Ligne vide pour espacer le tableau

            writer.writerow(["Stats des entreprises"])
            writer.writerow(["Nom", "Salaire moyen", "Salaire le plus élevé", "Salaire le plus bas"])
            # Même exemple qu'au dessus pour les entêtes de colonnes
            for companies, statistics in company_dictionnary.items():
                #companies --> les clés (nom des entreprises)
                #statistics --> les résultats obtenu avec la fonction company_stats
                writer.writerow([companies, f"{statistics[0]:.2f}", f"{statistics[1]:.2f}", f"{statistics[2]:.2f}"])

            writer.writerow([])
            # Ecriture des statistiques globales
            writer.writerow(["Statistiques globales"])
            writer.writerow(["Salaire moyen", "Salaire le plus élevé", "Salaire le plus bas"])
            writer.writerow([f"{moy_global/len(donnees_json):.2f}", f"{max_global:.2f}", f"{min_global:.2f}"])
    
except FileNotFoundError:
    # Si le try au début du code ne trouve pas le JSON, affiche une erreur
    print("Erreur : fichier introuvable")