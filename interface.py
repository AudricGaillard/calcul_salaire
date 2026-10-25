# Fichier pour l'interface graphique

import streamlit as st
import pandas as pd
import json
import sys
from fonctions.salary_functions import calculate_monthly, company_stats

# Streamlit va servir à faire les composants de l'interface graphique
# Pandas va nous permettre de manipuler les données

# Le code en dessous est simillaire au main, avec quelques changements
try:
    with open("data/faker.json", "r", encoding="utf-8") as fichier_json:
        donnees_json=json.load(fichier_json)
        max_global = 0
        min_global = sys.float_info.max
        moy_global = 0

        employees_data=[]
        # Tableau de données des employés
        companies_data=[]
        # Tableau de données des entreprises

        for entreprise, employees in donnees_json.items():
            current_company_stats=[]
            # Cette liste va enregistrer les infos de l'entreprise actuelle dans la boucle
            # Elle est remise à zéro lorsqu'on passe à l'entreprise suivant
            for employee in employees:
                employees_data.append((employee['name'], employee['job'], calculate_monthly(employee), entreprise))
                # Ajout de données au tableau de données des employés
                current_company_stats.append((employee['name'], employee['job'], calculate_monthly(employee), entreprise))
                # Ajout de données à la liste d'infos de l'entreprise actuelle
            
            stats=company_stats(current_company_stats)
            companies_data.append((entreprise, stats[0], stats[1], stats[2]))
            # On récupère les statistiques de l'entreprise actuelle de la boucle avec
            # company_stats, pour ensuite ajouter les données au tableau de données des entreprises
            moy_global+=stats[0]
            if max_global<stats[1]:
                max_global=stats[1]
            if min_global>stats[2]:
                min_global=stats[2]

        st.title("Statistiques des employés")
        # Affiche un titre
        employee_df = pd.DataFrame(employees_data, columns=['Nom', 'Job', 'Salaire mensuel', 'Entreprise'])
        # On créer un Dataframe avec pandas à partir d'une liste de données en indiquant les colonnes
        st.dataframe(employee_df) 
        # Streamlit affichera un tableau de données à partir du Dataframe

        st.title("Statistiques des entreprise")
        company_df = pd.DataFrame(companies_data, columns=['Nom', 'Salaire moyen', 'Salaire le plus élevé', 'Salaire le plus bas'])
        st.dataframe(company_df) 
        # Même chose pour le tableau de données des entreprises

        st.title("Statistiques globales")
        global_df = pd.DataFrame([((moy_global/len(companies_data)), max_global, min_global)], columns=['Salaire moyen', 'Salaire le plus élevé', 'Salaire le plus bas'])
        st.dataframe(global_df)
        # Pour les stats globaux
    
except FileNotFoundError:
    print("Erreur : fichier introuvable")
    
