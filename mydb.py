import mysql.connector



dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'go',
    passwd = 'ahmedsaiko5'

)


# Prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE soudy")


print("All done and database is created")

