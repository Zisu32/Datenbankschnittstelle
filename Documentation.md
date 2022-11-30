# Dokumentation
## Inhaltsverzeichnis

### 1. Python User erstellen
create user PythonUser@localhost;
grant all privileges on BichDB to PythonUser@localhost;

### 2. Datenverbindung aufbauen
import mariadb 

conn = mariadb.connect(
    user="PythonUser",
    password="",
    host="localhost",
    database="BuchDB")
cur = conn.cursor()

### 3. Datenbankverbindung prüfen


### 4. Cursor erstellen


 
