import random
nombre = random.randint(0,100)
cpt= 0
while True :
        a = int(input("Entrer une valeur entre 0 et 100 :"))
        cpt = cpt +1
        if a < nombre :
            print("Votre valeur est trop petite !")
        elif a > nombre :
            print("Votre valeur est est trop grande !")

        else :
                print("Vous avez trouvé la valeur en",cpt,"tour")
                break
