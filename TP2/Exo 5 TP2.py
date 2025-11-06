nombre=int(input("Entrez un nombre entier :"))
if nombre==0:
    print("Le nombre est zéro ( et il est paire")
if nombre > 0 :
    nombre=nombre%2
    if nombre==0:
        print("Le nombre est positif et paire")
    else:
        print("Le nombre est positif et impaire")
if nombre < 0:
    nombre = nombre % 2
    if nombre == 0:
        print("Le nombre est négatif et paire")
    else:
        print("Le nombre est négatif et impaire")

