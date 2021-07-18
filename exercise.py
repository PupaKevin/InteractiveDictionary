import mysql.connector

con = mysql.connector.connect(
    user=" ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()
query = cursor.execute("select * FROM Dictionary WHERE expression = 'line'")
results = cursor.fetchall()


for result in results:
    print(results)
