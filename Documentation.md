# Dokumentation
## Inhaltsverzeichnis

### 1. Python User erstellen
create user PythonUser@localhost;
grant all privileges on BuchDB.Buch to PythonUser@localhost;
ACHTUNG: zusätzlich muss grant select on BuchDB.Buch to PythonUser@localhost gegeben werden

### 2. Datenverbindung aufbauen
import mysql.connector as mariadb
import sys 

conn = mariadb.connect(
    user="PythonUser",
    password="",
    host="localhost",
    database="BuchDB")

### 3. Datenbankverbindung prüfen
except mariadb.Error as e:
    print(f"Verbindungsfehler: {e}")
    sys.exit(1)

### 4. Cursor erstellen
cur = conn.cursor()

### 5. User Input erstellt in Terminal
print("Wählen Sie aus deutsch, englisch, französisch, spanisch oder griechisch")
language_wish = input()

### 6. Get-Funktion schreiben
def get_data(language_wish):
    try:
        statement = f"select Titel,Sprache from BuchDB.Buch where Sprache like \'{language_wish}\';"
        cur.execute(statement)
        for(Titel, Sprache) in cur:
            print(f"Titel: {Titel}, Sprache: {Sprache}")
    except mariadb.Error as ex:
        print(f"Keine Buch in der Sprache verfügbar: {ex}")

### 7. Funktion ausführen und Verbindung schließen
get_data(language_wish)
conn.close()

### 8. Debugging im Termnial mit pdb
import pdb;pdb.set_trace()
