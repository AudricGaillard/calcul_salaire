# Calcul de salaires de filiales

## Contexte du projet
Sur base d'un fichier JSON généré avec Faker, cet exercice vise à calculer les salaires pour chaque filiale et à afficher les statistiques de ces calculs

## Fonctionnalités du projet
- Calcul du salaire moyen pour chaque filiale
- Affichage du salaire le plus élevé et celui le plus bas
- Ecriture de ces données dans un fichier CSV executable par LibreOffice et/ou Excel
- Interface WEB avec Streamlit

## Configuration
Pour garantir le bon fonctionnement du projet, veuillez installer les dépendances **Faker**, **Streamlit** et **Pandas** dans un environnement virtuel Python.

## Structure des fichiers
- **fonctions** : Dossier où se trouve les fonctions utilisés par le script pour calculer les stats d'entreprise
- **data** : Dossier où trouve les fichiers de données JSON et CSV (dossier vide sur le repository pour raisons de sécurité)
- **main.py** : Script principal à exécuter pour avoir les statistiques et écrire les données dans le CSV
- **interface.py** : Script pour l'interface graphique avec Streamlit (à exécuter dans le terminal avec streamlit run interface.py)