devise=input("Choisir entre 'E'(pour euro) et 'S'(pour dollar):\t")
montant=float(input("Entrer le montant:\t"))
#1euro=1.09 dollars
TAUX=1.09
if devise=='E':
    print(montant*TAUX)
elif devise=="S":
    print(montant/TAUX)
else:
    print("ERREUR!Nous faisons seulement la conversion euro<==>dollar")