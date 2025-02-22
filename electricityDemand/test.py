from datetime import datetime

def heures_ecoulees(date1, date2):
    # Conversion des chaînes de caractères en objets datetime
    dt1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    dt2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    
    # Calcul de la différence entre les deux dates
    delta = dt2 - dt1
    
    # Extraction du nombre d'heures écoulées
    heures = delta.total_seconds() / 3600
    
    return heures

# Exemple d'utilisation
#date1 = '2024-02-21 14:00:00'
#date2 = '2025-02-21 23:00:00'

#print(f'Heures écoulées : {heures_ecoulees(date1, date2)} heures')

