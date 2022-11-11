import psycopg2

conn = psycopg2.connect(dbname="fx_rates", user="postgres", password="postgres", host="localhost", port="5432")
cursor = conn.cursor()

cursor.execute("SELECT * FROM boc_rates")
rows = cursor.fetchall()
for row in rows:
    print(row)