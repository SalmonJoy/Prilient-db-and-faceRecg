import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "users"
)

mycursor = mydb.cursor()

insert_query = "INSERT INTO myusers (names) VALUES (%s)"
values = ("Suresh Iyer",)
mycursor.execute(insert_query,values)
mydb.commit()

read_query = "SELECT * FROM myusers"
mycursor.execute(read_query)
result = mycursor.fetchall()
print(result)