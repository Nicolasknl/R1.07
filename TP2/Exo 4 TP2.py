BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvives=int(input("Entrez le nombre de personn(s) conviées à la fondue :"))
nouvelleQuantite_fromage= 800*nbConvives / BASE
nouvelleQuantite_eau= 2*nbConvives / BASE
nouvelleQuantite_ail= 2*nbConvives / BASE
nouvelleQuantite_pain= 400*nbConvives / BASE
print("Pour faire une fondue fribourgeoise pour 3 personnes,il vous faut :")
print("-",nouvelleQuantite_fromage,"gr de fromage")
print("-",nouvelleQuantite_eau,"dl d'eau")
print("-",nouvelleQuantite_ail,"gousse(s) d'ail")
print("-",nouvelleQuantite_pain,"gr de pain")