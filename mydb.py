import mysql.connector;

dataBase = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="fred80fc", 
    port="3306",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE djangocrm")

print("ALL DONE")