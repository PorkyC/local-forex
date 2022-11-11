import psycopg2
import json

conn = psycopg2.connect(dbname="fx_rates", user="postgres", password="postgres", host="localhost", port="5432")
cursor = conn.cursor()

f = open("rates.json")
data = json.load(f)

for row in data:
    print(row)

cursor.execute("SELECT * FROM boc_rates")
rows = cursor.fetchall()
for row in rows:
    d = row[0].strftime("%Y-%m-%d")
    for i in range(1, len(row)):
        currency = "FX" + data[i-1]["symbol"].upper() + "CAD"
        v = row[i]
        if v:
            data[i-1]["rates"].append({"d": d, currency:{"v": str(v)}})

w = open("out.json", "w")
w.write(json.dumps(data, indent=4))
