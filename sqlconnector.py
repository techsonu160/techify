import mysql.connector

#conn=mysql.connector.connect(host='localhost',username='root',password='shivraj@1992',)
#for reconnecting reverse database
conn=mysql.connector.connect(host='localhost',username='root',password='shivraj@1992',database='tech_sonu')
my_cursor=conn.cursor()
#creating a database
#query="CREATE DATABASE tech_sonu"
query="SHOW  DATABASES"
#query="CREATE TABLE student(name VARCHAR(255),age INT)"
#INSERTING VALUE IN DATABASES
#query="INSERT INTO student(name,age)VALUE(%s,%s)"
values=[
    ('sonu',19),
    ('techno',20),
    ('aadi',17),
    ('karan',19)
]
query="SELECT * FROM student"
my_cursor.execute(query)
#my_cursor.execute(query,values)
#execute many
#my_cursor.executemany(query)
#for row in my_cursor:
#    print(row)
print(my_cursor.fetchall())


#SHOWING DATABASES
#for database_name in my_cursor:
#   print(database_name)


#my=my_cursor.fetchall()
#print(my)

conn.commit()
conn.close()
