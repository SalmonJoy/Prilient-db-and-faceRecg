import psycopg2
import cv2
import numpy as np

connection = psycopg2.connect(database = "faces",
                              user = "postgres",
                              password = "123456", 
                              host="localhost",
                              port = 5432)

cursor = connection.cursor()

image_size = 200

name = input("Enter your name")
image = cv2.imread("database\Satya.jpg")
image = cv2.resize(image,(image_size,image_size))
flattened_image = image.reshape(-1)
# print(flattened_image)
text = ','.join(str(x) for x in flattened_image)

# print(array)

# cursor.execute("INSERT INTO users(name,image_array) VALUES('{0}','{1}')".format(name,text))
# connection.commit()

cursor.execute("SELECT * from users")


result = cursor.fetchall()
user_id = 1
text = result[user_id][2]
array = text.split(",")
image_from_db = np.array(array).astype('uint8').reshape(image_size,image_size,3)
cv2.imshow("Image of "+result[user_id][1]+" from Database",image_from_db)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print("Database Data:- ",result[1][2])