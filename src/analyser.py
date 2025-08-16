import os


def analyser(chemin):
    """Analyse le code à l'emplacement spécifié et retourne les résultats de l'analyse."""
    resultats = []
    if not os.path.exists(chemin):
        return [f"Le chemin '{chemin}' n'existe pas."]
    
    # Logique d'analyse simple pour prouver le concept
    for filename in os.listdir(chemin):
        if filename.endswith('.py'):
            with open(os.path.join(chemin, filename), 'r') as f:
                code = f.read()
                if 'print ' in code:
                    resultats.append(f"'{filename}' utilise une syntaxe obsolète.")
                if 'import' in code and 'module' in code:
                    resultats.append(f"'{filename}' contient un module importé obsolète.")
    
    return resultats
