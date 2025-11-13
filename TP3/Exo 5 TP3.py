# Velo.py

# Saisie des heures
heure_debut = int(input("Donnez l’heure de début de la location (un entier) : "))
heure_fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

# Vérifications des erreurs
if not (0 <= heure_debut <= 24) or not (0 <= heure_fin <= 24):
    print("Les heures doivent être comprises entre 0 et 24 !")
elif heure_debut == heure_fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
elif heure_debut > heure_fin:
    print("Attention ! le début de la location est après la fin ...")
else:
    # Comptage des heures selon le tarif
    heures_tarif1 = 0  # 1€/h (0-7 et 17-24)
    heures_tarif2 = 0  # 2€/h (7-17)

    for h in range(heure_debut, heure_fin):
        if 0 <= h < 7 or 17 <= h < 24:
            heures_tarif1 += 1
        else:  # 7 <= h < 17
            heures_tarif2 += 1

    # Calcul du total
    total = heures_tarif1 * 1.0 + heures_tarif2 * 2.0

    # Affichage détaillé
    print("Vous avez loué votre vélo pendant")
    if heures_tarif1 > 0:
        print(f"{heures_tarif1} heure(s) au tarif horaire de 1.0 euro(s)")
    if heures_tarif2 > 0:
        print(f"{heures_tarif2} heure(s) au tarif horaire de 2.0 euro(s)")
    print(f"Le montant total à payer est de {total} euro(s)")
