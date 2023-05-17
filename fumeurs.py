age=int(input("Entrer votre age:\t"))
hasSmoked=bool(input("Fumez-vous?:(Répondez: True si vous fumez et False sinon)\t"))
isDiabetic=bool(input("Etes-vous diabétique?:(Répondez: True si vous fumez et False sinon)\t"))

#Critères choisis
#age>=50 et fumeur et diabétique  ===> risque élevé
#age>=50 et fumeur et diabétique  ===> risque moyen
#age>=50 et non fumeur et diabétique ===>faible risque
 

if age>=50 and hasSmoked==True and isDiabetic==True:
    print("ALERT!Les risques de cancer de poumons sont ELEVES!\nVous devriez arreter de fumer et réduire votre consommation de sucre.\nFaites attention à vous!")
elif age>=50 and hasSmoked==True and isDiabetic==False:
    print("Attention! Vous avez moyennement des risques de cancer de poumons!")
elif (age>=50 and hasSmoked==False and isDiabetic==False):
    print("Le cancer de poumons? Les risques sont très faibles!")
else:
    print("Aucun risque de cancer.Félicitation! Continuez à prendre soin de votre santé!")
    