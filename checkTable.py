import dataBaseStuff


def test_new_table():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
