#!/usr/bin/python 
import mysql.connector as mariadb 
import sys

#Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="PythonUser",
        password="",
        host="localhost",
        database="BuchDB")
except mariadb.Error as e:
    print(f"Verbindungsfehler: {e}")
    sys.exit(1)

#Get Cursor
cur = conn.cursor() 

#User Input 
print("Wählen Sie aus deutsch, englisch, französisch, spanisch oder griechisch")
language_wish = input()

#Get Data
def get_data(language_wish):
    try:
        #import pdb;pdb.set_trace()-> zum Debuggen
        statement = f"select Titel,Sprache from BuchDB.Buch where Sprache like \'{language_wish}\';"
        #data = (language_wish,) -> überflüssig da in select statement drin 
        cur.execute(statement)
        for(Titel, Sprache) in cur:
            print(f"Titel: {Titel}, Sprache: {Sprache}")
    except mariadb.Error as ex:
        print(f"Keine Buch in der Sprache verfügbar: {ex}")

get_data(language_wish)
conn.close()
