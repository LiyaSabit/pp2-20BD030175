import psycopg2,csv
from conn import data
conn = psycopg2.connect(**data)
current = conn.cursor()

insert = """
    INSERT INTO Hospital (Hospital_Name, Bed_Count) VALUES(%s,%s) returning *;
"""

update = """
    UPDATE Hospital SET Bed_Count = %s WHERE Hospital_Name = %s;
"""

select = """
    SELECT * FROM Hospital;
    SELECT AVG(Bed_Count)
    FROM Hospital
"""
order = """
    SELECT *
    FROM Hospital
    WHERE Bed_Count > 600
    ORDER BY Bed_Count DESC;
"""

delete = """
    DELETE FROM Hospital WHERE Hospital_Name = %s;
"""
sql ='''CREATE TABLE Hospital (
   Hospital_Id SERIAL PRIMARY KEY,
   Hospital_Name VARCHAR NOT NULL,
   Bed_Count SERIAL
)'''
#current.execute(sql)

while True:
    command = input("insert, order, update, select, delete, exit\n")
    if command == 'insert':
        name = input("Hospital name:")
        beds = input("Beds Count:")
        current.execute(insert, (name, beds))
        conn.commit()
    if command == 'update':
        name = input("Hospital name:")
        beds = input("Beds Count:")
        current.execute(update, (beds,name))
        conn.commit()
    if command == 'order':
        current.execute(order)
        conn.commit()
    if command == 'select':
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        conn.commit()
    if command == 'delete':
        name = input("Hospital name:")
        current.execute(delete, (name,))
        conn.commit()
    if command == 'exit':
        break

current.close()
conn.commit()
conn.close()