import json


f = open("rates.json")
data = json.load(f)

accData = {}
for row in data:
    accData[row["symbol"]] = {}
    accData[row["symbol"]]["name"] = row["name"]
    accData[row["symbol"]]["label"] = row["symbol"].upper()+"/CAD"
    accData[row["symbol"]]["rates"] = {}
    for i in range(len(row['rates'])):
        accData[row["symbol"]]["rates"][row['rates'][i]['d']] = row['rates'][i]["FX" + row["symbol"].upper()+"CAD"]['v']

json.dump(accData, open("ratesdf.json", "w"), indent=4)