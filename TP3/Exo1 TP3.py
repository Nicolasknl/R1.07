cpt2=0
cpt1=0
cpt = 0
for i in range(10):
    while True:
            valeur = float(input(f"Entrez la valeur n°{i+1} (entre 0 et 20) : "))
            if 0 <= valeur <= 20:
                break
            else:
                print(" Valeur hors intervalle ! Veuillez entrer un nombre entre 0 et 20.")
    if valeur < 10:
        cpt += 1
    elif valeur == 10 or valeur < 15:
        cpt1 += 1
    elif valeur >= 15 :
        cpt2 += 1
print("Nombre de valeur égale à 10 et inférieur a 15 :",cpt1)
print("Nombre de valeur inférieur à 10 :",cpt)
print("Nombre de valeur égale à 15 ou supérieur :",cpt2)








while True:
    N = int(input("Entrez un entier naturel (100 pour quitter) : "))
        N == 100:
        print("Fin du programme.")
        break
        somme = 0
    for i in range(N + 1):
        somme += i

    print("La somme des entiers de 0 à ",N," est : ",somme)

X = float(input("Entreze X > 1"))
while X <= 1:
    X = float(input("Erreur entre un nombre > 1"))
N = 0
somme = 0
while somme + (N+ 1) <= X:
    N += 1
    somme += N
print("Le plus grand N est :",N)
print("La somme est :",somme)