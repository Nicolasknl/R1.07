n=int(input("Entrer une valeur :"))
if n < 0:
    print("La factorielle n'est pas définie pour les nombres négatifs.")
else:

    print("Choisissez le type de boucle :")
    print("1 - Boucle FOR")
    print("2 - Boucle WHILE")
    choix = input("Entrez 1 ou 2 : ")

    if choix == "1":

        fact = 1
        print(f"0! = 1")
        for i in range(1, n + 1):
            fact *= i
            print(f"{i}! = {fact}")

    elif choix == "2":

        fact = 1
        i = 1
        print(f"0! = 1")
        while i <= n:
            fact *= i
            print(f"{i}! = {fact}")
            i += 1
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")