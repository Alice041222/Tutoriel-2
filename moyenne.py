"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.markdown import Markdown
from rich.console import Console


def moyenne(valeurs):
    # docstrings en markdown
    """
    # Calcule la moyenne des valeurs.

    **Paramètres**
    - `valeurs` : valeurs dont on veut calculer la moyenne

    **Retour**
    - la moyenne des valeurs

    **Exceptions**
    - `ValueError` : si la liste est vide

    ---
    """
    if len(valeurs)==0:
        return 'ValueError'
    else :
        somme=0
        for i in range(len(valeurs)):
            somme+=valeurs[i]
    return somme/len(valeurs)   

print(moyenne([10, 20, 15]))
