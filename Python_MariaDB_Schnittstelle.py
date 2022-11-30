#!/usr/bin/python 
#import mariadb
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

#Retrieving Information 
print("Wählen Sie aus deutsch, englisch, französisch, spanisch oder griechisch")
language_wish = int(input())
cur.execute("SELECT Titel, Sprache FROM Buch WHERE Sprache=?", (language_wish,)) 

for Titel, Sprache in cur: 
    print(f"Titel: {Titel}, Sprache: {Sprache}")
    
#insert information 
#try: 
#    cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
#except mariadb.Error as e: 
#    print(f"Error: {e}")

#conn.commit() 
#print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()
