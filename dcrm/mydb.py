import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='your_new_password',
)


cursorObject = dataBase.cursor()


cursorObject.execute('CREATE DATABASE IF NOT EXISTS webAPP')

print("all ready")



