#SQLITE CREATION DE LA TABLE

import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

curseur.execute("""CREATE TABLE artiste (
artiste_id INTEGER NOT NULL PRIMARY KEY,
nom VARCHAR);""")

# sql_table_artiste = 
curseur.execute("""CREATE TABLE albums (
                album_id INTEGER NOT NULL PRIMARY KEY,
                artiste_id INTEGER REFERENCES artiste,
                titre varchar,
                annee_sortie INTEGER);
                """)

curseur.execute("INSERT INTO artiste(nom) VALUES (\"Michael Jackson\");")    
mj_id = curseur.lastrowid            
curseur.execute('INSERT INTO artiste(nom) VALUES ("Celine Dion");')                
cd_id = curseur.lastrowid
curseur.execute("INSERT INTO albums(artiste_id, titre, annee_sortie) VALUES ("+str(mj_id)+", \"Thriller\", 1982);")                
curseur.execute('INSERT INTO albums(artiste_id, titre, annee_sortie) VALUES ('+str(cd_id)+', "Falling into you", 1996);')                
curseur.execute('INSERT INTO albums(artiste_id, titre, annee_sortie) VALUES ('+str(cd_id)+', "Let\'s talk about Love", 1997);')                
           

# con.execute(sql_table_artiste)
# curseur.execute(sql_others)

connexion.commit()
connexion.close()

