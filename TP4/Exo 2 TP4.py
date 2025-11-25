nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
somme_notes = 0.0
notes = []
print(f"Nombre étudiant {nombreEtudiants}")
for i in range(nombreEtudiants):
    erreur = False
    while not erreur:
        note = float(input(f"Donner les notes des élèves entre 0 et 20 {i}: "))
        if 0 <= note <= 20 :
            notes.append(note)
            somme_notes += note
            erreur = True
        else :
            print("Veuillez saissir une valeur entre 0 et 20 !")

moyenne = somme_notes / nombreEtudiants
print(f"La moyenne de classe est {moyenne}")

print("Numéro de l'Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
        ecart = notes[i]- moyenne
        print (f"{i} | {notes[i]} | {ecart}")