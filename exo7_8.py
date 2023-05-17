"""
f=open('fichier.txt', 'w')
f.write("'chaud'==>'hot'\n'froid'==>'cold'\n'tempéré'==>moderate\n'glacial==>'icy''\n'brûlant'==>'ardent'")
f.close()
"""


mots_français=["chaud","froid","tempéré","glacial","brûlant"]
mots_anglais=["hot","cold","moderate","icy","ardent "]

with open('fichier.txt', 'w', encoding="utf-8") as fichier:
    for mot_fr, mot_en in zip(mots_français, mots_anglais):
        ligne=f"{mot_fr}\t\t\t\t{mot_en}\n"
        fichier.write(ligne)