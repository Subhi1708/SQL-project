import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="movies"
)
mycursor=mydb.cursor()

def Aayalan():
    
    mycursor.execute ("select * from movies_list where movie='Ayalaan' ")
    myresult=mycursor.fetchall()
    insert_query = "INSERT INTO ayalaan_movies (id, name, movie, Actor, year) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(insert_query, myresult)

    mydb.commit()
    print("Uploaded Ayalaan Successfully")
Aayalan()

def kanguva():
    mycursor.execute ("select * from movies_list where movie='Kanguva' ")
    myresult=mycursor.fetchall()
    insert_query = "INSERT INTO kanguva_movies (id, name, movie, Actor, year) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(insert_query, myresult)

    mydb.commit()
    print("Uploaded kanguva Successfully")
kanguva()

def lover():
    mycursor.execute ("select * from movies_list where movie='Lover' ")
    myresult=mycursor.fetchall()
    insert_query = "INSERT INTO lover_movies (id, name, movie, Actor, year) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(insert_query, myresult)

    mydb.commit()
    print("Uploaded lover Successfully")
lover()

def Garudan():
    mycursor.execute ("select * from movies_list where movie='Garudan' ")
    myresult=mycursor.fetchall()
    insert_query = "INSERT INTO garudan_movies (id, name, movie, Actor, year) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(insert_query, myresult)

    mydb.commit()
    print("Uploaded garudan Successfully")
Garudan()

def Siren():
    mycursor.execute ("select * from movies_list where movie='Siren' ")
    myresult=mycursor.fetchall()
    insert_query = "INSERT INTO siren_movies (id, name, movie, Actor, year) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(insert_query, myresult)

    mydb.commit()
    print("Uploaded Siren Successfully")
Siren()

# Close the cursor and connection
mycursor.close()
mydb.close()

