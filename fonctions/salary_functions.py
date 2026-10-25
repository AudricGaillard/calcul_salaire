def calculate_monthly(employee_infos:dict)->float:
    """
    Calcule le salaire mensuel d'un(e) employé(e) selon ses heures de travail et en tenant compte
    des heures supplémentaire

    Args:
        employee_infos (dict): Le dictionnaire contenant les informations de l'employé(e)

    Returns:
        float: Le salaire mensuel de l'employé(e)

    """

    taux = employee_infos['hourly_rate']
    # Le taux auquel l'employé(e) est payé(e)
    nb_heures_travail = employee_infos['weekly_hours_worked']
    # Le nombre d'heures de travail effectuées
    heures_contrat = employee_infos['contract_hours']
    # Le nombre d'heures à effectuer sur le contrat

    
    if nb_heures_travail<heures_contrat:
    # On vérifie si l'employé(e) a effectué moins d'heures de travail que prévu sur le contrat
        total = taux*nb_heures_travail
        # Si c'est le cas, on multiplie son taux par ses heures de travail effectuées
    else:
        # Si au contraire, l'employé(e) a effectué plus d'heures de travail que prévu

        total = taux*heures_contrat
        # On multiplie d'abord son taux par ses heures de travail prévu sur le contrat

        heures_sup = nb_heures_travail-heures_contrat
        # On calcule les heures supplémentaires
        # Exemple : si nb_heures_travail = 47 et heures_contrat = 40 :
        # --> l'employé(e) a effectué 7 heures supplémentaires de travail

        total+=heures_sup*(taux*1.5)
        # On rajoute au total initial son taux rémunéré à 1,5 fois le taux normal multipliés par les
        # heures supplémentaires

    total*=4
    # On multiplie par 4 le total pour ensuite avoir le salaire mensuel
    return total


def company_stats(company_employees:list)->tuple:
    """
    Prend une liste contenant des tuples représentant tous les employés d'une entreprise et leurs
    infos, et renvoie le salaire moyen, ainsi que le salaire le plus élevé et salaire le plus bas.

    Args:
        company_employees (list): La liste des employés
    
    Returns:
        tuple: Un tuple avec dans l'ordre \: la moyenne, le salaire le plus haut puis celui le plus bas
    """
    salaries=[employee[2] for employee in company_employees]
    # Ici, seul les salaires des employés nous intéresses (il s'agit du 3ème élement d'un tuple)
    # On crée une nouvelle liste en reprenant le 3ème élement de chaque tuple dans la liste passée
    # en paramètres
    # Exemple : ("Helen", "Chef de projet", 2345.00) --> 2345.00 est ajouté à la liste

    return (sum(salaries)/len(salaries)), max(salaries), min(salaries)
    # sum --> additionne tous les élements de la liste des salaires (on divise ensuite par le
    # nombre de salaire pour faire la moyenne)
    # max --> récupère l'élement plus élevé de la liste
    # min --> récupère l'élement plus bas de la liste