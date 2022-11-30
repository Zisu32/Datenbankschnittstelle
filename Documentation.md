# Dokumentation
## Inhaltsverzeichnis

### 1. Python User erstellen
create user PythonUser@localhost;
grant all privileges on BuchDB to PythonUser@localhost;

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


 
