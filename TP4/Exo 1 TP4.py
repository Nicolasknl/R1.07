valeur=float(input("Vous cherchez la table de multiplication de quel nombre ?"))
resultat=[]

for i in range(10):
        produit = round(valeur * i, 1)
        resultat.append(produit)

for i in range(10):
    print(f"{valeur} * {i} = {resultat[i]}")




