import psycopg2

connection = psycopg2.connect(database = "test",
                              user = "postgres",
                              password = "123456", 
                              host="localhost",
                              port = 5432)

cursor = connection.cursor()

name = input("Enter your name")
url = input("Enter the url")

cursor.execute("INSERT INTO test(name,dataurl) VALUES('{0}','{1}')".format(name,url))
connection.commit()

cursor.execute("SELECT * from test")

result = cursor.fetchall()
print("Database Data:- ",result)