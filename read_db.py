# LECTURE BD

import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

curseur.execute('SELECT * FROM artiste')
artistes = curseur.fetchall()
print(artistes)
for artiste in artistes:
    print(artiste[1])

# ou encore 
for artiste in curseur.execute('SELECT * FROM artiste'):
    print(artiste)
#connexion.commit()# pas besoin lecture
print("Join...")
albums_cd = curseur.execute('SELECT nom,titre FROM albums a JOIN artiste ar ON a.artiste_id=ar.artiste_id AND ar.nom="Celine Dion"').fetchall()
print(albums_cd)
connexion.close()

