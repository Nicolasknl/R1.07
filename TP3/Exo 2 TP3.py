"""import time
n = int(input("Entrer un nombre entier positif :"))
for i in range(n,-1, -1):
    print(i)
    time.sleep(1)
    while n < 0 :
     n=int(input("Erreur ! entrer un nombre positif"))
print("Fin du compte a rebours"""""


import time
n = int(input("Entrez un nombre entier positif : "))

if n < 0:
    print("Veuillez entrer un nombre positif.")
else:
    print("Compte à rebours  :")
    while n >= 0:
        print(n)
        time.sleep(1)
        n -= 1








