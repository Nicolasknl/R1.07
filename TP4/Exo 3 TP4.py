v1=[]
v2=[]
nMax = 4
produit_scalaire = 0
n=int(input("Donnez la taille effective des vecteurs :"))
while n < 1 or n > nMax :
    print("Veuillez saisir une valeur adapter !")
    n = int(input("Donnez la taille effective des vecteurs :"))

print("Saisie la valeur du premier veceteur :")
for i in range(n):
    val = int(input(f"v1[{i}] = "))
    v1.append(val)

print("Saisie la valeur du second veceteur :")
for i in range(n):
    val = int(input(f"v2[{i}] = "))
    v2.append(val)

for i in range(n):
    produit_scalaire += v1[i] * v2[i]

print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}")






